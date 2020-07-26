#include "debug.h"
#include "../Sys/color.h" // To use NomakeSys::colorText()
#include <stdio.h> // To use puts

namespace NomakeApi {
    void debug(DebugLevel dbg_level, char* str, int code = 0, char* additinal_info = "") {
        // buffer(buffer size is length of str + ~len of Critacal error patern + additional info len)
        char buffer[sizeof(str) / sizeof(char) + 30 + sizeof(additinal_info) / sizeof(char)]; 

        switch (dbg_level)
        {
        case DebugLevel::INFO: // Non color
            puts(str);
            return;

        case DebugLevel::WARING: // Yellow color
            sprintf(buffer, "WARING : %s %s", str, additinal_info); // Formating string to buffer
            NomakeSys::colorText(buffer, Color::YELLOW); // print formated str from buffer
            return;

        case DebugLevel::ERROR: // Magenta 
            sprintf(buffer, "ERROR %d: %s %s", code, str, additinal_info); 
            NomakeSys::colorText(buffer, Color::MAGENTA);
            return;

        case DebugLevel::CRITICAL_ERROR: // Red
            sprintf(buffer, "CRITICAL ERROR %d: %s %s", code, str, additinal_info);
            NomakeSys::colorText(buffer, Color::RED);
            return;
        }
    }
}