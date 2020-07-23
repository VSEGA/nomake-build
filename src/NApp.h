#pragma once
#include "Api/settings.h"
#include "Api/debug.h"

namespace NomakeApi {
	class NApplication {
		protected:
			SETTINGS options;
		public:
			FLAGS Arg2Flag(const char* arg);
			void setArgs(int argc, const char* argv[]);
			NApplication(int argc, const char* argv[]);
			NApplication();
	};
}