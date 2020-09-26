/*
    Delete single and multi line comments from file(part of preprocessor)
*/

#pragma once
#include "../../Api/types.h" // SettingsBuffer

namespace NomakeTools {
    /*
        Delete comments
        
    */
    char comments(char s[2], NomakeApi::SettingsBuffer *options);
}