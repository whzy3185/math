#!/usr/bin/env bash
# Workspace-only fallback for an incomplete installed TeX format database.
set -euo pipefail
# Stable document dates when supported by pdfTeX; this does not change mathematics.
export SOURCE_DATE_EPOCH="${SOURCE_DATE_EPOCH:-1791187200}"
export FORCE_SOURCE_DATE=1
cd "$(dirname "$0")"
mkdir -p texmf/var texmf/config
export TEXMF="{$PWD/texmf/var,/usr/share/texmf,/usr/share/texlive/texmf-dist}"
export TEXMFVAR="$PWD/texmf/var" TEXMFCONFIG="$PWD/texmf/config"
export TEXFONTMAPS="$PWD/texmf//:"
cat /usr/share/texmf/fonts/map/dvips/lm/lm.map \
 /usr/share/texlive/texmf-dist/fonts/map/dvips/amsfonts/{cm,cmextra,symbols,latxfont}.map > texmf/pdftex.map
if [ ! -f pdflatex.fmt ]; then
 pdftex -ini -interaction=nonstopmode -halt-on-error -jobname=pdflatex -progname=pdflatex -etex pdflatex.ini > format.log 2>&1
fi
pdflatex -interaction=nonstopmode -halt-on-error manuscript.tex > build1.log 2>&1
pdflatex -interaction=nonstopmode -halt-on-error manuscript.tex > build2.log 2>&1
