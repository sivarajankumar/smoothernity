cmake .
make
./sandbox
luacov *
cat luacov.report.out
