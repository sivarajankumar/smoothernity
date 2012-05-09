find ../../../data -name *.shy -exec cat {} \; | python -B -m cProfile ../../codegen/codegen.py ../../../
