# Minimum required CMake version
cmake_minimum_required(VERSION 3.10)

# Project name and version
project(DogToyExample VERSION 1.0)

# Specify the C++ standard
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED True)

# Add the executable target
add_executable(DogToyExample dog_toy.cpp)

