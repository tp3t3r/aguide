#pragma once

extern "C" {
    const char* get_lib_version(void);
    char* apply_threshold(const char* img, unsigned width, unsigned height, unsigned char tval);
}

