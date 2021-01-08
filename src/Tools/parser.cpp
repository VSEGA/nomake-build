#include "tools.h"
#include "../Sys/Stack.h"
#include "../Sys/debug.h"
#include <vector>

struct element {
	str type;
	str id;
};

Expression decode(std::vector<element> ln, std::vector<ID> &idTable) {
	Expression expr;
	for (size_t i = 0; i < ln.size(); i++) {
		if (ln[i].type == "MULTIP" or ln[i].type == "DIVISN") {
			if (i == 0) {
//				print()
			}
		}
	}
	return expr;
}


str parser(str& in) {
	str out; // Out string
	str buffer; // Buffer
	std::vector<element> ln; // Elements in expression
	std::vector<ID> idTable;
	for (size_t i = 0; i < in.length();)
	{
		if ( in[i], in[i + 1], in[i + 2], in[i + 3], in[i + 4], in[i + 5] == 'I', 'D', ' ', ' ', ' ', ' ') {
			buffer = "";
			for (int j = i + 6; in[j] != '\n'; j++) { // Get name
				i = j;
				buffer += in[j];
			}
			ln.push_back(element{"ID    ", buffer}); // Add element
			++i; // from \n to next element
		}
		else if (in[i], in[i + 1], in[i + 2], in[i + 3], in[i + 4], in[i + 5] == 'E', 'N', 'D', 'L', 'I', 'N') {
			decode(ln, idTable);
			i += 6;
		}
		else {
			ln.push_back(element{ str{in[i], in[++i], in[++i], in[++i], in[++i], in[++i]} });
			++i;
		}
	}

	return out;
}