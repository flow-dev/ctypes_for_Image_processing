# -*- coding: utf-8 -*-
#!/usr/bin/python

import ctypes
import numpy as np

# Windows OS
# Download <https://sourceforge.net/projects/mingw-w64/files/Toolchains%20targetting%20Win64/Personal%20Builds/rubenvb/gcc-4.8-release/>
# "x86_64-w64-mingw32-gcc-4.8.0-win64_rubenvb.7z"
# Build Dll for Windows 64bit System.
# Reference <https://kakurasan.blogspot.jp/2015/07/debianubuntu-mingw-crosscompile.html>
# Command
# >>> x86_64-w64-mingw32-g++ -c Image_processing.cpp
# >>> x86_64-w64-mingw32-g++ -shared -o Image_processing.dll Image_processing.o

PATH = 'Image_processing.dll'
lib = ctypes.windll.LoadLibrary(PATH)

# Linux OS
# Build .so for linux System.
# Command
# >>> g++ -g -Wall -fPIC -o Image_processing.o -c Image_processing.cpp
# >>> g++ -shared Image_processing.o -o Image_processing.so

#PATH = 'Image_processing.so'
#lib = ctypes.cdll.LoadLibrary(PATH)

# test define
input_a = np.array([10,20,30])
input_b = np.array([40,50,60])
input_c = np.array([10,20,30,40,50,60,70,80,90])
output = np.array([0,0,0,0,0,0,0,0,0])
width = 3
height = 3

# force change type for c++ func
input_a = input_a.astype(np.uint8)
input_b = input_b.astype(np.uint8)
input_c = input_c.astype(np.uint8)
output = output.astype(np.uint8)

print (input_a, input_b, input_c, output)

# numpy array to pointer
input_a = input_a.ctypes.data_as(ctypes.POINTER(ctypes.c_ubyte))
input_b = input_b.ctypes.data_as(ctypes.POINTER(ctypes.c_ubyte))
input_c = input_c.ctypes.data_as(ctypes.POINTER(ctypes.c_ubyte))
output = output.ctypes.data_as(ctypes.POINTER(ctypes.c_ubyte))

print (input_a, input_b, input_c, output)

# Call C++ Func from DLL
add_out = lib.Image_processing_add(input_a, input_b)
lib.Image_processing_pics(input_c, output, width, height)

# Result C++ Func from DLL
print (add_out)

output_arr = np.array([])
for i in xrange(width*height):
    #print output[i]
    output_arr = np.append(output_arr, output[i])
output_arr = output_arr.astype(np.uint8)

print (output_arr)

