#include "sys.h"
#include <stdio.h> // printf() and puts()
#include <stdlib.h> // exit()

#define WIN32_LEAN_AND_MEAN
#include <Windows.h> // WinApi
#include "../Api/types.h" // NomakeApi::Color and NomakeApi::ErrorsCodes

namespace NomakeSys {
    typedef short colorWin32;
    typedef NomakeApi::Color clrs;

    /*
        Return Win32Api color code
    */
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
        return 0x0007;
    }
    void printColorText(const char text[], clrs bg, clrs fg) {
        HANDLE console_handle;
        CONSOLE_SCREEN_BUFFER_INFO buffer;
        WORD currentConsoleAttr;

        console_handle = GetStdHandle(STD_OUTPUT_HANDLE);
        if(GetConsoleScreenBufferInfo(console_handle, &buffer)) {
            currentConsoleAttr = buffer.wAttributes; // Current color
        }
        else {
            printf("Error %d: Error get ConsoleScreenBuffer", (int) NomakeApi::ErrorsCodes::Win32GetConsoleScreenBuffer);
            exit((int) NomakeApi::ErrorsCodes::Win32GetConsoleScreenBuffer);
        }
        SetConsoleTextAttribute(console_handle, getRealColor(fg) * 16 + getRealColor(bg)); // Set color
        puts(text); // print text
        SetConsoleTextAttribute(console_handle, currentConsoleAttr); // Return base color
    }
    char* getWorkingDir() {
        char *path; // buffer
        GetCurrentDirectoryA(sizeof(path), path);
        return path;
    }
}