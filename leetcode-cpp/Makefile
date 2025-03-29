CXX = g++
CXXFLAGS = -std=c++20 -pedantic-errors
STRICT_CXXFLAGS = -std=c++17 -pedantic-errors -Wall -Weffc++ -Wextra -Wconversion -Wsign-conversion
DEBUGFLAGS = -g
BUILD_DIR = ./build
LC_SOLUTION_PATH ?= lc_path
LC_SOLUTION_FILE ?= lc_solution

# Automatically set INCLUDE_TEST_FRAMEWORK based on whether LC_SOLUTION_PATH value includes 'playground' string or not
# Allowing me to include or exclude the test framework as needed.
ifeq ($(shell echo $(LC_SOLUTION_PATH) | grep '^playground'),playground)
    INCLUDE_TEST_FRAMEWORK := 0
else
    INCLUDE_TEST_FRAMEWORK := 1
endif

.PHONY: clean

# This is default target
$(BUILD_DIR)/$(LC_SOLUTION_FILE).out: $(LC_SOLUTION_PATH)/$(LC_SOLUTION_FILE).cpp
# Conditionally include test framework
ifeq ($(INCLUDE_TEST_FRAMEWORK), 1)
$(BUILD_DIR)/$(LC_SOLUTION_FILE).out: build/catch_amalgamated.o
endif
	
	
ifeq ($(INCLUDE_TEST_FRAMEWORK), 1)
	@echo "================================"
	@echo "Compiling the solution file WITH test framework"
	$(CXX) $(CXXFLAGS) $(DEBUGFLAGS) -o $(BUILD_DIR)/$(LC_SOLUTION_FILE).out $(LC_SOLUTION_PATH)/$(LC_SOLUTION_FILE).cpp build/catch_amalgamated.o
else
	@echo "================================"
	@echo "Compiling the solution file *WITHOUT* test framework"
	$(CXX) $(CXXFLAGS) $(DEBUGFLAGS) -o $(BUILD_DIR)/$(LC_SOLUTION_FILE).out $(LC_SOLUTION_PATH)/$(LC_SOLUTION_FILE).cpp 
endif
	@echo "Successfully compiled $(LC_SOLUTION_FILE).cpp at $(shell date "+%Y-%m-%d %H:%M:%S")"

build/catch_amalgamated.o: test/catch_amalgamated.cpp
	@echo "================================"
	@echo "Compiling TEST FRAMWORK catch 2"
	g++ --std=c++17 -c $< -o $@

clean:
	@echo "================================"
	@echo "Force delete the executable if exist"
	@echo "Build directory: $(BUILD_DIR)"
	@echo "Cleaning..."
	rm -fv $(BUILD_DIR)/*.out


