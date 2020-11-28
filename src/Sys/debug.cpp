#include "debug.h"
#include "../Sys/color.h" // colorText()
#include <stdio.h>
#include <string.h>

char* _bufferptr; // Formatting buffer
void print(DebugLevel dbg_lvl, str out, int code, str additinal_info) {
    // buffer(buffer size is length of str + ~len of Critacal error patern + additional info len)
    switch (dbg_lvl)
    {
    case DebugLevel::INFO: // Non color
        puts(out.c_str());
        return;

    case DebugLevel::WARING: // Yellow color
        sprintf(_bufferptr, "WARING : %s %s", out.c_str(), additinal_info.c_str()); // Formating string to buffer
        colorText(_bufferptr, Color::YELLOW); // print formated str from buffer
        return;

    case DebugLevel::ERROR: // Magenta 
        sprintf(_bufferptr, "ERROR %d: %s %s", code, out.c_str(), additinal_info.c_str());
        colorText(_bufferptr, Color::MAGENTA);
        return;

    case DebugLevel::CRITICAL_ERROR: // Red
        sprintf(_bufferptr, "CRITICAL ERROR %d: %s %s", code, out.c_str(), additinal_info.c_str());
        colorText(_bufferptr, Color::RED);
        return;
    }
}