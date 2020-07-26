/*
	Main File
*/
#include "NApp.h"

/*
	Main Function
*/
int main(int argc, const char* argv[]) {
	NomakeApi::NApplication app = NomakeApi::NApplication(argc, argv);
	app.run();
	return 0;
}