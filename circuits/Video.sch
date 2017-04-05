EESchema Schematic File Version 2
LIBS:power
LIBS:device
LIBS:transistors
LIBS:conn
LIBS:linear
LIBS:regul
LIBS:74xx
LIBS:cmos4000
LIBS:adc-dac
LIBS:memory
LIBS:xilinx
LIBS:microcontrollers
LIBS:dsp
LIBS:microchip
LIBS:analog_switches
LIBS:motorola
LIBS:texas
LIBS:intel
LIBS:audio
LIBS:interface
LIBS:digital-audio
LIBS:philips
LIBS:display
LIBS:cypress
LIBS:siliconi
LIBS:opto
LIBS:atmel
LIBS:contrib
LIBS:valves
EELAYER 25 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 1 1
Title ""
Date ""
Rev ""
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
Text GLabel 4150 2200 0    60   Input ~ 0
Video
Text GLabel 4150 2450 0    60   Input ~ 0
Shield
$Comp
L GND #PWR?
U 1 1 58E56085
P 4300 2550
F 0 "#PWR?" H 4300 2300 50  0001 C CNN
F 1 "GND" H 4300 2400 50  0000 C CNN
F 2 "" H 4300 2550 50  0000 C CNN
F 3 "" H 4300 2550 50  0000 C CNN
	1    4300 2550
	1    0    0    -1  
$EndComp
Wire Wire Line
	4150 2450 4300 2450
Wire Wire Line
	4300 2450 4300 2550
$Comp
L R R?
U 1 1 58E560C9
P 4500 2200
F 0 "R?" V 4580 2200 50  0000 C CNN
F 1 "100" V 4500 2200 50  0000 C CNN
F 2 "" V 4430 2200 50  0000 C CNN
F 3 "" H 4500 2200 50  0000 C CNN
	1    4500 2200
	0    1    1    0   
$EndComp
Wire Wire Line
	4150 2200 4350 2200
$Comp
L R R?
U 1 1 58E56266
P 4750 2050
F 0 "R?" V 4830 2050 50  0000 C CNN
F 1 "2.4K" V 4750 2050 50  0000 C CNN
F 2 "" V 4680 2050 50  0000 C CNN
F 3 "" H 4750 2050 50  0000 C CNN
	1    4750 2050
	1    0    0    -1  
$EndComp
$Comp
L R R?
U 1 1 58E562EB
P 4900 2050
F 0 "R?" V 4980 2050 50  0000 C CNN
F 1 "2.4K" V 4900 2050 50  0000 C CNN
F 2 "" V 4830 2050 50  0000 C CNN
F 3 "" H 4900 2050 50  0000 C CNN
	1    4900 2050
	1    0    0    -1  
$EndComp
Wire Wire Line
	4650 2200 4900 2200
Connection ~ 4750 2200
Wire Wire Line
	4550 1900 4900 1900
Text GLabel 4550 1900 0    60   Input ~ 0
+52V
Connection ~ 4750 1900
$EndSCHEMATC
