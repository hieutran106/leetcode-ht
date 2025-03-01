CXX = g++
CXXFLAGS = -std=c++17
DEBUGFLAGS = -g
BUILD_DIR = ./build
LC_SOLUTION_PATH ?= lc_path
LC_SOLUTION_FILE ?= lc_solution
clean:
	rm -f $(BUILD_DIR)/*.o

compile:
	$(CXX) $(CXXFLAGS) $(DEBUGFLAGS) -o $(BUILD_DIR)/$(LC_SOLUTION_FILE).exe $(LC_SOLUTION_PATH)/$(LC_SOLUTION_FILE).cpp