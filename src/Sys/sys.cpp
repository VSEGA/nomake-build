#include "sys.h"
#include <stdio.h>
#include <stdlib.h>


#if !defined(__unix__) || (defined(_WIN64) || defined(_WIN32))
#define WIN32_LEAN_AND_MEAN
#include <VersionHelpers.h>
#include <Windows.h>
#include "../Api/error.h"

namespace NomakeSys {
    typedef short colorWin32;
    typedef NomakeApi::ErrorsCodes errors;
    typedef NomakeApi::Color clrs;

    SysType getSystem() { return SysType::nt; }

    WinVers getOSver() {
        if (IsWindows8Point1OrGreater())
        {
            return WinVers::eight_point_one;
        }
        if (IsWindows8OrGreater())
        {
            return WinVers::eight;
        }
        if (IsWindows7OrGreater())
        {
            return WinVers::seven;
        }
        if (IsWindowsVistaOrGreater())
        {
            return WinVers::vista;
        }
        if (IsWindowsXPOrGreater())
        {
            return WinVers::xp;
        }
        return WinVers::unkown;
    }

    inline colorWin32 getRealColor(clrs color) {
        switch (color)
        {
            case clrs::BLACK:
                return 0x0000;
            case clrs::BLUE:
                return 0x0001;
            case clrs::GREEN:
                return 0x0002;
            case clrs::LIGHT_BLUE:
                return 0x0003;
            case clrs::RED:
                return 0x0004;
            case clrs::MAGENTA:
                return 0x0005;
            case clrs::YELLOW:
                return 0x0006;
            case clrs::WHITE:
                return 0x0007;
            case clrs::GRAY:
                return 0x0008;
        }
        return NomakeApi::unkown;
    }
    void printColorText(char* s, clrs fg, clrs bg) {
        HANDLE console_handle;
        CONSOLE_SCREEN_BUFFER_INFO buffer;
        WORD currentConsoleAttr;

        console_handle = GetStdHandle(STD_OUTPUT_HANDLE);
        if(GetConsoleScreenBufferInfo(console_handle, &buffer)) {
            currentConsoleAttr = buffer.wAttributes;
        }
        else {
            printf("Error %d: Error get ConsoleScreenBuffer", (int) errors::Win32GetConsoleScreenBuffer);
            exit((int) errors::Win32GetConsoleScreenBuffer);
        }
        SetConsoleTextAttribute(console_handle, getRealColor(bg) * 16 + getRealColor(fg));
        puts(s);
        SetConsoleTextAttribute(console_handle, currentConsoleAttr);
    }
}

#else
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
}

#endif