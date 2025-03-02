CXX = g++
CXXFLAGS = -std=c++17 -pedantic-errors
DEBUGFLAGS = -g
BUILD_DIR = ./build
LC_SOLUTION_PATH ?= lc_path
LC_SOLUTION_FILE ?= lc_solution

# This is default target
clean_then_compile:
	@echo "This is default target" # Do not show the command

clean:
	@echo "Force delete the executable if exist"
	rm -f $(BUILD_DIR)/$(LC_SOLUTION_FILE).exe

compile: clean
	$(CXX) $(CXXFLAGS) $(DEBUGFLAGS) -o $(BUILD_DIR)/$(LC_SOLUTION_FILE).exe $(LC_SOLUTION_PATH)/$(LC_SOLUTION_FILE).cpp
	@echo "Successfully compiled $(LC_SOLUTION_FILE).cpp at $(shell date "+%Y-%m-%d %H:%M:%S")"