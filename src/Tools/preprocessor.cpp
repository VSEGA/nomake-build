#include "tools.h"

str preprocessor(str &in) {
    SettingsBuffer options;
    options.multi_comment_started = false;
    options.single_comment_started = false;
    str out;
    in += ' ';
    for (long i = 0; i < in.length() - 1; i++) {
        if (options.single_comment_started && in[i] == '\n') { // If single comment and end line
            options.single_comment_started = false;
            out += '\n';
            continue;
        }
        else if (!options.single_comment_started && in[i] == '/' && in[i + 1] == '/') { // set single comment
            options.single_comment_started = true;
            i++;
            continue;
        }
        else if (!options.multi_comment_started && in[i] == "/"[0] && in[i + 1] == '*') { // set multi comment
            options.multi_comment_started = true;
            i++;
            continue;
        }
        else if (options.multi_comment_started && in[i] == '*' && in[i + 1] == '/') { // unset multi comment 
            options.multi_comment_started = false;
            i++;
            continue;
        }
        if (options.multi_comment_started || options.single_comment_started) continue;
        out += in[i];
    }
    return out;
}
