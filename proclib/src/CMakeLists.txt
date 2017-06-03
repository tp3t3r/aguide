add_library(
    ${libproc} SHARED
    imgproc.h
    imgproc.cc
    ImageProcessor.h
    ImageProcessor.cc
)

install(TARGETS ${libproc} DESTINATION /tmp)
