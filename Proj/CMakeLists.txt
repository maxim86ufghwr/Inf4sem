cmake_minimum_required(VERSION 3.16)

project(cmake_project)

set(LIBRARY matrix.cpp vector.cpp volume.cpp)

add_executable(${PROJECT_NAME} main.cpp)

add_library(matrix matrix.cpp vector.cpp volume.cpp)

target_link_libraries(${PROJECT_NAME} matrix)