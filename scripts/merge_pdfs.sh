# pdftk thesis.pdf cat 2-r4 output bulk.pdf

echo "Converting to PDF version 1.7..."
ghostscript -q -sDEVICE=pdfwrite -dCompatibilityLevel=1.7 -o thesis1p7.pdf thesis.pdf # convert to version 1.7, default is 1.5

echo "Adjusting cover and back..."
pdflatex -output-directory=couverture couverture/4eme.tex 2>&1 > /dev/null
pdflatex -output-directory=couverture couverture/1ere.tex 2>&1 > /dev/null
pdftk thesis1p7.pdf cat 2-r1 output bulk.pdf
pdftk couverture/4eme.pdf cat 1 output back.pdf
pdftk couverture/1ere.pdf bulk.pdf back.pdf cat output thesis_final.pdf

echo "Done."
rm bulk.pdf back.pdf thesis1p7.pdf couverture/4eme.pdf couverture/1ere.pdf
