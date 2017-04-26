#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <fcntl.h>
#include <linux/fb.h>
#include <sys/mman.h>

int main(int argc, char* argv[]) {
    int fb_fd = 0;
    struct fb_var_screeninfo var_info;
    const char* FB_PATH = "/dev/fb0";
    fb_fd = open(FB_PATH, O_RDWR);
    if (fb_fd == -1) {
        printf("Error opening framebuffer %s.\n", FB_PATH);
        return 1;
    }
    printf("Framebuffer %s open.", FB_PATH);
    // Get screen info
    if (ioctl(fb_fd, FBIOGET_VSCREENINFO, &var_info)) {
        printf("Error reading framebuffer info.\n");
       return 1;
    }
    printf("FB display info: %dx%d, %d bpp\n",
           var_info.xres, var_info.yres, var_info.bits_per_pixel);
    close(fb_fd);
    return 0;
}
