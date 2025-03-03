CXX = g++
CXXFLAGS = -std=c++17 -pedantic-errors
STRICT_CXXFLAGS = -std=c++17 -pedantic-errors -Wall -Weffc++ -Wextra -Wconversion -Wsign-conversion
DEBUGFLAGS = -g
BUILD_DIR = ./build
LC_SOLUTION_PATH ?= lc_path
LC_SOLUTION_FILE ?= lc_solution

.PHONY: clean

# This is default target
clean_then_compile:
	@echo "This is default target" # Do not show the command

build/catch_amalgamated.o: test/catch_amalgamated.cpp
	@echo "Compiling catch 2"
	g++ --std=c++17 -c $< -o $@

clean:
	@echo "================================"
	@echo "Force delete the executable if exist"
	rm -f $(BUILD_DIR)/$(LC_SOLUTION_FILE).exe


compile: build/catch_amalgamated.o clean
	@echo "================================"
	@echo "Compiling the solution file"
	$(CXX) $(CXXFLAGS) $(DEBUGFLAGS) -o $(BUILD_DIR)/$(LC_SOLUTION_FILE).exe $(LC_SOLUTION_PATH)/$(LC_SOLUTION_FILE).cpp $<
	@echo "Successfully compiled $(LC_SOLUTION_FILE).cpp at $(shell date "+%Y-%m-%d %H:%M:%S")"