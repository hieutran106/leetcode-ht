PROBLEM_DIR = easy/_01_problem
OUTDIR = build
CFFLAGS = -g -I./build/include

.PHONY: clean-problem

all: hello compile-seatest compile-util clean-problem compile-problem

hello:
	pwd
	@echo $(OUTDIR)/$(PROBLEM_DIR)

compile-seatest: src/seatest/seatest.h src/seatest/seatest.c
	gcc -g -c src/seatest/seatest.c -o $(OUTDIR)/deps/seatest.o
	mkdir -p $(OUTDIR)/include/seatest
	cp src/seatest/seatest.h $(OUTDIR)/include/seatest/

compile-util: src/util/tree.h src/util/tree.c
	gcc -g -c src/util/tree.c -o $(OUTDIR)/deps/tree.o
	mkdir -p $(OUTDIR)/include/util
	cp src/util/tree.h $(OUTDIR)/include/util/

clean-problem:
	rm -rf src/$(PROBLEM_DIR)/test_solution.out

compile-problem: src/$(PROBLEM_DIR)/solution.h src/$(PROBLEM_DIR)/solution.c src/$(PROBLEM_DIR)/test_solution.c
	gcc src/$(PROBLEM_DIR)/solution.c src/$(PROBLEM_DIR)/test_solution.c build/deps/seatest.o build/deps/tree.o -o src/$(PROBLEM_DIR)/test_solution.out $(CFFLAGS)

run-solution-test: src/$(PROBLEM_DIR)/test_solution.out
	src/$(PROBLEM_DIR)/test_solution.out