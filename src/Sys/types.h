#pragma once
#include <string>
#include <array>
#include <unordered_map>
// Types of IDs objects
#define func_t 1
#define class_t 2
#define var_t 3

#define str std::string

constexpr std::array<char, 19> extrasym = { '(', ')', 
'[', ']', 
'{', '}', 
';', '.', 
'+', '-', '*', '/', '%', 
'=', '!', '<', '>', '&', '|'}; // Sym which seperate ids in lexer
const std::unordered_map<char, unsigned short> level = {
	{'+', 1},
	{'-', 1},
	{'*', 2},
	{'/', 2}
};


/*
	This enum is using for print func in debug.h/cpp
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
	Errors codes
*/
enum ErrorsCodes {
	Win32GetConsoleScreenBuffer = 1,
	NotFoundId,
	IncorrectArg
};

/*
	Preprocessor internal flags
*/
struct SettingsBuffer {
	bool multi_comment_started;
	bool single_comment_started;
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