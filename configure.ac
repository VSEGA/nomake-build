#                                               -*- Autoconf -*-
# Process this file with autoconf to produce a configure script.

AC_PREREQ([2.69])
AC_INIT([nomake], [0.0.1], [tupjnin@gmail.com])
AC_CONFIG_SRCDIR([src/NApp.h])
AC_CONFIG_HEADERS([config.h])

# Checks for programs.
AC_PROG_CXX
AC_PROG_CC
AM_INIT_AUTOMAKE

# Checks for libraries.

# Checks for header files.
AC_CHECK_HEADERS([limits.h stdlib.h string.h unistd.h])

# Checks for typedefs, structures, and compiler characteristics.
AC_CHECK_HEADER_STDBOOL
AC_C_INLINE

# Checks for library functions.
AC_CHECK_FUNCS([getcwd])

AC_CONFIG_FILES([Makefile
                 src/Api/Makefile
                 src/Makefile
                 src/Sys/Makefile
                 src/Tools/Makefile
                 src/Tools/Preprocessor/Makefile])
AC_OUTPUT
