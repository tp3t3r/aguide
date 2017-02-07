set(t_exe test_imgproc)
include_directories(${CMAKE_SOURCE_DIR}/src)
link_directories(${CMAKE_CURRENT_BINARY_DIR})

add_executable(${t_exe}
    test_imgproc.cc
)
target_link_libraries(${t_exe} ${libproc})

add_test(test1 ${t_exe})
