cmake_minimum_required(VERSION 3.6)
project(zbar)

configure_file(include/config.h.in include/config.h)

set(SOURCE_FILES
    zbar/config.c
    zbar/convert.c
    zbar/debug.h
    zbar/decoder
    zbar/decoder.c
    zbar/decoder.h
    zbar/error.c
    zbar/error.h
    zbar/event.h
    zbar/image.c
    zbar/image.h
    zbar/img_scanner.c
    zbar/img_scanner.h
    zbar/jpeg.c
    zbar/libzbar.rc
    zbar/Makefile.am.inc
    zbar/mutex.h
    zbar/processor
    zbar/processor.c
    zbar/processor.h
    zbar/qrcode
    zbar/qrcode.h
    zbar/refcnt.c
    zbar/refcnt.h
    zbar/scanner.c
    zbar/svg.c
    zbar/svg.h
    zbar/symbol.c
    zbar/symbol.h
    zbar/thread.h
    zbar/timer.h
    zbar/video
    zbar/video.c
    zbar/video.h
    zbar/window
    zbar/window.c
    zbar/window.h
)


include_directories(./include ./zbar)

add_library(zbar SHARED ${SOURCE_FILES})



