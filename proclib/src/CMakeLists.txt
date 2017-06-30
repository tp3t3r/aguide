set(libsource imgproc.h imgproc.cc ImageProcessor.h ImageProcessor.cc)
add_library(
    ${libproc} SHARED
    ${libsource}
)

add_library(
    prod-${libproc} SHARED
    ${libsource}
)

target_compile_definitions(prod-${libproc} PRIVATE PRODUCTION_BUILD=1)

install(TARGETS ${libproc} DESTINATION /tmp)
install(TARGETS prod-${libproc} DESTINATION /tmp)
