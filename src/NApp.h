/*
	Base Application Class 
*/
#pragma once
#include "Api/types.h" // For use FLAGS, SETTINGS ENUMS, ErrorsCodes

class NApplication {
		protected:
			/*
				Contains args
			*/
			SETTINGS options;
		public:
			/*
				Convert string to enum FLAGS
			*/
			FLAGS Arg2Flag(const char arg[]);
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