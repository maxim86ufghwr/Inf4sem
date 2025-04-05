cmake_minimum_required(VERSION 3.10)

project(myProject)


set(SOURCE
    src/main.cpp
    src/Parser.cpp
    src/Field.cpp
    src/Cloud.cpp
    src/Cow.cpp
    src/ASCIIPicture.cpp
)

add_executable(myProject ${SOURCE})