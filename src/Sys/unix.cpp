#include "sys.h"

#include <stdio.h> // For use printf
#include <unistd.h> // For use getcwd
#include <limits.h> // For use PATH_MAX

typedef Color clrs;

/*
    Return Foreground acsii color code

    background color = foreground + 10
*/
inline short getRealColor(clrs color) {
    switch (color)
    {
        case clrs::BLACK:
            return 30;
        case clrs::BLUE:
            return 34;
        case clrs::GREEN:
            return 32;
        case clrs::LIGHT_BLUE:
            return 94;
        case clrs::RED:
            return 31;
        case clrs::MAGENTA:
            return 35;
        case clrs::YELLOW:
            return 33;
        case clrs::WHITE:
            return 37;
        case clrs::GRAY:
            return 90;
    }
    return 37;
}
void printColorText(const char text[], clrs bg, clrs fg) {
    printf("\033[3;%d;%dm%s\033[0m", getRealColor(bg) + 10, getRealColor(fg), text); // bg color = fg color + 10
}

char* getWorkingDir() {
    char cwd[PATH_MAX + 1]; // buffer with end char
    getcwd(cwd, sizeof(cwd));
    return cwd;
}
