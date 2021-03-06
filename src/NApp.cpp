#include "NApp.h" 
#include "Api/debug.h" // Debug class and DebugLevel enum
#include "Tools/preprocessor.h" // preprocessor()
#include <string.h>
#include "Tools/lexer.h" // lexer()


FLAGS NApplication::Arg2Flag(const char* arg) {
	if (!strcmp(arg, "--cxx")) return FLAGS::CXX; // Set the compiler
	else if (!strcmp(arg, "--target")) return FLAGS::TARGET; // target machine
	else if (!strcmp(arg, "--linker")) return FLAGS::LINKER; // linker
	Debug::print(DebugLevel::ERROR, "Inccorect Arg", (int) ErrorsCodes::IncorrectArg, arg); // If anothers if-s didn't run
	return FLAGS::UNKOWN;
}

NApplication::NApplication(){}

NApplication::NApplication(int argc, const char* argv[]) {
	setArgs(argc, argv); // Set the args
}

void NApplication::setArgs(int argc, const char* argv[]) {
	if (argc != 1) { // If argc contains things without file name
		for(int i = 1; i < argc; i++) {
			args.push_back(Arg2Flag(argv[i])); // Setting the args
		}
	}
}

void NApplication::run() {
	FILE *f = fopen("NomakeScript.ns", "r"); // Open the file
	str in; // File buffer
	char ch = fgetc(f); // Sym buffer
	while(ch != EOF) { // Read file
		in += ch;
		ch = fgetc(f);
	}
	lexer(preprocessor(in)); // Start program
}