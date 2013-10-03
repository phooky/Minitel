Minitel 1B utility scripts
==========================

minitel.py is a script for connecting to a minitel terminal over a serial port and writing data to it from stdin or one or more files. It can also be used to send hex codes directly to the minitel, as well as a clear code or one of several test patterns. Try "python minitel.py --help" for options.

minitel.py also provides a Minitel class that may be used by other python scripts that want to communicate with the Minitel. It's documented in docstrings, so you can "import minitel; help(minitel.Minitel)" in python for details.

mtimage.py converts any normal image type into a full-screen image for the minitel. It provides a Converter class for use by other scripts as well.

tumblr-mt.py is a script that searches Tumblr for posts matching the provided tags, finds the photo posts, and displays them on the Minitel. If no arguments are provided it displays a prompt and waits for tags to be entered by the user at the Minitel terminal.

Using the Minitel to interact with terminal programs
----------------------------------------------------

You'll want to begin by setting the minitel into 80-column mode (fn-M A) and 4800 baud mode (fn-B 4). Then:

* Set up and open a serial connection to the minitel. If you've put the minitel in 4800 baud mode (say, with Fn-B 4), then:

```Shell
    minicom -D /dev/ttyUSB0 -b 4800
```
Leave the connection open by exiting with Ctrl-A J.

* Set the tty to do newline processing correctly

```Shell
    stty opost onlcr icrnl </dev/ttyUSB0
```
* Redirect your terminal program to talk to the minitel

```Shell
    adventure </dev/ttyUSB0 >/dev/ttyUSB0
```
