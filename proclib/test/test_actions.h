#pragma once

#include <stdarg.h>
#include <stdio.h>

void TEST_RESULT(const char *fmt, ...) {
    va_list args;
    va_start(args, fmt);
    vprintf(fmt, args);
    va_end(args);
}
