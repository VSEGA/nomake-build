#include "color.h"

namespace NomakeSys {
    void colorText(char* str, NomakeApi::Color fg, NomakeApi::Color bg = NomakeApi::Color::BLACK) {
        NomakeSys::printColorText(str, bg, fg);
    }
}