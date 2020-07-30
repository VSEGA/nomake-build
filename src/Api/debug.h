/*
    Use this file for print info to user
*/

#pragma once

namespace NomakeApi {
    /*
        These debugLevels differ in color and label
    */
    enum class DebugLevel{
        INFO,
        WARING,
        ERROR,
        CRITICAL_ERROR
    };

    /*
        Use this function to print text(And standart getchar/gets/scanf to get symbols)
    */
    void debug(DebugLevel dbg_lvl, const char str[], int code = 0, const char additinal_info[] = "");
}