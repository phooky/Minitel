EESchema Schematic File Version 2
LIBS:local
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
Title "Minitel 1 (US Version) Video Adapter Board"
Date ""
Rev ""
Comp "phooky"
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
$Comp
L 74HC04 U2
U 1 1 58F22E97
P 5950 2300
F 0 "U2" H 6100 2400 50  0000 C CNN
F 1 "74HC04" H 6150 2200 50  0000 C CNN
F 2 "" H 5950 2300 50  0000 C CNN
F 3 "" H 5950 2300 50  0000 C CNN
	1    5950 2300
	1    0    0    -1  
$EndComp
$Comp
L 74HC04 U2
U 2 1 58F22F28
P 5950 2700
F 0 "U2" H 6100 2800 50  0000 C CNN
F 1 "74HC04" H 6150 2600 50  0000 C CNN
F 2 "" H 5950 2700 50  0000 C CNN
F 3 "" H 5950 2700 50  0000 C CNN
	2    5950 2700
	1    0    0    -1  
$EndComp
$Comp
L 74HC04 U2
U 3 1 58F22F4B
P 5950 3100
F 0 "U2" H 6100 3200 50  0000 C CNN
F 1 "74HC04" H 6150 3000 50  0000 C CNN
F 2 "" H 5950 3100 50  0000 C CNN
F 3 "" H 5950 3100 50  0000 C CNN
	3    5950 3100
	1    0    0    -1  
$EndComp
$Comp
L 74HC04 U2
U 4 1 58F22F74
P 5950 3500
F 0 "U2" H 6100 3600 50  0000 C CNN
F 1 "74HC04" H 6150 3400 50  0000 C CNN
F 2 "" H 5950 3500 50  0000 C CNN
F 3 "" H 5950 3500 50  0000 C CNN
	4    5950 3500
	1    0    0    -1  
$EndComp
$Comp
L 74HC04 U2
U 5 1 58F2301A
P 6550 4300
F 0 "U2" H 6700 4400 50  0000 C CNN
F 1 "74HC04" H 6750 4200 50  0000 C CNN
F 2 "" H 6550 4300 50  0000 C CNN
F 3 "" H 6550 4300 50  0000 C CNN
	5    6550 4300
	1    0    0    -1  
$EndComp
$Comp
L 74HC04 U2
U 6 1 58F2310F
P 8750 3700
F 0 "U2" H 8900 3800 50  0000 C CNN
F 1 "74HC04" H 8950 3600 50  0000 C CNN
F 2 "" H 8750 3700 50  0000 C CNN
F 3 "" H 8750 3700 50  0000 C CNN
	6    8750 3700
	0    -1   -1   0   
$EndComp
$Comp
L CONN_01X07 P2
U 1 1 58F232A1
P 9900 2550
F 0 "P2" H 9900 2950 50  0000 C CNN
F 1 "CONN_01X07" V 10000 2550 50  0000 C CNN
F 2 "" H 9900 2550 50  0000 C CNN
F 3 "" H 9900 2550 50  0000 C CNN
	1    9900 2550
	1    0    0    -1  
$EndComp
$Comp
L GND #PWR01
U 1 1 58F23403
P 9050 3250
F 0 "#PWR01" H 9050 3000 50  0001 C CNN
F 1 "GND" H 9050 3100 50  0000 C CNN
F 2 "" H 9050 3250 50  0000 C CNN
F 3 "" H 9050 3250 50  0000 C CNN
	1    9050 3250
	1    0    0    -1  
$EndComp
$Comp
L 7805 U3
U 1 1 58F23540
P 9900 3500
F 0 "U3" H 10050 3304 50  0000 C CNN
F 1 "7805" H 9900 3700 50  0000 C CNN
F 2 "" H 9900 3500 50  0000 C CNN
F 3 "" H 9900 3500 50  0000 C CNN
	1    9900 3500
	1    0    0    -1  
$EndComp
$Comp
L VCC #PWR02
U 1 1 58F23654
P 10450 3450
F 0 "#PWR02" H 10450 3300 50  0001 C CNN
F 1 "VCC" H 10450 3600 50  0000 C CNN
F 2 "" H 10450 3450 50  0000 C CNN
F 3 "" H 10450 3450 50  0000 C CNN
	1    10450 3450
	0    1    1    0   
$EndComp
$Comp
L GND #PWR03
U 1 1 58F23689
P 9900 3950
F 0 "#PWR03" H 9900 3700 50  0001 C CNN
F 1 "GND" H 9900 3800 50  0000 C CNN
F 2 "" H 9900 3950 50  0000 C CNN
F 3 "" H 9900 3950 50  0000 C CNN
	1    9900 3950
	1    0    0    -1  
$EndComp
Text GLabel 8650 4300 0    60   Input ~ 0
SYNC
$Comp
L D D4
U 1 1 58F237A3
P 5300 3950
F 0 "D4" H 5300 4050 50  0000 C CNN
F 1 "1N4148" H 5300 3850 50  0000 C CNN
F 2 "" H 5300 3950 50  0000 C CNN
F 3 "" H 5300 3950 50  0000 C CNN
	1    5300 3950
	0    -1   -1   0   
$EndComp
$Comp
L D D3
U 1 1 58F23831
P 5000 3950
F 0 "D3" H 5000 4050 50  0000 C CNN
F 1 "1N4148" H 5000 3850 50  0000 C CNN
F 2 "" H 5000 3950 50  0000 C CNN
F 3 "" H 5000 3950 50  0000 C CNN
	1    5000 3950
	0    -1   -1   0   
$EndComp
$Comp
L D D2
U 1 1 58F2386F
P 4700 3950
F 0 "D2" H 4700 4050 50  0000 C CNN
F 1 "1N4148" H 4700 3850 50  0000 C CNN
F 2 "" H 4700 3950 50  0000 C CNN
F 3 "" H 4700 3950 50  0000 C CNN
	1    4700 3950
	0    -1   -1   0   
$EndComp
$Comp
L D D1
U 1 1 58F238B0
P 4400 3950
F 0 "D1" H 4400 4050 50  0000 C CNN
F 1 "1N4148" H 4400 3850 50  0000 C CNN
F 2 "" H 4400 3950 50  0000 C CNN
F 3 "" H 4400 3950 50  0000 C CNN
	1    4400 3950
	0    -1   -1   0   
$EndComp
$Comp
L CONN_01X06 P1
U 1 1 58F23AA2
P 1200 2550
F 0 "P1" H 1200 2900 50  0000 C CNN
F 1 "CONN_01X06" V 1300 2550 50  0000 C CNN
F 2 "" H 1200 2550 50  0000 C CNN
F 3 "" H 1200 2550 50  0000 C CNN
	1    1200 2550
	-1   0    0    1   
$EndComp
Text GLabel 3850 3150 0    60   Input ~ 0
SYNC
$Comp
L GND #PWR04
U 1 1 58F23BA6
P 1500 3450
F 0 "#PWR04" H 1500 3200 50  0001 C CNN
F 1 "GND" H 1500 3300 50  0000 C CNN
F 2 "" H 1500 3450 50  0000 C CNN
F 3 "" H 1500 3450 50  0000 C CNN
	1    1500 3450
	1    0    0    -1  
$EndComp
NoConn ~ 9700 2650
NoConn ~ 9700 2850
$Comp
L 74LS244 U1
U 1 1 58F27E95
P 2600 2800
F 0 "U1" H 2650 2600 50  0000 C CNN
F 1 "74LS244" H 2700 2400 50  0000 C CNN
F 2 "" H 2600 2800 50  0000 C CNN
F 3 "" H 2600 2800 50  0000 C CNN
	1    2600 2800
	1    0    0    -1  
$EndComp
Wire Wire Line
	9700 2750 9350 2750
Wire Wire Line
	9350 2750 9350 3450
Wire Wire Line
	9350 3450 9500 3450
Wire Wire Line
	10300 3450 10450 3450
Wire Wire Line
	9900 3750 9900 3950
Wire Wire Line
	8650 4300 8750 4300
Wire Wire Line
	8750 4300 8750 4150
Wire Wire Line
	5300 4300 5300 4100
Wire Wire Line
	4400 4300 5600 4300
Wire Wire Line
	5300 3800 5300 3500
Wire Wire Line
	4100 3500 5500 3500
Wire Wire Line
	4200 3100 5500 3100
Wire Wire Line
	5000 3100 5000 3800
Wire Wire Line
	5000 4100 5000 4300
Connection ~ 5300 4300
Wire Wire Line
	4700 4100 4700 4300
Connection ~ 5000 4300
Wire Wire Line
	4400 4100 4400 4300
Connection ~ 4700 4300
Wire Wire Line
	4700 3800 4700 2700
Wire Wire Line
	4300 2700 5500 2700
Wire Wire Line
	4400 3800 4400 2300
Wire Wire Line
	3300 2300 5500 2300
Wire Wire Line
	1400 2800 1900 2800
Wire Wire Line
	1500 2800 1500 3450
Wire Wire Line
	3850 3150 3900 3150
Wire Wire Line
	3900 3150 3900 2700
Wire Wire Line
	3900 2700 3300 2700
Wire Wire Line
	3300 2600 4100 2600
Wire Wire Line
	4100 2600 4100 3500
Connection ~ 5300 3500
Wire Wire Line
	3300 2500 4200 2500
Wire Wire Line
	4200 2500 4200 3100
Connection ~ 5000 3100
Wire Wire Line
	3300 2400 4300 2400
Wire Wire Line
	4300 2400 4300 2700
Connection ~ 4700 2700
Connection ~ 4400 2300
Wire Wire Line
	9050 3250 9050 2550
Wire Wire Line
	9050 2550 9700 2550
Wire Wire Line
	8750 3250 8750 2450
Wire Wire Line
	8750 2450 9700 2450
Wire Wire Line
	1900 3200 1500 3200
Connection ~ 1500 3200
Wire Wire Line
	1900 3300 1500 3300
Connection ~ 1500 3300
Wire Wire Line
	1400 2700 1900 2700
Wire Wire Line
	1400 2600 1900 2600
Wire Wire Line
	1400 2500 1900 2500
Wire Wire Line
	1400 2400 1900 2400
Wire Wire Line
	1400 2300 1900 2300
Connection ~ 1500 2800
Wire Wire Line
	1900 2900 1500 2900
Connection ~ 1500 2900
Wire Wire Line
	1900 3000 1500 3000
Connection ~ 1500 3000
$Comp
L R R1
U 1 1 58F287FA
P 5750 4300
F 0 "R1" V 5830 4300 50  0000 C CNN
F 1 "680" V 5750 4300 50  0000 C CNN
F 2 "" V 5680 4300 50  0000 C CNN
F 3 "" H 5750 4300 50  0000 C CNN
	1    5750 4300
	0    1    1    0   
$EndComp
Wire Wire Line
	5900 4300 6100 4300
$Comp
L Q_NPN_CBE Q1
U 1 1 58F28961
P 7300 1850
F 0 "Q1" H 7600 1900 50  0000 R CNN
F 1 "C5468" H 7900 1800 50  0000 R CNN
F 2 "" H 7500 1950 50  0000 C CNN
F 3 "" H 7300 1850 50  0000 C CNN
	1    7300 1850
	1    0    0    -1  
$EndComp
$Comp
L R R7
U 1 1 58F28A42
P 7400 1200
F 0 "R7" V 7480 1200 50  0000 C CNN
F 1 "100" V 7400 1200 50  0000 C CNN
F 2 "" V 7330 1200 50  0000 C CNN
F 3 "" H 7400 1200 50  0000 C CNN
	1    7400 1200
	1    0    0    -1  
$EndComp
Wire Wire Line
	7400 1350 7400 1650
$Comp
L COAX CX1
U 1 1 58F28BCD
P 8400 1250
F 0 "CX1" H 8400 1850 60  0000 C CNN
F 1 "COAX" H 8400 1250 60  0000 C CNN
F 2 "" H 8400 1250 60  0000 C CNN
F 3 "" H 8400 1250 60  0000 C CNN
	1    8400 1250
	1    0    0    -1  
$EndComp
Wire Wire Line
	7400 1050 7400 950 
Wire Wire Line
	7400 950  8000 950 
$Comp
L GND #PWR05
U 1 1 58F28C88
P 7800 800
F 0 "#PWR05" H 7800 550 50  0001 C CNN
F 1 "GND" H 7800 650 50  0000 C CNN
F 2 "" H 7800 800 50  0000 C CNN
F 3 "" H 7800 800 50  0000 C CNN
	1    7800 800 
	0    1    1    0   
$EndComp
$Comp
L GND #PWR06
U 1 1 58F28CC0
P 7800 1100
F 0 "#PWR06" H 7800 850 50  0001 C CNN
F 1 "GND" H 7800 950 50  0000 C CNN
F 2 "" H 7800 1100 50  0000 C CNN
F 3 "" H 7800 1100 50  0000 C CNN
	1    7800 1100
	0    1    1    0   
$EndComp
Wire Wire Line
	7800 1100 8000 1100
Wire Wire Line
	7800 800  8000 800 
$Comp
L R R9
U 1 1 58F28D99
P 8550 1500
F 0 "R9" V 8630 1500 50  0000 C CNN
F 1 "2.4K" V 8550 1500 50  0000 C CNN
F 2 "" V 8480 1500 50  0000 C CNN
F 3 "" H 8550 1500 50  0000 C CNN
	1    8550 1500
	0    1    1    0   
$EndComp
$Comp
L R R10
U 1 1 58F28E74
P 8550 1750
F 0 "R10" V 8630 1750 50  0000 C CNN
F 1 "2.4K" V 8550 1750 50  0000 C CNN
F 2 "" V 8480 1750 50  0000 C CNN
F 3 "" H 8550 1750 50  0000 C CNN
	1    8550 1750
	0    1    1    0   
$EndComp
Wire Wire Line
	7400 1500 8400 1500
Connection ~ 7400 1500
Wire Wire Line
	8250 1500 8250 1750
Wire Wire Line
	8250 1750 8400 1750
Connection ~ 8250 1500
Wire Wire Line
	8700 1750 9450 1750
Wire Wire Line
	9450 1650 9450 2250
Wire Wire Line
	9450 2250 9700 2250
Wire Wire Line
	8700 1500 8850 1500
Wire Wire Line
	8850 1500 8850 1750
Connection ~ 8850 1750
$Comp
L C C2
U 1 1 58F29076
P 9450 1500
F 0 "C2" H 9475 1600 50  0000 L CNN
F 1 "100nF" H 9475 1400 50  0000 L CNN
F 2 "" H 9488 1350 50  0000 C CNN
F 3 "" H 9450 1500 50  0000 C CNN
	1    9450 1500
	1    0    0    -1  
$EndComp
$Comp
L GND #PWR07
U 1 1 58F29128
P 9450 1200
F 0 "#PWR07" H 9450 950 50  0001 C CNN
F 1 "GND" H 9450 1050 50  0000 C CNN
F 2 "" H 9450 1200 50  0000 C CNN
F 3 "" H 9450 1200 50  0000 C CNN
	1    9450 1200
	-1   0    0    1   
$EndComp
Wire Wire Line
	9450 1200 9450 1350
Connection ~ 9450 1750
$Comp
L INDUCTOR L1
U 1 1 58F29228
P 6700 1450
F 0 "L1" V 6650 1450 50  0000 C CNN
F 1 "20uH" V 6800 1450 50  0000 C CNN
F 2 "" H 6700 1450 50  0000 C CNN
F 3 "" H 6700 1450 50  0000 C CNN
	1    6700 1450
	-1   0    0    1   
$EndComp
$Comp
L VCC #PWR08
U 1 1 58F292A5
P 6700 950
F 0 "#PWR08" H 6700 800 50  0001 C CNN
F 1 "VCC" H 6700 1100 50  0000 C CNN
F 2 "" H 6700 950 50  0000 C CNN
F 3 "" H 6700 950 50  0000 C CNN
	1    6700 950 
	1    0    0    -1  
$EndComp
Wire Wire Line
	6700 950  6700 1150
Wire Wire Line
	6700 1750 6700 1850
Wire Wire Line
	6700 1850 7100 1850
$Comp
L C C1
U 1 1 58F2940C
P 9150 2150
F 0 "C1" H 9175 2250 50  0000 L CNN
F 1 "10nF" H 9175 2050 50  0000 L CNN
F 2 "" H 9188 2000 50  0000 C CNN
F 3 "" H 9150 2150 50  0000 C CNN
	1    9150 2150
	1    0    0    -1  
$EndComp
Wire Wire Line
	8550 2350 9700 2350
Wire Wire Line
	9150 2350 9150 2300
Wire Wire Line
	9150 2000 9150 1300
Wire Wire Line
	9150 1300 9450 1300
Connection ~ 9450 1300
$Comp
L R R8
U 1 1 58F2968C
P 8400 2350
F 0 "R8" V 8480 2350 50  0000 C CNN
F 1 "1.2K" V 8400 2350 50  0000 C CNN
F 2 "" V 8330 2350 50  0000 C CNN
F 3 "" H 8400 2350 50  0000 C CNN
	1    8400 2350
	0    1    1    0   
$EndComp
Connection ~ 9150 2350
Wire Wire Line
	7400 2050 7400 3850
Wire Wire Line
	7400 2350 8250 2350
$Comp
L POT RV1
U 1 1 58F298D9
P 7000 2300
F 0 "RV1" H 7000 2220 50  0000 C CNN
F 1 "POT" H 7000 2300 50  0000 C CNN
F 2 "" H 7000 2300 50  0000 C CNN
F 3 "" H 7000 2300 50  0000 C CNN
	1    7000 2300
	1    0    0    -1  
$EndComp
$Comp
L POT RV2
U 1 1 58F29997
P 7000 2700
F 0 "RV2" H 7000 2620 50  0000 C CNN
F 1 "POT" H 7000 2700 50  0000 C CNN
F 2 "" H 7000 2700 50  0000 C CNN
F 3 "" H 7000 2700 50  0000 C CNN
	1    7000 2700
	1    0    0    -1  
$EndComp
$Comp
L POT RV3
U 1 1 58F299E6
P 7000 3100
F 0 "RV3" H 7000 3020 50  0000 C CNN
F 1 "POT" H 7000 3100 50  0000 C CNN
F 2 "" H 7000 3100 50  0000 C CNN
F 3 "" H 7000 3100 50  0000 C CNN
	1    7000 3100
	1    0    0    -1  
$EndComp
$Comp
L POT RV4
U 1 1 58F29A35
P 7000 3500
F 0 "RV4" H 7000 3420 50  0000 C CNN
F 1 "POT" H 7000 3500 50  0000 C CNN
F 2 "" H 7000 3500 50  0000 C CNN
F 3 "" H 7000 3500 50  0000 C CNN
	1    7000 3500
	1    0    0    -1  
$EndComp
Wire Wire Line
	7000 2150 7400 2150
Connection ~ 7400 2150
Wire Wire Line
	7400 2550 7000 2550
Connection ~ 7400 2350
Wire Wire Line
	7400 2950 7000 2950
Connection ~ 7400 2550
Wire Wire Line
	7400 3350 7000 3350
Connection ~ 7400 2950
$Comp
L POT RV5
U 1 1 58F29FCA
P 7550 3850
F 0 "RV5" H 7550 3770 50  0000 C CNN
F 1 "POT" H 7550 3850 50  0000 C CNN
F 2 "" H 7550 3850 50  0000 C CNN
F 3 "" H 7550 3850 50  0000 C CNN
	1    7550 3850
	0    -1   -1   0   
$EndComp
Connection ~ 7400 3350
$Comp
L R R6
U 1 1 58F2A0FB
P 7300 4300
F 0 "R6" V 7380 4300 50  0000 C CNN
F 1 "620" V 7300 4300 50  0000 C CNN
F 2 "" V 7230 4300 50  0000 C CNN
F 3 "" H 7300 4300 50  0000 C CNN
	1    7300 4300
	0    1    1    0   
$EndComp
$Comp
L R R5
U 1 1 58F2A1C4
P 6600 3500
F 0 "R5" V 6680 3500 50  0000 C CNN
F 1 "460" V 6600 3500 50  0000 C CNN
F 2 "" V 6530 3500 50  0000 C CNN
F 3 "" H 6600 3500 50  0000 C CNN
	1    6600 3500
	0    1    1    0   
$EndComp
$Comp
L R R4
U 1 1 58F2A21B
P 6600 3100
F 0 "R4" V 6680 3100 50  0000 C CNN
F 1 "1K" V 6600 3100 50  0000 C CNN
F 2 "" V 6530 3100 50  0000 C CNN
F 3 "" H 6600 3100 50  0000 C CNN
	1    6600 3100
	0    1    1    0   
$EndComp
$Comp
L R R3
U 1 1 58F2A278
P 6600 2700
F 0 "R3" V 6680 2700 50  0000 C CNN
F 1 "1.8K" V 6600 2700 50  0000 C CNN
F 2 "" V 6530 2700 50  0000 C CNN
F 3 "" H 6600 2700 50  0000 C CNN
	1    6600 2700
	0    1    1    0   
$EndComp
$Comp
L R R2
U 1 1 58F2A2D5
P 6600 2300
F 0 "R2" V 6680 2300 50  0000 C CNN
F 1 "4K" V 6600 2300 50  0000 C CNN
F 2 "" V 6530 2300 50  0000 C CNN
F 3 "" H 6600 2300 50  0000 C CNN
	1    6600 2300
	0    1    1    0   
$EndComp
Wire Wire Line
	6400 3500 6450 3500
Wire Wire Line
	6400 3100 6450 3100
Wire Wire Line
	6400 2700 6450 2700
Wire Wire Line
	6400 2300 6450 2300
Wire Wire Line
	6750 2300 6850 2300
Wire Wire Line
	6750 2700 6850 2700
Wire Wire Line
	6750 3100 6850 3100
Wire Wire Line
	6750 3500 6850 3500
Wire Wire Line
	7000 4300 7150 4300
Wire Wire Line
	7450 4300 7550 4300
Wire Wire Line
	7550 4300 7550 4000
NoConn ~ 7150 2300
NoConn ~ 7150 2700
NoConn ~ 7150 3500
NoConn ~ 7150 3100
NoConn ~ 7550 3700
NoConn ~ 3300 2800
NoConn ~ 3300 2900
NoConn ~ 3300 3000
$Comp
L PWR_FLAG #FLG09
U 1 1 58F2DC65
P 9100 3000
F 0 "#FLG09" H 9100 3095 50  0001 C CNN
F 1 "PWR_FLAG" H 9100 3180 50  0000 C CNN
F 2 "" H 9100 3000 50  0000 C CNN
F 3 "" H 9100 3000 50  0000 C CNN
	1    9100 3000
	0    1    1    0   
$EndComp
Wire Wire Line
	9100 3000 9050 3000
Connection ~ 9050 3000
$EndSCHEMATC
