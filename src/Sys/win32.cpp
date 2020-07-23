#include "sys.h"
#include <stdio.h>
#include <stdlib.h>

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
    char* getTargetDir() {
        char path[MAX_PATH];
        GetCurrentDirectoryA(sizeof(path), path);
        return path;
    }
}