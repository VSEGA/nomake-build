/*
	Main File
*/
#include "NApp.h"
#include <string.h>

/*
	Main Function
*/
int main(int argc, const char* argv[]) {
	NApplication app(argc, argv);
	app.run();
	return 0;
}