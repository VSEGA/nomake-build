#pragma once

namespace NomakeApi {

enum class Color {
    RED,
    GREEN,
    WHITE,
    YELLOW,
    LIGHT_BLUE,
    BLUE,
    GRAY,
    BLACK,
    MAGENTA
};

short unkown = 1;

enum class ErrorsCodes {
    Win32GetConsoleScreenBuffer = 1,
    OutOfRange,
    NotFoundItem,
    IncorrectArg
};

struct SettingsBuffer {
    bool multi_comment_started;
    bool single_comment_started;
};

enum class FLAGS
{	
	CXX,
	LINKER,
	TARGET,
    UNKOWN
};

struct SETTINGS
{
    FLAGS *args;
    int args_len;
};

}