#pragma once

namespace NomakeApi {
    enum class Color {
        RED,
        GREEN,
        WHITE,
        YELLOW,
        LIGHT_BLUE,
        BLUE,
        GRAY,
        BLACK,
        MAGENTA
    };
    short unkown = 1;
} 

namespace NomakeSys {
    enum class SysType {
        nt,
        unix
    };
    enum class WinVers {
        xp,
        vista,
        seven,
        eight,
        eight_point_one,
        unkown
    };
    SysType getSystem();
    WinVers getOSver(); // Only for Windows, if os type is unix return unkown
    char* getTargetDir();
    void printColorText(char* text, NomakeApi::Color bg, NomakeApi::Color fg);
}