# Minimum required CMake version
cmake_minimum_required(VERSION 3.10)

# Project name and version
project(DogToyExample VERSION 1.0)

# Specify the C++ standard
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED True)

# Define directories for include and source files
set(SRC_DIR ${CMAKE_SOURCE_DIR}/src)
set(INCLUDE_DIR ${CMAKE_SOURCE_DIR}/include)
set(TEST_DIR ${CMAKE_SOURCE_DIR}/test)

# Include directories for headers
include_directories(${INCLUDE_DIR})

# Add the executable target for your main application
add_executable(DogToyExample ${SRC_DIR}/main.cpp ${SRC_DIR}/dog.cpp ${SRC_DIR}/toy.cpp)

find_package(GTest REQUIRED)

# Enable testing
enable_testing()

# Add the test executable
add_executable(DogToyTest ${TEST_DIR}/test_dog.cpp ${SRC_DIR}/dog.cpp ${SRC_DIR}/toy.cpp)

target_link_libraries(DogToyTest PRIVATE GTest::gmock_main)
