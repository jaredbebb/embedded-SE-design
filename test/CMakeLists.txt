# CMakeList.txt : CMake project for amazon-embedded-SE-interview-prep, include source and define
# project specific logic here.
#
cmake_minimum_required (VERSION 3.8)

set(BINARY ${CMAKE_PROJECT_NAME}_test)

file(GLOB_RECURSE TEST_SOURCES LIST_DIRECTORIES false *.h *.cpp)

set(SOURCES ${TEST_SOURCES})

add_executable(${BINARY} ${TEST_SOURCES})

add_test(NAME ${BINARY} COMMAND ${BINARY})

# target_link_libraries(${BINARY} PUBLIC ${CMAKE_PROJECT_NAME}_lib gtest)

#message(FATAL_ERROR var="${target}")
set(target algs_structs)
# message(FATAL_ERROR "target = ${target}")
target_link_libraries(${BINARY} PUBLIC ${target} gtest)

# add the binary tree to the search path for include files
target_include_directories(${BINARY} PUBLIC
                          "${PROJECT_BINARY_DIR}"
                          "${PROJECT_SOURCE_DIR}/algs_structs"
                          )


# add_executable(algs_structs_GTEST "ut_Util.cpp")

#target_link_libraries(algs_structs_GTEST PUBLIC ${lib})

# message(FATAL_ERROR var="${lib}")








# enable_testing()
# find_package(GTest REQUIRED)

# include(GoogleTest)

# add_executable(algs_structs_GTEST ut_Util.cpp)

# gtest_discover_tests(algs_structs_GTEST)