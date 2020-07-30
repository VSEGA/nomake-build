#include "color.h"

namespace NomakeSys {
    void colorText(const char str[], NomakeApi::Color fg, NomakeApi::Color bg) {
        NomakeSys::printColorText(str, fg, bg);
    }
}