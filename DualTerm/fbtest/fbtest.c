#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <fcntl.h>
#include <linux/fb.h>
#include <sys/mman.h>

int line_len, pix_len;
int xres, yres;
char* buffer;

static inline size_t offset(int x, int y) {
    return (y*line_len) + (x*pix_len);
}

static inline void set_pixel(int x, int y, int val) {
    size_t off = offset(x,y);
    buffer[off] = (val >> 8) & 0xff;
    buffer[off+1] = val & 0xff;
}

void draw_reticule() {
    int i,j;
    for (i = 0; i < xres-1; i++) {
        set_pixel(i,0,0xffff);
        set_pixel(i,yres-1, 0xffff);
        set_pixel(i,yres/2, 0xffff);
    }
    for (j = 0; j < yres; j++) {
        set_pixel(0,j,0xffff);
        set_pixel(xres-2,j, 0xffff);
        set_pixel((xres-1)/2,j, 0xffff);
    }
}

void draw_blocks() {
    int x, y, x1, y1, i;
    int xoff = (xres-160)/2;
    int yoff = (yres-160)/2;
    for (i = 0; i < 16; i++) {
        x1 = xoff + (i & 0x3)*40;
        y1 = yoff + (i >> 2)*40;
        for (x = x1; x < x1+40; x++) {
            for (y = y1; y < y1+40; y++) {
                set_pixel(x,y,i << 8);
            }
        }
    }
}

int main(int argc, char* argv[]) {
    int fb_fd = 0;
    struct fb_var_screeninfo var_info;
    struct fb_fix_screeninfo fix_info;
    const char* FB_PATH = "/dev/fb0";
    fb_fd = open(FB_PATH, O_RDWR);
    if (fb_fd == -1) {
        printf("Error opening framebuffer %s.\n", FB_PATH);
        return 1;
    }
    printf("Framebuffer %s open.\n", FB_PATH);
    // Get screen info
    if (ioctl(fb_fd, FBIOGET_FSCREENINFO, &fix_info)) {
        printf("Error reading fixed framebuffer info.\n");
       return 1;
    }
    if (ioctl(fb_fd, FBIOGET_VSCREENINFO, &var_info)) {
        printf("Error reading variable framebuffer info.\n");
       return 1;
    }
    printf("FB display info: %dx%d, %d bpp\n",
           var_info.xres, var_info.yres, var_info.bits_per_pixel);
    xres = var_info.xres;
    yres = var_info.yres;
    long bufsz = fix_info.smem_len;
    line_len = fix_info.line_length;
    pix_len = 2;
    buffer = (char*)mmap(0, bufsz,
            PROT_READ | PROT_WRITE, MAP_SHARED,
            fb_fd, 0);
    if ((int)buffer == -1) {
        printf("Error mapping framebuffer.\n");
    } else {
        int j;
        int w = var_info.xres;
        int h = var_info.yres;
        memset(buffer, 0x0, bufsz);
        draw_reticule();
        draw_blocks();
        printf("Drawn.\n");
    }
    munmap(buffer, bufsz);
    close(fb_fd);

    return 0;
}
