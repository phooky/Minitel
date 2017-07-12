
Framebuffer
===========

The tilcdc driver provides a framebuffer on /dev/fb0. The resolution of this
framebuffer is 320x256. 
LAST COLUMN MUST BE SET TO 0 TO AVOID A BRIGHT LINE DURING ENTIRE HORIZ. RETRACT

Create fb0:
echo "MINITEL-TILCDC" >>/sys/devices/platform/bone_capemgr/slots

Detatch the console on fb0:
echo 0 >/sys/class/vtconsole/vtcon1/bind

Disable screen blanking:
echo 0 >/sys/class/graphics/fb0/blank

fbpad is build to default to fb0.

KERNEL VERSION:
debian@beaglebone:~$ cat /proc/version 
Linux version 4.4.36-ti-r72 (root@a2-imx6q-wandboard-2gb) (gcc version 4.9.2 (Debian 4.9.2-10) ) #1 SMP Wed Dec 7 22:29:53 UTC 2016
debian@beaglebone:~$ lsb -a
-bash: lsb: command not found
debian@beaglebone:~$ lsb
lsblk        lsb_release  
debian@beaglebone:~$ lsb_release -a
No LSB modules are available.
Distributor ID: Debian
Description:    Debian GNU/Linux 8.6 (jessie)
Release:    8.6
Codename:   jessie

Warning: there is a newer version with missing capemgr!


