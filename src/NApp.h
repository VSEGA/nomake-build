#pragma once
#include "Api/debug.h"
#include "Api/error.h"

namespace NomakeApi {
	enum class FLAGS
	{	
		CXX,
		LINKER,
		TARGET
	};

	class NApplication {
		protected:
			FLAGS *current_flags;
			int curr_flags_len;
		public:
			FLAGS Arg2Flag(const char* arg);
			void setArgs(int argc, const char* argv[]);
			NApplication(int argc, const char* argv[]);
			NApplication();
	};
}