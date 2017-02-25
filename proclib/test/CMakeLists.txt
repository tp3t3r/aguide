
include_directories(${CMAKE_SOURCE_DIR}/src)
link_directories(${CMAKE_CURRENT_BINARY_DIR})

set(test1 thresholding)
add_executable(${test1}
    test_thresholding.cc
)
target_link_libraries(${test1} ${libproc})
add_test("Image-thresholding" ${test1})

set(test2 indexing)
add_executable(${test2}
    test_slice_indexing.cc
    img_sample.h
)
target_link_libraries(${test2} ${libproc})
add_test("Slice-indexing" ${test2})

set(test3 brightest)
add_executable(${test3}
    test_brightestarea.cc
    img_sample.h
)
target_link_libraries(${test3} ${libproc})
add_test("Select-brightest-area" ${test3})


