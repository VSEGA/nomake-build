/*
    Systemed functions
*/

#pragma once
#include "../Api/types.h" // ErrorsCodes, Color
typedef Color clrs;
/* 
    Return Working Dir
*/
char* getWorkingDir();
/* 
    DON'T USE THIS, USE debug FROM Api/debug.h/cpp!

    Print Force Color Text
*/
void printColorText(const char text[], clrs bg, clrs fg);
