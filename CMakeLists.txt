cmake_minimum_required(VERSION 3.6)
project(zbar)


set(ENABLE_CODE128 1)
set(ENABLE_CODE39 1)
set(ENABLE_EAN 1)
set(ENABLE_I25 1)
set(ENABLE_QRCODE 1)

# cmake's configure_file doesn't set 0 properly.
# Using #cmakedefine01 in config.h.in as a hack.
#set(ZBAR_VERSION_MAJOR 0) 

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







set(HAVE_STDINT_H 1)

configure_file(include/config.h.in include/config.h)



set(SOURCE_FILES
    zbar/config.c    

    zbar/error.h
    zbar/error.c
    zbar/symbol.h
    zbar/symbol.c
    zbar/image.h
    zbar/image.c
    zbar/convert.c
    zbar/refcnt.c
    zbar/refcnt.h
    zbar/mutex.h
    zbar/thread.h
    zbar/video.h
    zbar/video.c
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



