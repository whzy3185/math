.PHONY: test paper paper-en paper-zh clean

test:
	@test -f src/normal_form.py && test -f tests/test_normal_form.py || (echo "Use the complete delivered source ZIP for the verification code."; exit 1)
	python -m unittest discover -s tests -v

paper: paper-en paper-zh

paper-en:
	cd paper && pdflatex -interaction=nonstopmode -halt-on-error main.tex
	cd paper && pdflatex -interaction=nonstopmode -halt-on-error main.tex

paper-zh:
	cd paper && xelatex -interaction=nonstopmode -halt-on-error main_zh.tex
	cd paper && xelatex -interaction=nonstopmode -halt-on-error main_zh.tex

clean:
	rm -f paper/*.aux paper/*.log paper/*.out paper/*.fdb_latexmk paper/*.fls
	rm -rf src/__pycache__ tests/__pycache__
