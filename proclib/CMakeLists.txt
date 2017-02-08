project(Proclib)

cmake_minimum_required(VERSION 3.6)
set(CMAKE_CXX_FLAGS "-std=c++11 -Wall -O3" )
enable_testing()

#output binary
set(libproc "imgproc")

add_subdirectory(src)
add_subdirectory(test)
