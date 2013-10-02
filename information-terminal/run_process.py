import logging
import minitel
import os
import subprocess
import pty
import fcntl
import time

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

def make_run_process(command,wait_on_exit=False,no_input_timeout=10*60):
    logging.debug('Creating process hook for {}'.format(command))
    def fn(m, parents):
        logging.debug('Running {}'.format(command))
        m.clearScreen()
        m.setTextMode(minitel.NORMAL)
        m.moveCursor(0,0)
        master, slave = pty.openpty()
        proc = subprocess.Popen(command,
                                stdin=subprocess.PIPE,
                                stdout=slave,
                                env={'TERM':'vt100'})
        procout = os.fdopen(master)
        fl = fcntl.fcntl(master, fcntl.F_GETFL)
        fcntl.fcntl(master, fcntl.F_SETFL, fl | os.O_NONBLOCK)
        tout = Timeout(no_input_timeout)
        while proc.poll() == None and not tout.expired():
            try:
                out = procout.read()
                if len(out) > 0:
                    m.send(out)
            except IOError:
                pass
            kp = m.recv(10)
            if kp:
                tout.kick()
                proc.stdin.write(kp)
            time.sleep(0.05)
        if wait_on_exit and not tout.expired():
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
        logging.debug('{} done; return code {}'.format(command,proc.poll()))
    return fn