;;; Driver for the monitor of a Minitel 1B (weird US edition).
;;; The horizontal line frequency is 15.63kHz.
;;; Much of this code was poached from the IBM 5291 driver. 
  
#define SYNC_BIT 0
#define V0_BIT 5
#define V1_BIT 3
#define V2_BIT 1
    #define V3_BIT 2

#define NOP ADD r0, r0, 0

#define DATA_ROWS 310
#define TOTAL_ROWS 312

/** Register map */
#define data_addr r0
#define row r1
#define col r2
#define timer_ptr r4
#define pixel_data r5  // r5 - r20
#define pixdat_ptr r27
#define tmp1 r28
#define tmp2 r29

/** Reset the cycle counter. Should be invoked once at the start
    of each row. */
.macro resetcounter
    // Disable the counter and clear it, then re-enable it
    // This starts our clock at the start of the row.
    LBBO tmp2, timer_ptr, 0, 4
    CLR tmp2, tmp2, 3 // disable counter bit
    SBBO tmp2, timer_ptr, 0, 4 // write it back

    MOV r10, 20 // 20: compensate for cycles in macro
    SBBO r10, timer_ptr, 0xC, 4 // clear the timer

    SET tmp2, tmp2, 3 // enable counter bit
    SBBO tmp2, timer_ptr, 0, 4 // write it back
.endm

/** Wait for the cycle counter to hit the given absolute value.
    The counter is reset at the start of each row. */
.macro waitforns
.mparam ns
    MOV tmp1, (ns)/5;
waitloop:
    LBBO tmp2, timer_ptr, 0xC, 4; /* read the cycle counter */
    QBGT waitloop, tmp2, tmp1;
.endm

/** Synchronize to a 8-cycle boundry- 7 to 14 cycles */
.macro cyclesync
    LBBO tmp2, timer_ptr, 0xC, 4    // 3 cycles(?)
    AND tmp2, tmp2, 0x7             // 1 cycle
    LDI tmp1, noptable              // 1 cycle
    ADD tmp1, tmp2                  // 1 cycle
    JMP tmp1                        // 1 cycle
noptable:
    NOP
    NOP
    NOP
    NOP
    NOP
    NOP
    NOP
.endm
    
.origin 0
.entrypoint TOP
TOP:
    // Enable OCP master port
    // clear the STANDBY_INIT bit in the SYSCFG register,
    // otherwise the PRU will not be able to write outside the
    // PRU memory space and to the BeagleBone pins.
    LBCO    r0, C4, 4, 4
    CLR     r0, r0, 4
    SBCO    r0, C4, 4, 4

    MOV row, 0
    MOV col, 0
    MOV timer_ptr, 0x22000 /* control register */
    CLR r30, r30, SYNC_BIT
    resetcounter
HSYNC:
    SET r30, r30, SYNC_BIT // Remember, bits are inverted
    MOV tmp1, DATA_ROWS
    QBLT RETRACE_LINE, row, tmp1
    // load line from DDR; this is risky but *shrug*
    waitforns 4500
    CLR r30, r30, SYNC_BIT
    // set up pixdat_ptr
    MOV 
    // load first set of pixels
    // wait for start of drawn line
    // cycle sync
    // pixel 1
    // pixel 2
    // pixel 3
    // pixel 4
    // load next set
    // cycle sync

RETRACE_LINE:
    waitforns 63980
    ADD row, row, 1
    mov tmp1, TOTAL_ROWS
    QBGE SKIP_ROW_RESET, row, tmp1 
    MOV row, 0
SKIP_ROW_RESET: 
    resetcounter
    JMP HSYNC
