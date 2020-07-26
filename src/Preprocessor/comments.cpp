#include "comments.h"

namespace NomakeTools {
    char comments(char s[2], NomakeApi::SettingsBuffer *options) {
        if (options->single_comment_started && s[0] == (char) "\n") { // If single comment and end line
            options->single_comment_started = false;
            return (char) "\n";
        }
        else if (!options->single_comment_started && s[0] == (char) "/" && s[1] == (char) "/") { // set single comment
            options->single_comment_started = true;
            return (char) "";
        }
        else if (!options->multi_comment_started && s[0] == (char) "/" && s[1] == (char) "*") { // set multi comment
            options->multi_comment_started = true;
            return (char) "";
        }
        else if (options->multi_comment_started && s[0] == (char) "*" && s[1] == (char) "/") { // unset multi comment 
            options->multi_comment_started = false;
            return (char) "";
        }
        return s[0];
    }
}