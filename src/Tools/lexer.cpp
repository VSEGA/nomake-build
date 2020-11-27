#include "lexer.h"
#include "../Api/types.h"

/*
    Conevrting sym to lexem
*/
str convertToken(char sym) {
    switch (sym)
    {
    case '[':
        return "ASTART";
    case ']':
        return "AEND";
    case '}':
        return "FEND";
    case '{':
        return "FSTART";
    case ')':
        return "CEND";
    case '(':
        return "CSTART";
    default:
        return "";
    }
}

str lexer(str &in) {
    str out;
    str buffer;
    for(auto it = in.cbegin(); it != in.cend(); it++) {
        if(*it == ' ' && buffer.length() != 0) {
            out += str("ID ") + buffer;
            buffer = "";
        }
        else if(std::find(extrasym.cbegin(), extrasym.cend(), *it) != extrasym.cend()) {
            if (buffer.length() != 0) {
                out += str("ID ") + buffer + "\n" + convertToken(*it) + "\n";
                buffer = "";
            }
            else {
                out += convertToken(*it) + "\n";
                buffer = "";
            }
        }
        else {
            buffer += *it;
        }
        }
    return out;
    }