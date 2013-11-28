# M1Algo project's Makefile
#

REPORT=rapport
REPORT_PATH=docs/$(REPORT)
COVERFILE=.coverage

.DEFAULT: check benchmarks
.PHONY: check benchmarks covercheck

benchmarks:
	./ben.sh

check:
	python3 tests/test.py

# You need to install 'coverage':
#   [sudo] pip3 install coverage
covercheck:
	coverage3 run --omit='tests/**' tests/test.py
	coverage3 report -m

report: $(REPORT_PATH).pdf

clean:
	rm -f *~ */*~
	rm -f $(COVERFILE)
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
