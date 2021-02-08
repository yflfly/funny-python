#if 1
#define DLL_API __declspec(dllexport)
#else
#define DLL_API __declspec(dllimport)
#endif

#include <stdio.h>
#include <stdlib.h>

// Point 结构体
struct Point
{
    float x, y;
};

static Point* position = NULL;

extern "C" {

    DLL_API int add(int a, int b)
    {
        return a + b;
    }

    DLL_API float addf(float a, float b)
    {
        return a + b;
    }

    DLL_API void print_point(Point* p)
    {
        if (p)
            printf("position x %f y %f", p->x, p->y);
    }
}