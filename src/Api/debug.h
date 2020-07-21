#pragma once

namespace NomakeApi {
    enum class DebugLevel{
        INFO,
        WARING,
        ERROR,
        CRITICAL_ERROR
    };
    void debug(DebugLevel dbg_lvl, char* str, int code = 0);
}