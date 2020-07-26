/*
    Non systemless functions.
*/

#pragma once
#include "../Api/types.h" // Unkown, ErrorsCodes, Color

namespace NomakeSys {
    /*
        OS Types
    */
    enum class SysType {
        nt,
        unix
    };
    /*
        Windows Versions
    */
    enum class WinVers {
        xp,
        vista,
        seven,
        eight,
        eight_point_one,
        unkown
    };
    /*
        Return OS Type
    */
    SysType getSystem();
    /*
        Return Windows Version(if win10 return 8.1), if os type is unix or winver not xp - 10 return unkown
    */
    WinVers getOSver();
    /* 
        Return Working Dir
    */
    char* getWorkingDir();
    /* 
        DON'T USE THIS, USE colorText FROM color.h!

        Print Color Text
    */
    void printColorText(char* text, NomakeApi::Color bg, NomakeApi::Color fg);
}