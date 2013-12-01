import logging
import minitel
import os
import subprocess
import pty
import fcntl
import time
from screen import Screen

class Timeout:
    def __init__(self,duration=-1):
        self.duration = duration
        self.stamp = time.time()
    def kick(self):
        self.stamp = time.time()
    def expired(self):
        if self.duration == -1: 
            return False # never expires
        else:
            return time.time() - self.stamp > self.duration

class RunProcess(Screen):
    def initialize(self,command=None,wait_on_exit=False,no_input_timeout=10*60,col80=True,lfcr=True,echo_off=False):
        logging.debug('Creating process hook for {}'.format(command))
        self.lfcr = lfcr
        self.command = command
        self.wait_on_exit = wait_on_exit
        self.no_input_timeout = no_input_timeout
        self.col80 = col80
        self.echo_off = echo_off

    def __call__(self,m,parents):
        self.parents = parents
        logging.debug('Running {}'.format(self.command))
        if self.col80:
            m.setMode(minitel.MODE_ANSI)
        if self.echo_off:
            m.send('\xec')
        m.clearScreen()
        m.setTextMode(minitel.NORMAL)
        m.moveCursor(0,0)
        master, slave = pty.openpty()
        env = os.environ
        env['TERM']='minitel1b-80'
        proc = subprocess.Popen(self.command,
                                stdin=subprocess.PIPE,
                                stdout=slave,
                                env=env)
        procout = os.fdopen(master)
        fl = fcntl.fcntl(master, fcntl.F_GETFL)
        fcntl.fcntl(master, fcntl.F_SETFL, fl | os.O_NONBLOCK)
        tout = Timeout(self.no_input_timeout)

        self.eat(m)
        while proc.poll() == None and not tout.expired():
            try:
                out = procout.read()
                if len(out) > 0:
                    m.send(out)
            except IOError:
                pass
            kp = m.recv(10)
            if kp:
                if self.lfcr:
                    kp = kp.replace('\r','\n')
                tout.kick()
                proc.stdin.write(kp)
            time.sleep(0.05)
        if self.wait_on_exit and not tout.expired():
            m.newline()
            m.setTextMode(minitel.BOLD)
            m.send('PRESS ANY KEY TO RETURN TO MENU')
            while not m.recv(1):
                pass
        if tout.expired():
            logging.info('Process timed out.')
        if proc.poll() == None:
            logging.info('Killing process.')
            proc.kill()
        logging.debug('{} done; return code {}'.format(self.command,proc.poll()))

