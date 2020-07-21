#include "debug.h"
#include "../Sys/color.h"
#include <stdio.h>
using namespace NomakeSys;
namespace NomakeApi {
    void debug(DebugLevel dbg_level, char* str, int code = 0) {
        char buffer[sizeof(str) + 25];
        switch (dbg_level)
        {
        case DebugLevel::INFO:
            puts(str);
            return;
        case DebugLevel::WARING:
            sprintf(buffer, "WARING : %s", str);
            colorText(buffer, Color::YELLOW);
            return;
        case DebugLevel::ERROR:
            sprintf(buffer, "ERROR %d: %s", code, str);
            colorText(buffer, Color::MAGENTA);
            return;
        case DebugLevel::CRITICAL_ERROR:
            sprintf(buffer, "CRITICAL ERROR %d: %s", code, str);
            colorText(buffer, Color::RED);
            return;
        }
    }
}