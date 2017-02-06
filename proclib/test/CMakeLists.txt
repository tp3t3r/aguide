set(t_exe test_imgproc)
add_executable(${t_exe}
    test_imgproc.cc
)
target_link_libraries(${t_exe} ${libproc})

add_test(test1 ${t_exe})
