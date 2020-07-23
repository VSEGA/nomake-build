#pragma once

namespace NomakeApi {
enum class FLAGS
{	
	CXX,
	LINKER,
	TARGET,
    UNKOWN
};

struct SETTINGS
{
    FLAGS *args;
    int args_len;
};
}