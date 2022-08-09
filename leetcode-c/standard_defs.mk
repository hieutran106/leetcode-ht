OUTDIR = build
CFFLAGS = -g -I./build/include
PROBLEM_SOURCE = src/$(PROBLEM_DIR)/solution.c src/$(PROBLEM_DIR)/test_solution.c
PROBLEM_HEADER = src/$(PROBLEM_DIR)/solution.h

.PHONY: clean

all: hello compile-unity compile-util clean compile

hello:
	@echo "Current working directory"
	pwd
	@echo $(OUTDIR)/$(PROBLEM_DIR)

compile-unity: src/unity/unity.h src/unity/unity.c src/unity/unity_internals.h
	@echo "Create Deps folder"
	mkdir -p $(OUTDIR)/deps
	@echo "Compile unity"
	gcc -g -c src/unity/unity.c -o $(OUTDIR)/deps/unity.o
	@echo "Copy unity header to include folder"
	mkdir -p $(OUTDIR)/include/unity
	cp src/unity/unity.h $(OUTDIR)/include/unity/
	cp src/unity/unity_internals.h $(OUTDIR)/include/unity/

compile-util: src/util/tree.h src/util/tree.c
	gcc -g -c src/util/tree.c -o $(OUTDIR)/deps/tree.o
	mkdir -p $(OUTDIR)/include/util
	cp src/util/tree.h $(OUTDIR)/include/util/

clean:
	rm -rf src/$(PROBLEM_DIR)/test_solution.out

compile: $(PROBLEM_SOURCE) $(PROBLEM_HEADER)
	gcc $(PROBLEM_SOURCE) build/deps/unity.o build/deps/tree.o -o src/$(PROBLEM_DIR)/test_solution.out $(CFFLAGS)

run-solution-test: src/$(PROBLEM_DIR)/test_solution.out
	src/$(PROBLEM_DIR)/test_solution.out