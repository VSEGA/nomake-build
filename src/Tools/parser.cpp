#include "tools.h"
#include <vector>

using line = std::vector<element>;

struct element {
	str type;
	str id;
};

str parser(str& in) {
	str out;
	str buffer;
	line ln;
	for (auto i = 0; i < in.length();)
	{
		if ( in[i], in[i + 1], in[i + 2], in[i + 3], in[i + 4], in[i + 5] == 'I', 'D', ' ', ' ', ' ', ' ') {
			buffer = "";
			for (int j = i + 6; in[j] != '\n'; j++) {
				i = j;
				buffer += in[j];
			}
			ln.push_back(element{"ID", buffer});
			++i;
		}
		else if (in[i], in[i + 1], in[i + 2], in[i + 3], in[i + 4], in[i + 5] == 'E', 'N', 'D', 'L', 'I', 'N') {
			
		}
	}

	return out;
}