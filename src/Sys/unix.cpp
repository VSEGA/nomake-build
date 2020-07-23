#include "sys.h"

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <limits.h>

namespace NomakeSys {
    typedef NomakeApi::ErrorsCodes errors;
    typedef NomakeApi::Color clrs;
    short getSystem() { return unix; }
    short getOSver() { return unkown; }

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
        return NomakeApi::unkown;
    }
    void printColorText(char* s, clrs fg, clrs bg) {
        printf("\033[3;%d;%dm%s\033[0m", getRealColor(bg) + 10, getRealColor(fg), s);
    }
    char* getTargetDir() {
        char cwd[PATH_MAX + 1];
        getcwd(cwd, sizeof(cwd));
        return cwd;
    }
}