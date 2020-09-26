#include "debug.h"
#include "../Sys/color.h" // colorText()
#include <iostream> // puts()

void debug(DebugLevel dbg_level, const char str[], const int code, const char additinal_info[]) {
    // buffer(buffer size is length of str + ~len of Critacal error patern + additional info len)
    char *buffer; 

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