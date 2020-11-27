/*
	Use this file for print info to user
*/
#pragma once
#define _CRT_SECURE_NO_WARNINGS 
#include "types.h"
/*
	These debugLevels differ in color and label
*/
enum class DebugLevel{
	INFO,
	WARING,
	ERROR,
	CRITICAL_ERROR
};

/*
	Use this function to print text(And standart getchar/gets/scanf to get symbols)
*/

class Debug
{
public:
	static char *buffer; // Formatting buffer
	static void print(DebugLevel dbg_lvl, str out, int code = 0, str additinal_info = "");
};
