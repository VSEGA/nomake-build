/*
    Non systemless functions
*/

#pragma once
#include "../Api/types.h" // ErrorsCodes, Color

/* 
    Return Working Dir
*/
char* getWorkingDir();
/* 
    DON'T USE THIS, USE colorText FROM color.h!

    Print Color Text
*/
void printColorText(const char text[], Color fg, Color bg);
