.PHONY: all test pdf clean
all: test pdf
test:
	python verify.py --output verification_results.json
pdf:
	latexmk -xelatex -interaction=nonstopmode -halt-on-error manuscript.tex
clean:
	latexmk -c manuscript.tex
