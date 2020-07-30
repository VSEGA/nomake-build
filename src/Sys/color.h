/*
    Color Text profile
*/

#pragma once
#include "sys.h" 

namespace NomakeSys {
    /*
        Print color Text
    */
    void colorText(const char str[], NomakeApi::Color fg, NomakeApi::Color bg = NomakeApi::Color::BLACK);
}