# CMakeList.txt : CMake project for amazon-embedded-SE-interview-prep, include source and define
# project specific logic here.
#
cmake_minimum_required (VERSION 3.8)

set(BINARY ${CMAKE_PROJECT_NAME}_test)


set( SOURCES
	ut_Util.cpp
	main.cpp
)


# message(FATAL_ERROR "SOURCES = ${SOURCES}")

add_executable(${BINARY} ${SOURCES})

add_test(NAME ${BINARY} COMMAND ${BINARY})

target_link_libraries(${BINARY} PUBLIC ${CMAKE_PROJECT_NAME}_lib gtest)


