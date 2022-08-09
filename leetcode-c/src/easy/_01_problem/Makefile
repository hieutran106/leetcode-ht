PROBLEM_DIR = easy/_01_problem
OUTDIR = build
CFFLAGS = -g -I./build/include
PROBLEM_SOURCE = src/$(PROBLEM_DIR)/solution.c src/$(PROBLEM_DIR)/test_solution.c
PROBLEM_HEADER = src/$(PROBLEM_DIR)/solution.h

.PHONY: clean

all: hello compile-seatest compile-util clean compile

hello:
	@echo "Current working directory " $(pwd)
	@echo $(OUTDIR)/$(PROBLEM_DIR)

compile-seatest: src/seatest/seatest.h src/seatest/seatest.c
	@echo "Create Deps folder"
	mkdir -p $(OUTDIR)/deps
	@echo "Compile seatest"
	gcc -g -c src/seatest/seatest.c -o $(OUTDIR)/deps/seatest.o
	@echo "Copy seatest header to include folder"
	mkdir -p $(OUTDIR)/include/seatest
	cp src/seatest/seatest.h $(OUTDIR)/include/seatest/

compile-util: src/util/tree.h src/util/tree.c
	gcc -g -c src/util/tree.c -o $(OUTDIR)/deps/tree.o
	mkdir -p $(OUTDIR)/include/util
	cp src/util/tree.h $(OUTDIR)/include/util/

clean:
	rm -rf src/$(PROBLEM_DIR)/test_solution.out

compile: $(PROBLEM_SOURCE) $(PROBLEM_HEADER)
	gcc $(PROBLEM_SOURCE) build/deps/seatest.o build/deps/tree.o -o src/$(PROBLEM_DIR)/test_solution.out $(CFFLAGS)

run-solution-test: src/$(PROBLEM_DIR)/test_solution.out
	src/$(PROBLEM_DIR)/test_solution.out