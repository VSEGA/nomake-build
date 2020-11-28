#include "tools.h"
#include "../Api/types.h"

/*
    Conevrting sym to lexem
*/
str convertToken(char sym) {
    switch (sym)
    {
    case '[':
        return "SSTART";
    case ']':
        return "SEND  ";
    case '}':
        return "FEND  ";
    case '{':
        return "FSTART";
    case ')':
        return "CEND  ";
    case '(':
        return "CSTART";
    case ';':
        return "ENDLIN";
    case '.':
        return "POINT ";
    case '+':
        return "PLUS  ";
    case '-':
        return "MINUS ";
    case '*':
        return "MULTIP";
    case '/':
        return "DIVISN";
    case '%':
        return "PERCEN";
    case '=':
        return "EQUSET";
    case '!':
        return "NOT   ";
    case '<':
        return "SMALL ";
    case '>':
        return "BIG   ";
    case '&':
        return "AND   ";
    case '|':
        return "OR    ";
    default:
        return "      ";
    }
}

str lexer(str in) {
    str out;
    str buffer;
    for(auto it = in.cbegin(); it != in.cend(); it++) {
        if(*it == ' ' && buffer.length() != 0) {
            out += str("ID    ") + buffer + "\n";
            buffer = "";
        }
        else if(std::find(extrasym.cbegin(), extrasym.cend(), *it) != extrasym.cend()) {
            if (buffer.length() != 0) {
                out += str("ID    ") + buffer + "\n" + convertToken(*it) + "\n";
                buffer = "";
            }
            else {
                out += convertToken(*it) + "\n";
                buffer = "";
            }
        }
        else {
            if (*it != '\n') {
                buffer += *it;
            }
        }
        }
    return out;
    }