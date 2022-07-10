# Customer analytics framework for online retail stores

In this project, we propose to build an application that will help online retail stores in offering personalized services to customers. To achieve better results, three strategies in customer analytics are considered in this project - a personalized recommendation system, categorization of customers, and sales trend analysis for achieving better customer retention.

Features
Robustness.

Supports the full SML 97 language as given in The Definition of Standard ML (Revised).

A complete implementation of the Basis Library.

Generates standalone executables.

Compiles large programs.

Support for large amounts of memory (up to 4G on 32-bit systems; more on 64-bit systems).

Support for large array lengths (up to 231 - 1 on 32-bit systems; up to 263-1 on 64-bit systems).

Support for large files, using 64-bit file positions.

Performance.

Executables have excellent runtime performance.

Generates small executables.

Untagged and unboxed native integers, reals, and words.

Unboxed native arrays.

Multiple garbage collection strategies.

Fast arbitrary-precision arithmetic based on GMP.

Tools.

Source-level profiling for both time and allocation.

MLLex lexer generator.

MLYacc parser generator.

MLNLFFIGEN foreign-function-interface generator.

Extensions.

The ML Basis system for programming with source libraries.

A number of useful language extensions.

A simple and fast C FFI that supports calling from SML to C and from C to SML.

Libraries for weak pointers and finalization, threads, continuations, interval timers and signal handlers, world save and restore, and more.

Portability.

Runs on a wide variety of platforms.

Build and Install (from source)
Requirements
Software
GCC or Clang (The C compiler must support -std=gnu11.)

GMP (GNU Multiple Precision arithmetic library)

GNU Make

GNU Bash

binutils (ar, ranlib, strip, …​)

miscellaneous Unix utilities (diff, find, grep, gzip, patch, sed, tar, xargs, …​)

Standard ML compiler and tools to bootstrap:

MLton (mlton, mllex, and mlyacc) recommended. Pre-built binary packages for MLton can be installed via an OS package manager or (for select platforms) obtained from http://mlton.org.

SML/NJ (sml, ml-lex, ml-yacc) supported, but not recommended.

(optional, for documentation only) TeX, AsciiDoctor, Rouge, GraphicsMagick or ImageMagick, …​

Hardware
≥ 1GB RAM (for 32-bit platforms) or ≥ 2GB RAM (for 64-bit platforms)

Build Instructions
On typical platforms, building MLton requires no configuration and can be accomplished via:

$ make all
A small set of Makefile variables can be used to customize the build:

CC: Specify C compiler. Can be used for alternative tools (e.g., CC=clang or CC=gcc-7).

WITH_GMP_DIR, WITH_GMP_INC_DIR, WITH_GMP_LIB_DIR: Specify GMP include and library paths, if not on default search paths. (If WITH_GMP_DIR is set, then WITH_GMP_INC_DIR defaults to $(WITH_GMP_DIR)/include and WITH_GMP_LIB_DIR defaults to $(WITH_GMP_DIR)/lib.)

MLTON_RUNTIME_ARGS, MLTON_COMPILE_ARGS: Specify runtime and compile arguments given to (the to-be-built) mlton when compiling distributed executables ((self-compiled) mlton, mllex, mlyacc, mlprof, and mlnlffigen). Can be used for testing (e.g., MLTON_COMPILE_ARGS="-codegen c") or for downstream packaging.

OLD_MLTON_RUNTIME_ARGS, OLD_MLTON_COMPILE_ARGS: Specify runtime and compile arguments given to "old" mlton when compiling "new" mlton. Can be used to work around bugs in "old" mlton when compiling "new" mlton.

For example:

$ make CC=clang WITH_GMP_DIR=/opt/gmp MLTON_COMPILE_ARGS="-codegen c" all
The build artifacts are located under ./build. The just-built mlton can be executed via ./build/bin/mlton.

Building documentation can be accomplished via:

$ make docs
Install Instructions
On typical platforms, installing MLton (after performing make all and, optionally, make docs) to /usr/local can be accomplished via:

$ make install
A small set of Makefile variables can be used to customize the installation:

PREFIX: Specify the installation prefix.

For example:

$ make PREFIX=/opt/mlton install
Install (from binary package)
Requirements
Software
GCC or Clang (The C compiler must support -std=gnu11.)

GMP (GNU Multiple Precision arithmetic library)

GNU Make

GNU Bash

miscellaneous Unix utilities (bzip2, gzip, sed, tar, …​)

Binary Package
A .tgz or .tbz binary package can be extracted at any location, yielding README.adoc (this file), CHANGELOG.adoc, LICENSE, Makefile, bin/, lib/, and share/. The compiler and tools can be executed in-place (e.g., ./bin/mlton).

A small set of Makefile variables can be used to customize the binary package via make update:

CC: Specify C compiler. Can be used for alternative tools (e.g., CC=clang or CC=gcc-7).

WITH_GMP_DIR, WITH_GMP_INC_DIR, WITH_GMP_LIB_DIR: Specify GMP include and library paths, if not on default search paths. (If WITH_GMP_DIR is set, then WITH_GMP_INC_DIR defaults to $(WITH_GMP_DIR)/include and WITH_GMP_LIB_DIR defaults to $(WITH_GMP_DIR)/lib.)

For example:

$ make CC=clang WITH_GMP_DIR=/opt/gmp update
Install Instructions
On typical platforms, installing MLton (after optionally performing make update) to /usr/local can be accomplished via:

$ make install
A small set of Makefile variables can be used to customize the installation:

PREFIX: Specify the installation prefix.

For example:

$ make PREFIX=/opt/mlton install
Resources
http://mlton.org

Development

https://github.com/ar1422/CSCI-620-Group-Project.git

Support and Contributing
To report bugs or suggest new features, use the issue tracker or ask on the mailing list.

Pull requests with bug fixes or changes are welcome.
