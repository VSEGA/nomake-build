#include "NApp.h"
#include "Api/error.h"

namespace NomakeApi {
FLAGS NApplication::Arg2Flag(const char* arg) {
	if (arg == "--cxx") return FLAGS::CXX;
	else if (arg == "--target") return FLAGS::TARGET;
	else if (arg == "--linker") return FLAGS::LINKER;
	debug(DebugLevel::ERROR, "Inccorect Arg", (int) ErrorsCodes::IncorrectArg);
	return FLAGS::UNKOWN;
}

NApplication::NApplication(){
	this->options.args = new FLAGS[];
	this->options.args_len = 0;
}

NApplication::NApplication(int argc, const char* argv[]) {
	this->options.args = new FLAGS[argc];
	this->options.args_len = 0;
	this->setArgs(argc, argv);
}

void NApplication::setArgs(int argc, const char* argv[]) {
	for(int i = 0; i < argc; i++) {
		this->options.args[this->options.args_len++] = this->Arg2Flag(argv[i]);
	}
}
}