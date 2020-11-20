#include "fdescriptor.h"
#include "comments.h" // comments()

void preprocessor(std::string str) {
    SettingsBuffer *options; // Settings Buffer
    for(auto it = str.cbegin()) {
        buffer[0] = buffer[1];
        buffer[1] = fgetc(in);
        fputc(comments(buffer, options), out);
    }
    fclose(in);
    return out;
}
