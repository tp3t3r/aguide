#pragma once

//api functions
extern "C" {
    const char* get_lib_version(void);
    void init_image(unsigned width, unsigned height, const unsigned char* data);
    void destroy(void);
    void apply_threshold(unsigned char tval);
    int get_brightest_area(unsigned slice_size);
    unsigned char* get_image_buffer(void);
}

//internal
unsigned get_slice_index(unsigned pixel_index, unsigned slice_size);

