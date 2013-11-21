# M1Algo project's Makefile
#

REPORT=rapport
REPORT_PATH=docs/$(REPORT)

.DEFAULT: check benchmarks
.PHONY: check benchmarks

benchmarks:
	./ben.sh

check:
	python3 tests/test.py

report: $(REPORT_PATH).pdf

clean:
	rm -f *~ */*~
	for ext in toc aux log bbl blg; do \
		rm -f *.$$ext docs/*.$$ext; \
	done

$(REPORT_PATH).pdf: $(REPORT_PATH).tex $(REPORT_PATH).bib
	cd docs; \
	pdflatex $(REPORT); \
	bibtex $(REPORT); \
	bibtex $(REPORT); \
	pdflatex $(REPORT); \
	pdflatex $(REPORT);
