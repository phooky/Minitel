import logging
import minitel
import os
import subprocess
import pty
import fcntl
import time

def make_run_process(command,wait_on_exit=False):
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
        logging.debug('Nonblocking mode on {}'.format(master))
        while proc.poll() == None:
            try:
                try:
                    out = procout.read()
                    if len(out) > 0:
                        m.send(out)
                except IOError:
                    pass
                kp = m.recv(10)
                if kp:
                    proc.stdin.write(kp)
            except:
                logging.exception('oops')
            time.sleep(0.05)
        if wait_on_exit:
            m.newline()
            m.setTextMode(minitel.BOLD)
            m.send('PRESS ANY KEY TO RETURN TO MENU')
            while not m.recv(1):
                pass
        logging.debug('{} done; return code {}'.format(command,proc.poll()))
    return fn
