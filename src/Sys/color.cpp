#include "color.h"
using namespace NomakeApi;
namespace NomakeSys {
    void colorText(char* str, Color fg, Color bg = Color::BLACK) {
        NomakeSys::printColorText(str, bg, fg);
    }
}