cmake_minimum_required(VERSION 3.7)
project(zbar)

if("${PROJECT_SOURCE_DIR}" STREQUAL "${PROJECT_BINARY_DIR}")
  message(FATAL_ERROR "In-source builds are not permitted. Make a separate \
folder for building:\nmkdir build; cd build; cmake ..\nBefore that, remove the \
files already created:\nrm -rf CMakeCache.txt CMakeFiles") 
endif("${PROJECT_SOURCE_DIR}" STREQUAL "${PROJECT_BINARY_DIR}")

set(ENABLE_CODE128 1)
set(ENABLE_CODE39 1)
set(ENABLE_EAN 1)
set(ENABLE_I25 1)
set(ENABLE_QRCODE 1)


set(ZBAR_VERSION_MAJOR 0) 
set(ZBAR_VERSION_MINOR 10)

message(STATUS "Checking include files.")
include(CheckIncludeFile)
include(CheckIncludeFiles)

CHECK_INCLUDE_FILE(sys/types.h HAVE_SYS_TYPES_H)
CHECK_INCLUDE_FILE(sys/stat.h HAVE_SYS_STAT_H)
CHECK_INCLUDE_FILES(stdlib.h stddef.h HAVE_STDC_HEADERS)
CHECK_INCLUDE_FILE(stdlib.h HAVE_STDLIB_H)
CHECK_INCLUDE_FILE(string.h HAVE_STRING_H)
CHECK_INCLUDE_FILE(strings.h HAVE_STRINGS_H)
CHECK_INCLUDE_FILE(inttypes.h HAVE_INTTYPES_H)
CHECK_INCLUDE_FILE(stdint.h HAVE_STDINT_H)
CHECK_INCLUDE_FILE(unistd.h HAVE_UNISTD_H)

configure_file(${PROJECT_SOURCE_DIR}/include/config.h.in ${PROJECT_SOURCE_DIR}/include/config.h)

set(SOURCE_FILES
    ${PROJECT_SOURCE_DIR}/zbar/config.c
    ${PROJECT_SOURCE_DIR}/zbar/error.h
    ${PROJECT_SOURCE_DIR}/zbar/error.c
    ${PROJECT_SOURCE_DIR}/zbar/symbol.h
    ${PROJECT_SOURCE_DIR}/zbar/symbol.c
    ${PROJECT_SOURCE_DIR}/zbar/image.h
    ${PROJECT_SOURCE_DIR}/zbar/image.c
    ${PROJECT_SOURCE_DIR}/zbar/convert.c
    ${PROJECT_SOURCE_DIR}/zbar/refcnt.c
    ${PROJECT_SOURCE_DIR}/zbar/refcnt.h
    ${PROJECT_SOURCE_DIR}/zbar/mutex.h
    ${PROJECT_SOURCE_DIR}/zbar/thread.h
    ${PROJECT_SOURCE_DIR}/zbar/video.h
    ${PROJECT_SOURCE_DIR}/zbar/video.c
    # zbar/event.h
    # zbar/img_scanner.c
    # zbar/img_scanner.h
    # zbar/jpeg.c
    # zbar/libzbar.rc
    # zbar/processor.c
    # zbar/processor.h
    # zbar/qrcode
    # zbar/qrcode.h
    # zbar/scanner.c
    # zbar/svg.c
    # zbar/svg.h
    # zbar/debug.h
    # zbar/decoder.c
    # zbar/decoder.h    
    # zbar/timer.h
    # zbar/window.c
    # zbar/window.h
)


include_directories(./include ./zbar)

add_library(zbar SHARED ${SOURCE_FILES})



