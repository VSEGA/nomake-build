#include "NApp.h"
namespace NomakeApi {

FLAGS NApplication::Arg2Flag(const char* arg) {
	if (arg == "--cxx") return FLAGS::CXX;
	else if (arg == "--target") return FLAGS::TARGET;
	else if (arg == "--linker") return FLAGS::LINKER;
	debug(DebugLevel::CRITICAL_ERROR, "Inccorect Arg", (int) ErrorsCodes::IncorrectArg);
}

NApplication::NApplication(){
	this->current_flags = new FLAGS[];
	this->curr_flags_len = 0;
}

NApplication::NApplication(int argc, const char* argv[]) {
	this->current_flags = new FLAGS[argc];
	this->curr_flags_len = 0;
	this->setArgs(argc, argv);
}

void NApplication::setArgs(int argc, const char* argv[]) {
	for(int i = 0; i < argc; i++) {
		this->current_flags[this->curr_flags_len++] = this->Arg2Flag(argv[i]);
	}
}
}