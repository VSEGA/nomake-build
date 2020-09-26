#include "comments.h"

namespace NomakeTools {
    char comments(char s[2], NomakeApi::SettingsBuffer *options) {
        if (options->single_comment_started && s[0] == '\n') { // If single comment and end line
            options->single_comment_started = false;
            return '\n';
        }
        else if (!options->single_comment_started && s[0] == '/' && s[1] == '/') { // set single comment
            options->single_comment_started = true;
            return '\0';
        }
        else if (!options->multi_comment_started && s[0] == "/"[0] && s[1] == "*"[0]) { // set multi comment
            options->multi_comment_started = true;
            return '\0';
        }
        else if (options->multi_comment_started && s[0] == '*' && s[1] == '/') { // unset multi comment 
            options->multi_comment_started = false;
            return '\0';
        }
        return s[0];
    }
}