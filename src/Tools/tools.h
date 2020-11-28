#pragma once

#include "../Api/types.h"
#define _CRT_NO_SECURE_WARNINGS
#include <stdio.h>
#include <string>

/*
	Main function
*/
str lexer(str in);
str preprocessor(str& in);
str parser(str& in);