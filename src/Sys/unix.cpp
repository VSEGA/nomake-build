#include "sys.h"

#include <stdio.h> // For use printf
#include <unistd.h> // For use getcwd
#include <limits.h> // For use PATH_MAX

namespace NomakeSys {
    typedef NomakeApi::Color clrs;
    SysType getSystem() { return SysType::unix; }
    WinVers getOSver() { return WinVers::unkown; }
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
        return NomakeApi::unkown;
    }
    void printColorText(char* s, clrs fg, clrs bg) {
        printf("\033[3;%d;%dm%s\033[0m", getRealColor(bg) + 10, getRealColor(fg), s); // bg color = fg color + 10
    }
    char* getWorkingDir() {
        char cwd[PATH_MAX + 1]; // buffer with end char
        getcwd(cwd, sizeof(cwd));
        return cwd;
    }
}