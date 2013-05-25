Minitel 1B utility scripts
==========================

minitel.py is a script for connecting to a minitel terminal over a serial port and writing data to it from stdin or one or more files. It can also be used to send hex codes directly to the minitel, as well as a clear code or one of several test patterns. Try "python minitel.py --help" for options.

minitel.py also provides a Minitel class that may be used by other python scripts that want to communicate with the Minitel. It's documented in docstrings, so you can "import minitel; help(minitel.Minitel)" in python for details.

mtimage.py converts any normal image type into a full-screen image for the minitel. It provides a Converter class for use by other scripts as well.

tumblr-mt.py is a script that searches Tumblr for posts matching the provided tags, finds the photo posts, and displays them on the Minitel. If no arguments are provided it displays a prompt and waits for tags to be entered by the user at the Minitel terminal.

