DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
rm -rf /tmp/smoothernity/docs
mkdir -p /tmp/smoothernity/docs
cp -r $DIR/* /tmp/smoothernity/docs
cd /tmp/smoothernity/docs
pdflatex smoothernity.tex
pdflatex smoothernity.tex
pdflatex smoothernity.tex

cp /tmp/smoothernity/docs/smoothernity.pdf $DIR/
