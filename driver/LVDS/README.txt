To build and install device tree overlay:

	dtc -O dtb -I dts -o /lib/firmware/MINITEL-TILCDC-00A0.dtbo -b 0 -@ MINITEL-TILCDC-00A0.dts

To load the overlay:

	echo "MINITEL-TILCDC" >> /sys/devices/platform/bone_capemgr/slots


