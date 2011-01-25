echo not-injections headers with ifndef:
find .. \( -name '*.h' -or -name '*.hpp' -or -name '*.m' -or -name '*.mm' -or -name '*.cpp' \) -exec grep -Hn \#ifndef {} \;|grep -v injections\\.|grep -v /injections/

echo incorrect ifndef names:
find .. \( -name '*.h' -or -name '*.hpp' -or -name '*.m' -or -name '*.mm' -or -name '*.cpp' \) -exec grep -Hn \#ifndef {} \;|grep -v injections_included$|grep -v _shy_injections_

echo includes without directory:
find .. \( -name '*.h' -or -name '*.hpp' -or -name '*.m' -or -name '*.mm' -or -name '*.cpp' \) -exec grep -HGn "\#include \"[^\.]\+" {} \;
