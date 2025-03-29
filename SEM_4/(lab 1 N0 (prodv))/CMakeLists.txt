cmake_minimum_required(VERSION 3.10)

project(mytest)

add_subdirectory(src)

add_executable(test_one tests/test1.cpp)

add_executable(test_two tests/test2.cpp)

add_executable(test_three tests/test3.cpp)

