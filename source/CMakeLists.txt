# CMakeList.txt : CMake project for amazon-embedded-SE-interview-prep, include source and define
# project specific logic here.
#
cmake_minimum_required (VERSION 3.8)

# add source and header files
add_subdirectory ("algs_structs")

# Add source to this project's executable.
add_executable (main "main.cpp" "main.h")

# TODO: Add tests and install targets if needed.

target_link_libraries(main PUBLIC algs_structs)

# add the binary tree to the search path for include files
# so that we will find TutorialConfig.h
target_include_directories(main PUBLIC
                          "${PROJECT_BINARY_DIR}"
                          "${PROJECT_SOURCE_DIR}/algs_structs"
                          )