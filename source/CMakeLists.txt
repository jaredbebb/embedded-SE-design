# CMakeList.txt : CMake project for amazon-embedded-SE-interview-prep, include source and define
# project specific logic here.
#
cmake_minimum_required (VERSION 3.8)

set(BINARY ${CMAKE_PROJECT_NAME})
# set (target algs_structs )

set( HEADERS
	Element.h
	IntElement.h
	LinkedList.h
	Util.h
)

set( SOURCES
	Element.cpp
	LinkedList.cpp
	IntElement.cpp
)

# add source and header files
# add_subdirectory ("algs_structs")

add_executable(${BINARY}_run ${SOURCES})
add_library(${BINARY}_lib STATIC  ${SOURCES} ${HEADERS})

#set(algs_structs algs_structs )

# Add source to this project's executable.
set(executable main )
add_executable (${executable} "main.cpp" "main.h")

# TODO: Add tests and install targets if needed.

target_link_libraries(${executable} PUBLIC ${BINARY}_lib)

# add the binary tree to the search path for include files
# so that we will find TutorialConfig.h
target_include_directories(${executable} PUBLIC
                          "${PROJECT_BINARY_DIR}"
                          "${PROJECT_SOURCE_DIR}"
                          )