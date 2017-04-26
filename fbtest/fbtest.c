#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <fcntl.h>
#include <linux/fb.h>
#include <sys/mman.h>

int line_len, pix_len;

inline size_t offset(int x, int y) {
    return (y*line_len) + (x*pix_len);
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
    long bufsz = fix_info.smem_len;
    line_len = fix_info.line_length;
    pix_len = 2;
    char* buffer = (char*)mmap(0, bufsz,
            PROT_READ | PROT_WRITE, MAP_SHARED,
            fb_fd, 0);
    if ((int)buffer == -1) {
        printf("Error mapping framebuffer.\n");
    } else {
        int j;
        int w = var_info.xres;
        int h = var_info.yres;
        memset(buffer, 0x0, bufsz);
        for (j = 0; j < 240; j++) {
            buffer[offset(j,j)] = 0xff;
            buffer[offset(j,(h-1)-j)] = 0xff;
            buffer[offset((w-2)-j,(h-1)-j)] = 0xff;
            buffer[offset((w-2)-j,j)] = 0xff;
        }
    }
    munmap(buffer, bufsz);
    close(fb_fd);

    return 0;
}
