; blink.p: demonstration of PRU on the BeagleBone Black
; blink LED connected to P8_11 ten times
.origin 0
.entrypoint TOP
TOP:
  MOV r1, 10 ; blink counter
BLINK:
  SET r30, r30, 15 ; set GPIO output 15
  MOV r0, 0x00a00000 ; delay counter
DELAY:
  SUB r0, r0, 1
  QBNE DELAY, r0, 0 ; loop until r0 == 0 (delay)
  CLR r30, r30, 15  ; clear GPIO output 15
  MOV r0, 0x00a00000 ; delay counter
DELAY2:
  SUB r0, r0, 1
  QBNE DELAY2, r0, 0 ; loop until r0 == 0 (delay)
  SUB r1, r1, 1
  QBNE BLINK, r1, 0 ; loop until r1 = 0 (blink counter)
  MOV r31.b0, 32 + 3
  HALT