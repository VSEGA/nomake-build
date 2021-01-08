#pragma once
#include "types.h"

/*
	Universal(for class, func and var) object class
*/
struct ID {
	str name; // Name
	unsigned short type; // Type(class_t, func_t, var_t)
};


struct Expression {
	bool isID;
	union {
		ID func;
		ID id;
	};
	std::vector<Expression> args;
	Expression() {}
	Expression(const Expression& expr) {
		isID = expr.isID;
		func = expr.func;
		args = expr.args;
	}
};