#include "color.h"
#include <stdio.h> // puts() 

namespace NomakeSys {
    void colorText(const char str[], NomakeApi::Color bg, NomakeApi::Color fg) {
        puts(str); //  Non color text
    }
}