#include "preprocessor.h"

std::string preprocessor(str in) {
    SettingsBuffer options; // Settings Buffer
    str out;
    std::string::const_iterator it = in.cbegin();
    ++it;
    while(it != in.cend()) {
        if (options.single_comment_started && *(it - 1) == '\n') { // If single comment and end line
            options.single_comment_started = false;
            out += '\n';
        }
        else if (!options.single_comment_started && *(it - 1) == '/' && *it == '/') { // set single comment
            options.single_comment_started = true;
        }
        else if (!options.multi_comment_started && *(it - 1) == "/"[0] && *it == '*') { // set multi comment
            options.multi_comment_started = true;
        }
        else if (options.multi_comment_started && *(it - 1) == '*' && *it == '/') { // unset multi comment 
            options.multi_comment_started = false;
        }
        ++it;
    }
    return out;
}
