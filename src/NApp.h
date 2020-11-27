/*
	Base Application Class 
*/
#pragma once
#define _CRT_SECURE_NO_WARNINGS
#include "Api/types.h" // For use FLAGS, SETTINGS ENUMS, ErrorsCodes
#include <vector>

class NApplication {
		protected:
			std::vector<FLAGS> args; // Args
		public:
			/*
				Convert string to enum FLAGS
			*/
			FLAGS Arg2Flag(const char *arg);
			/*
				Set Args without constructer
			*/
			void setArgs(int argc, const char* argv[]);
			/*
				Constructure with args
			*/
			NApplication(int argc, const char* argv[]);
			/*
				Constructure without args
			*/
			NApplication();
			/*
				Run the Nomake!
			*/
			void run();
};