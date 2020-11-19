/*
    Delete single and multi line comments from file(part of preprocessor)
*/

#pragma once
#include "../../Api/types.h" // SettingsBuffer

/*
    Delete comments
        
*/
char comments(char s[2], SettingsBuffer *options);