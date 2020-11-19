#include "fdescriptor.h"
#include "comments.h" // comments()

void preprocessor(std::string &buffer, std::string str) {
    buffer = "";
    FILE *in = fopen(str, "r"); // Input File
    SettingsBuffer *options; // Settings Buffer
    char buffer[2]; // char buffer[0 is char, 1 is next char]

    buffer[0] = fgetc(in);

    while (buffer[1] != EOF) {
        buffer[0] = buffer[1];
        buffer[1] = fgetc(in);
        fputc(comments(buffer, options), out);
    }
    fclose(in);
    return out;
}
