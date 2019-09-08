cmake_minimum_required(VERSION 3.6)
project(zbar)

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



