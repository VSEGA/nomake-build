#include "lexer.h"
#include "../Api/types.h"
#include <vector>
#define token LexToken
#define types LexTokensTypes

inline str covertToken(types type, str id) {
    switch (type)
    {
    case types::ASTART:
        return "ASTART";

    default:
        return str("ID ") + id;
    }
}

inline void saveToken(token thisToken, FILE* fin) {

}

FILE* lexer(FILE* fin) {
    str buffer;
    char sym;
    FILE* fout = tmpfile();


        do {
            sym = getc(fin);
            if(sym == ' ' && buffer.length() != 0) {

                buffer = "";
            }
            else if(std::find(extrasym.begin(), extrasym.end(), sym) != extrasym.end()) {
                if (len != 0) {

                }
            }
            else {
                buffer[len++] = sym;
            }
            }
        while (sym != EOF);

    fclose(fin);
    return fout;
    }