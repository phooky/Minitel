; Driver for the monitor of a Minitel 1B (weird US edition).
; The horizontal line frequency is 15.63kHz.

#define SYNC_BIT 0
#define V0_BIT 5
#define V1_BIT 3
#define V2_BIT 1
#define V3_BIT 2

#define NOP ADD r0, r0, 0

#define DATA_ROWS 310
#define RETRACE_ROWS 2
 

.origin 0
.entrypoint TOP
TOP:

  MOV r1, 10 ; blink counter
BLINK:
  SET r30, r30, 14 ; set GPIO output 15
  SET r30, r30, 15 ; set GPIO output 15
  MOV r0, 0x00a00000 ; delay counter
DELAY:
  SUB r0, r0, 1
  QBNE DELAY, r0, 0 ; loop until r0 == 0 (delay)
  CLR r30, r30, 14  ; clear GPIO output 15
  CLR r30, r30, 15  ; clear GPIO output 15
  MOV r0, 0x00a00000 ; delay counter
DELAY2:
  SUB r0, r0, 1
  QBNE DELAY2, r0, 0 ; loop until r0 == 0 (delay)
  SUB r1, r1, 1
  QBNE BLINK, r1, 0 ; loop until r1 = 0 (blink counter)
  MOV r31.b0, 32 + 3
  HALT
