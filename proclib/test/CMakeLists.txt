include_directories(${CMAKE_SOURCE_DIR}/src)
link_directories(${CMAKE_CURRENT_BINARY_DIR})

file(GLOB testcases_src
    "test_*.cc"
)

foreach(testcase ${testcases_src})
    #compile
    get_filename_component(test_binary ${testcase} NAME)
    add_executable(${test_binary}
        ${testcase}
        img_sample.h
    )
    #link with production code
    target_link_libraries(${test_binary} ${libproc})
    #add to test set
    add_test(${test_binary} ${test_binary})
endforeach(testcase)


