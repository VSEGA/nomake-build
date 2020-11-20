#include "NApp.h" 
#include "Api/debug.h" // debug() and DebugLevel enum
#include "Tools/Preprocessor/fdescriptor.h" // NomakeTools::preprocessor()
#include <string.h>


FLAGS NApplication::Arg2Flag(const char arg[]) {
	if (!strcmp(arg, "--cxx")) return FLAGS::CXX; // Set the compiler
	else if (!strcmp(arg, "--target")) return FLAGS::TARGET; // target machine
	else if (!strcmp(arg, "--linker")) return FLAGS::LINKER; // linker
	debug(DebugLevel::ERROR, "Inccorect Arg", (int) ErrorsCodes::IncorrectArg, arg); // If anothers if-s didn't run
	return FLAGS::UNKOWN; 
}

NApplication::NApplication(){
	this->options.args = new FLAGS[1]; // new dynamic memory
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
	fclose(preprocessor("NomakeScript.ns")); // Run the script
}