cmake_minimum_required(VERSION 3.7)
project(zbar)

if("${PROJECT_SOURCE_DIR}" STREQUAL "${PROJECT_BINARY_DIR}")
  message(FATAL_ERROR "In-source builds are not permitted. Make a separate \
folder for building:\nmkdir build; cd build; cmake ..\nBefore that, remove the \
files already created:\nrm -rf CMakeCache.txt CMakeFiles") 
endif("${PROJECT_SOURCE_DIR}" STREQUAL "${PROJECT_BINARY_DIR}")

set(ZBAR_VERSION_MAJOR 0) 
set(ZBAR_VERSION_MINOR 10)

set(ENABLE_CODE128 1)
set(ENABLE_CODE39 1)
set(ENABLE_EAN 1)
set(ENABLE_I25 1)
set(ENABLE_QRCODE 1)
set(ENABLE_PDF417 1)

#TODO: actually check for video support
set(HAVE_VIDEO 0)
set(HAVE_V4L1 0)
set(HAVE_V4L2 0)

#TODO: actually check for x11 support
set(HAVE_X 0)

#TODO: actually check for xv support
set(HAVE_XV 0)

set(INCLUDE_DIRS
  ${PROJECT_SOURCE_DIR}/include
  ${PROJECT_SOURCE_DIR}/zbar
  )

set(SOURCE_FILES
  ${PROJECT_SOURCE_DIR}/zbar/config.c
  ${PROJECT_SOURCE_DIR}/zbar/error.h
  ${PROJECT_SOURCE_DIR}/zbar/error.c
  ${PROJECT_SOURCE_DIR}/zbar/symbol.h
  ${PROJECT_SOURCE_DIR}/zbar/symbol.c
  ${PROJECT_SOURCE_DIR}/zbar/image.h
  ${PROJECT_SOURCE_DIR}/zbar/image.c
  ${PROJECT_SOURCE_DIR}/zbar/convert.c
  ${PROJECT_SOURCE_DIR}/zbar/processor.h
  ${PROJECT_SOURCE_DIR}/zbar/processor.c
  ${PROJECT_SOURCE_DIR}/zbar/processor/lock.c
  ${PROJECT_SOURCE_DIR}/zbar/refcnt.c
  ${PROJECT_SOURCE_DIR}/zbar/refcnt.h
  ${PROJECT_SOURCE_DIR}/zbar/timer.h
  ${PROJECT_SOURCE_DIR}/zbar/mutex.h
  ${PROJECT_SOURCE_DIR}/zbar/event.h
  ${PROJECT_SOURCE_DIR}/zbar/thread.h
  ${PROJECT_SOURCE_DIR}/zbar/window.h
  ${PROJECT_SOURCE_DIR}/zbar/window.c
  ${PROJECT_SOURCE_DIR}/zbar/video.h
  ${PROJECT_SOURCE_DIR}/zbar/video.c
  ${PROJECT_SOURCE_DIR}/zbar/img_scanner.c
  ${PROJECT_SOURCE_DIR}/zbar/scanner.c
  ${PROJECT_SOURCE_DIR}/zbar/decoder.h    
  ${PROJECT_SOURCE_DIR}/zbar/decoder.c
  )

set(EXTRA_SOURCES
  ${PROJECT_SOURCE_DIR}/zbar/svg.h
  ${PROJECT_SOURCE_DIR}/zbar/svg.c  
  )


if(ANDROID)
  message(STATUS "CMAKE_ANDROID_ARCH_ABI=${CMAKE_ANDROID_ARCH_ABI}")
  set(INCLUDE_DIRS
    ${INCLUDE_DIRS}
    ${PROJECT_SOURCE_DIR}/android/libjpeg/${CMAKE_ANDROID_ARCH_ABI}/install/include
    ${PROJECT_SOURCE_DIR}/android/libiconv/${CMAKE_ANDROID_ARCH_ABI}/install/include
    )
  set(SOURCE_FILES
    ${SOURCE_FILES}
    ${PROJECT_SOURCE_DIR}/android/libjpeg/${CMAKE_ANDROID_ARCH_ABI}/install/include/jconfig.h
    ${PROJECT_SOURCE_DIR}/android/libjpeg/${CMAKE_ANDROID_ARCH_ABI}/install/include/jerror.h
    ${PROJECT_SOURCE_DIR}/android/libjpeg/${CMAKE_ANDROID_ARCH_ABI}/install/include/jmorecfg.h
    ${PROJECT_SOURCE_DIR}/android/libjpeg/${CMAKE_ANDROID_ARCH_ABI}/install/include/jpeglib.h
    ${PROJECT_SOURCE_DIR}/android/libiconv/${CMAKE_ANDROID_ARCH_ABI}/install/include/iconv.h
    ${PROJECT_SOURCE_DIR}/android/libiconv/${CMAKE_ANDROID_ARCH_ABI}/install/include/libcharset.h
    ${PROJECT_SOURCE_DIR}/android/libiconv/${CMAKE_ANDROID_ARCH_ABI}/install/include/localcharset.h    
    )
  set(LIB_FILES_STATIC
    ${LIB_FILES_STATIC}
    ${PROJECT_SOURCE_DIR}/android/libjpeg/${CMAKE_ANDROID_ARCH_ABI}/install/lib/libjpeg.a
    ${PROJECT_SOURCE_DIR}/android/libiconv/${CMAKE_ANDROID_ARCH_ABI}/install/lib/libiconv.a
    ${PROJECT_SOURCE_DIR}/android/libiconv/${CMAKE_ANDROID_ARCH_ABI}/install/lib/libcharset.a
    )

endif()

include_directories(${INCLUDE_DIRS})

message(STATUS "Include directories:")
get_property(dirs DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR} PROPERTY INCLUDE_DIRECTORIES)
foreach(dir ${dirs})
  message(STATUS "dir='${dir}'")
endforeach()

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
CHECK_INCLUDE_FILE(iconv.h HAVE_ICONV)
CHECK_INCLUDE_FILE(jpeglib.h HAVE_JPEG)

configure_file(${PROJECT_SOURCE_DIR}/include/config.h.in ${PROJECT_SOURCE_DIR}/include/config.h)


message(STATUS "ENABLE_EAN=${ENABLE_EAN}")
if(${ENABLE_EAN})
  set(SOURCE_FILES
    ${SOURCE_FILES}
    ${PROJECT_SOURCE_DIR}/zbar/decoder/ean.h
    ${PROJECT_SOURCE_DIR}/zbar/decoder/ean.c
    )
endif()

message(STATUS "ENABLE_CODE128=${ENABLE_CODE128}")
if(${ENABLE_CODE128})
  set(SOURCE_FILES
    ${SOURCE_FILES}
    ${PROJECT_SOURCE_DIR}/zbar/decoder/code128.h
    ${PROJECT_SOURCE_DIR}/zbar/decoder/code128.c
    )
endif()

message(STATUS "ENABLE_CODE39=${ENABLE_CODE39}")
if(${ENABLE_CODE39})
  set(SOURCE_FILES
    ${SOURCE_FILES}
    ${PROJECT_SOURCE_DIR}/zbar/decoder/code39.h
    ${PROJECT_SOURCE_DIR}/zbar/decoder/code39.c
    )
endif()

message(STATUS "ENABLE_I25=${ENABLE_I25}")
if(${ENABLE_I25})
  set(SOURCE_FILES
    ${SOURCE_FILES}
    ${PROJECT_SOURCE_DIR}/zbar/decoder/i25.h
    ${PROJECT_SOURCE_DIR}/zbar/decoder/i25.c
    )
endif()

message(STATUS "ENABLE_PDF417=${ENABLE_PDF417}")
if(${ENABLE_PDF417})
  set(SOURCE_FILES
    ${SOURCE_FILES}
    ${PROJECT_SOURCE_DIR}/zbar/decoder/pdf417.h
    ${PROJECT_SOURCE_DIR}/zbar/decoder/pdf417.c
    ${PROJECT_SOURCE_DIR}/zbar/decoder/pdf417_hash.h
    )
endif()

message(STATUS "ENABLE_QRCODE=${ENABLE_QRCODE}")
if(${ENABLE_QRCODE})
  set(SOURCE_FILES
    ${SOURCE_FILES}
    ${PROJECT_SOURCE_DIR}/zbar/decoder/qr_finder.h
    ${PROJECT_SOURCE_DIR}/zbar/decoder/qr_finder.c
    ${PROJECT_SOURCE_DIR}/zbar/qrcode/qrdec.h
    ${PROJECT_SOURCE_DIR}/zbar/qrcode/qrdec.c
    ${PROJECT_SOURCE_DIR}/zbar/qrcode/qrdectxt.c
    ${PROJECT_SOURCE_DIR}/zbar/qrcode/rs.h
    ${PROJECT_SOURCE_DIR}/zbar/qrcode/rs.c
    ${PROJECT_SOURCE_DIR}/zbar/qrcode/isaac.h
    ${PROJECT_SOURCE_DIR}/zbar/qrcode/isaac.c
    ${PROJECT_SOURCE_DIR}/zbar/qrcode/bch15_5.h
    ${PROJECT_SOURCE_DIR}/zbar/qrcode/bch15_5.c
    ${PROJECT_SOURCE_DIR}/zbar/qrcode/binarize.h
    ${PROJECT_SOURCE_DIR}/zbar/qrcode/binarize.c
    ${PROJECT_SOURCE_DIR}/zbar/qrcode/util.h
    ${PROJECT_SOURCE_DIR}/zbar/qrcode/util.c
    )
endif()

if(${WIN32})
  message(STATUS "TODO: WIN32 NOT IMPLEMENTED IN CMAKE")
elseif()
  set(SOURCE_FILES
    ${SOURCE_FILES}
    ${PROJECT_SOURCE_DIR}/zbar/processor/posix.h
    ${PROJECT_SOURCE_DIR}/zbar/decoder/posix.c
    )
endif()

message(STATUS "HAVE_V4L1=${HAVE_V4L1}")
if(${HAVE_V4L1})
  set(SOURCE_FILES
    ${SOURCE_FILES}
    ${PROJECT_SOURCE_DIR}/zbar/video/v4l1.c
    )
  message(STATUS "HAVE_V4L2=${HAVE_V4L2}")
  if(${HAVE_V4L2})
    set(SOURCE_FILES
      ${SOURCE_FILES}
      ${PROJECT_SOURCE_DIR}/zbar/video/v4l2.c
      )
  endif()
endif()

message(STATUS "WIN32=${WIN32}")
if(${WIN32})
  if(${HAVE_VIDEO})
    message(STATUS "TODO: WIN32 HAVE_VIDEO NOT IMPLEMENTED IN CMAKE")
  endif()
endif()

message(STATUS "HAVE_VIDEO=${HAVE_VIDEO}")
if(NOT ${HAVE_VIDEO})
  set(SOURCE_FILES
    ${SOURCE_FILES}
    ${PROJECT_SOURCE_DIR}/zbar/video/null.c
    )
endif()

message(STATUS "HAVE_JPEG=${HAVE_JPEG}")
if(${HAVE_JPEG})
  set(SOURCE_FILES
    ${SOURCE_FILES}
    ${PROJECT_SOURCE_DIR}/zbar/jpeg.c
    )
endif()

message(STATUS "HAVE_X=${HAVE_X}")
if(${HAVE_X})
  set(SOURCE_FILES
    ${SOURCE_FILES}
    #${PROJECT_SOURCE_DIR}/zbar/jpeg.c
    #TODO
    )
  message(STATUS "HAVE_XV=${HAVE_XV}")
  if(${HAVE_XV})
    set(SOURCE_FILES
      ${SOURCE_FILES}
      #${PROJECT_SOURCE_DIR}/zbar/jpeg.c
      #TODO
      )
  endif()

elseif(${WIN32})
  message(STATUS "TODO: WIN32 WINDOW SYTEM NOT IMPLEMENTED IN CMAKE")
  
else()
  set(SOURCE_FILES
    ${SOURCE_FILES}
    ${PROJECT_SOURCE_DIR}/zbar/window/null.c
    )  
endif()

add_library(zbar SHARED ${SOURCE_FILES})

message(STATUS "Target link libraries:")
foreach(file ${LIB_FILES_STATIC})
  message(STATUS "file='${file}'")
endforeach()

target_link_libraries(zbar ${LIB_FILES_STATIC})


