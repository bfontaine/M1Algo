# M1Algo project's Makefile
#

.DEFAULT: check benchmarks
.PHONY: check benchmarks

benchmarks:
	./ben.sh

check:
	python3 tests/test.py
