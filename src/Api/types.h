#pragma once
#include <string>
#include <array>
#include <unordered_map>

using str = std::string; // String
constexpr std::array<char, 6> extrasym = {'(', ')', '[', ']', '{', '}'};

enum class LexTokensTypes{
    ID, // ID
    CSTART, // (
    CEND, // )
    FSTART, // {
    FEND, // }
    ASTART, // [
    AEND // ]
};

struct LexToken
{
    LexTokensTypes type;
    str id;
};


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
