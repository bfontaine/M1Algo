# M1Algo project's Makefile
#

REPORT=docs/rapport

.DEFAULT: check benchmarks
.PHONY: check benchmarks

benchmarks:
	./ben.sh

check:
	python3 tests/test.py

report: $(REPORT).pdf

$(REPORT).pdf: $(REPORT).tex $(REPORT).bib
	pdflatex $(REPORT)
	bibtex $(REPORT)
	pdflatex $(REPORT)
	pdflatex $(REPORT)
