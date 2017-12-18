#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Need extern "C" __declspec(dllexport) for DLL
extern "C" __declspec(dllexport) unsigned short Image_processing_add(unsigned char *in_a, unsigned char *in_b)
{
    unsigned short add_out = 0;
    //single value out.
    add_out = in_a[0] + in_a[1] + in_a[2] + in_b[0] + in_b[1] + in_b[2];
    return(add_out);
}

// Need extern "C" __declspec(dllexport) for DLL
extern "C" __declspec(dllexport) void Image_processing_pics(unsigned char *in_c, unsigned char *out, int width, int height)
{
    //pointer value out.
	for( int y = 0; y < height; y++ ){
		for( int x = 0; x < width; x++ )
			out[(y * width) + x] = in_c[(y * width) + x] + 1;
	}
	return;
}
