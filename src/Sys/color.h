#pragma once
#include "sys.h"

namespace NomakeSys {
    void colorText(char* str, NomakeApi::Color fg, NomakeApi::Color bg = NomakeApi::Color::BLACK);
}