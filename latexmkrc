# latexmk configuration: compile with LuaLaTeX, build the index with makeindex
$pdf_mode = 4;            # 4 = lualatex
$lualatex = 'lualatex -interaction=nonstopmode -file-line-error -synctex=1 %O %S';
$makeindex = 'makeindex %O -o %D %S';
$clean_ext = 'synctex.gz run.xml bbl idx ind ilg';
