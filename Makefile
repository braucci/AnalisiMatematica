# ---------------------------------------------------------------------------
#  Analisi Matematica — Makefile
#  make          compila il libro (LuaLaTeX via latexmk)
#  make figure   rigenera le figure prodotte con Python (cartella figure/)
#  make clean    rimuove i file ausiliari
#  make distclean rimuove anche il PDF
# ---------------------------------------------------------------------------
MAIN = main
PY   = python3

all: $(MAIN).pdf

$(MAIN).pdf: $(MAIN).tex stile/*.sty frontmatter/*.tex capitoli/*.tex capitoli/*/*.tex
	latexmk -lualatex -interaction=nonstopmode $(MAIN)

figure:
	for f in python/fig_*.py; do $(PY) $$f; done

clean:
	latexmk -c $(MAIN)
	rm -f $(MAIN).ind $(MAIN).idx $(MAIN).ilg $(MAIN).synctex.gz

distclean: clean
	rm -f $(MAIN).pdf

.PHONY: all figure clean distclean
