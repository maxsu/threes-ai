# Process this file with autoconf to produce a configure script.

# Specify autoconf macro directory.
AC_CONFIG_MACRO_DIR([m4])

# Require autoconf >= 2.71.
AC_PREREQ([2.71])

# Define project name, version, issues URL, repo name, repo url.
AC_INIT(
    [Threes! AI],
    [1.1.1], 
    [https://github.com/nneonneo/threes-ai/issues],
    [threes-ai],
    [https://github.com/nneonneo/threes-ai])

# Define source files location.
AC_CONFIG_SRCDIR([threes_cpp/threes.cpp])

# Define config header output location.
AC_CONFIG_HEADERS([threes_cpp/config.h])

# Ensure we have a C++ toolchain
AC_LANG([C++])

# Use C++ 11 if available.
# - Upgrade to C++ 20
AX_CXX_COMPILE_STDCXX_11([], [optional])

# Provide C++ linker, C++ & C compilers.
AC_PROG_CXX
AC_PROG_CPP
AC_PROG_CC

# Provide MKDIR_P.
AC_PROG_MKDIR_P

# Check header files.
AC_CHECK_HEADERS([fcntl.h stdint.h stdlib.h string.h sys/time.h unistd.h unordered_map tr1/unordered_map])

# Check typedefs, structures, and compiler characteristics.
AC_C_INLINE
AC_TYPE_UINT16_T
AC_TYPE_UINT64_T

# Check library functions (time of day, stringchar, arc4 uniform random numbers, {drand48?})
AC_CHECK_FUNCS([gettimeofday strchr arc4random_uniform drand48])

# Generate Makefile from Makefile.in
# - May be deprecated
# - autreconf warns: AC_OUTPUT should be called without arguments
#   - suggest run {autoconf update?} 
AC_OUTPUT(Makefile)
