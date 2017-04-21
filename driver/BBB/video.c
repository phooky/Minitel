#include <stdio.h>
#include <stdlib.h>
#include <prussdrv.h>
#include <pruss_intc_mapping.h>

#define VRAM_WIDTH 512
#define VRAM_HEIGHT 300

void
vram_set(
	void * const vram_ptr,
	int x,
	int y,
	int val
)
{
	if (x < 0 || x >= VRAM_WIDTH)
		die("x %d", x);
	if (y < 0 || y >= VRAM_HEIGHT)
		die("y %d", y);

	volatile uint32_t * const vram = vram_ptr;

	volatile uint32_t * const p = &vram[x + y * VRAM_WIDTH];
        *p = val;
}
int main(int argc, char **argv) {
  if (argc != 2 && argc != 3) {
    printf("Usage: %s loader text.bin [data.bin]\n", argv[0]);
    return 1;
  }
	uint8_t * const vram = pru->ddr;

	memset(vram, 0x00, VRAM_WIDTH*VRAM_HEIGHT);

#if 1
	for (int y = 0 ; y < VRAM_HEIGHT/2 ; y++)
		for (int x = 0 ; x < VRAM_WIDTH ; x++)
                    vram_set(vram, x, y, ((x ^ y) & 0x04)?0xFE:0);
#endif

  prussdrv_init();
  if (prussdrv_open(PRU_EVTOUT_0) == -1) {
    printf("prussdrv_open() failed\n");
    return 1;
  }

  tpruss_intc_initdata pruss_intc_initdata = PRUSS_INTC_INITDATA;
  prussdrv_pruintc_init(&pruss_intc_initdata);

  printf("Executing program and waiting for termination\n");
  if (argc == 3) {
    if (prussdrv_load_datafile(0 /* PRU0 */, argv[2]) < 0) {
      fprintf(stderr, "Error loading %s\n", argv[2]);
      exit(-1);
    }
  }
  if (prussdrv_exec_program(0 /* PRU0 */, argv[1]) < 0) {
    fprintf(stderr, "Error loading %s\n", argv[1]);
    exit(-1);
  }

  // Wait for the PRU to let us know it's done
  prussdrv_pru_wait_event(PRU_EVTOUT_0);
  printf("All done\n");

  prussdrv_pru_disable(0 /* PRU0 */);
  prussdrv_exit();

	return 0;
}
