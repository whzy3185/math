#!/usr/bin/env bash
# Build with XeLaTeX. The fallback repairs only a local format/search tree.
set -euo pipefail
cd "$(dirname "$0")"
mkdir -p output/pdf tmp/pdfs texmf/var texmf/config texmf/cache
export XDG_CACHE_HOME="$PWD/texmf/cache"
if ! kpsewhich xelatex.fmt >/dev/null 2>&1 || ! kpsewhich article.cls >/dev/null 2>&1; then
  export TEXMF="{$PWD/texmf/var,/usr/share/texmf,/usr/share/texlive/texmf-dist}"
  export TEXMFVAR="$PWD/texmf/var" TEXMFCONFIG="$PWD/texmf/config" TEXMFCACHE="$PWD/texmf/cache"
  if [ ! -f xelatex.fmt ]; then
    xetex -ini -interaction=nonstopmode -halt-on-error \
      -jobname=xelatex -progname=xelatex -etex xelatex.ini > tmp/pdfs/format.log 2>&1
  fi
fi
xelatex -interaction=nonstopmode -halt-on-error -output-directory=output/pdf \
  mycielski_hall_v2.tex > tmp/pdfs/compile_first.txt
xelatex -interaction=nonstopmode -halt-on-error -output-directory=output/pdf \
  mycielski_hall_v2.tex > tmp/pdfs/compile_second.txt
if grep -E 'Overfull|Missing character|Undefined control sequence|There were undefined references' \
  output/pdf/mycielski_hall_v2.log; then
  echo 'Build completed with a layout or reference warning; review before delivery.' >&2
  exit 1
fi
printf 'Built output/pdf/mycielski_hall_v2.pdf\n'
