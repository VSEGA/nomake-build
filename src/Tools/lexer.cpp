#include "lexer.h"
#include "../Api/types.h"
#define token LexToken
#define types LexTokensTypes

namespace NomakeTools {
    inline token getToken(char* str) {
        if (str == '{') return token{types::};
    }


    FILE* lexer(FILE* fin) {
        char *buffer = new char[1];
        char sym;
        int len = 0;
        FILE* fout = tmpfile();


        do {
            sym = getc(fin);
            if(sym == ' ' && len != 0) {

            }
            else if(sym == '{') {
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
}