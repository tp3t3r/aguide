#pragma once

extern "C" {
    const char* get_lib_version(void);
    void init_image(unsigned width, unsigned height, const unsigned char* data);
    void apply_threshold(unsigned char tval);
    unsigned char* get_image_buffer(void);
}

