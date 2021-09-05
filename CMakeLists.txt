# CMakeList.txt : Top-level CMake project file, do global configuration
# and include sub-projects here.
#
cmake_minimum_required (VERSION 3.8)

project ("embedded")

# Include sub-projects.
add_subdirectory ("source")
add_subdirectory("lib")
add_subdirectory ("test")


