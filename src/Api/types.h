#pragma once
#include <string>
#include <array>

using str = std::string; // String
constexpr std::array<char, 6> extrasym = {'(', ')', '[', ']', '{', '}'}; // Sym which seperate ids in lexer

/*
    Colors
*/
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

/*
    Errors
*/
enum class ErrorsCodes {
    Win32GetConsoleScreenBuffer = 1,
    OutOfRange,
    NotFoundItem,
    IncorrectArg
};

/*
    NPreprocessor internal flags
*/
static struct SettingsBuffer {
    bool multi_comment_started = false;
    bool single_comment_started = false;
};

/*
    Internal command line args
*/
enum class FLAGS
{	
	CXX,
	LINKER,
	TARGET,
    UNKOWN
};
