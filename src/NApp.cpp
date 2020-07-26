#include "NApp.h" 
#include "Api/debug.h" // debug() and DebugLevel enum
#include "Preprocessor/fdescriptor.h" // NomakeTools::preprocessor()

namespace NomakeApi {
FLAGS NApplication::Arg2Flag(const char* arg) {
	if (arg == "--cxx") return FLAGS::CXX; // Set the compiler
	else if (arg == "--target") return FLAGS::TARGET; // target machine
	else if (arg == "--linker") return FLAGS::LINKER; // linker
	debug(DebugLevel::ERROR, "Inccorect Arg", (int) ErrorsCodes::IncorrectArg, (char*) arg); // If anothers if-s didn't run
	return FLAGS::UNKOWN; 
}

NApplication::NApplication(){
	this->options.args = new FLAGS[]; // new dynamic memory
	this->options.args_len = 0; // len of args without file name
}

NApplication::NApplication(int argc, const char* argv[]) {
	this->options.args = new FLAGS[argc]; // new dynamic memory
	this->options.args_len = 0; // len of args without file name
	this->setArgs(argc, argv); // Set the args
}

void NApplication::setArgs(int argc, const char* argv[]) {
	if (argc != 1) { // If argc contains things without file name
		for(int i = 1; i < argc; i++) {
			this->options.args[this->options.args_len++] = this->Arg2Flag(argv[i]);
		}
	}
}

void NApplication::run() {
	NomakeTools::preprocessor("NomakeScript.ns"); // Run the script
}
}