echo not-injections headers with ifdef:
find .. \( -name '*.h' -or -name '*.hpp' -or -name '*.m' -or -name '*.mm' -or -name '*.cpp' \) -exec grep -Hn \#ifndef {} \;|grep -v injections

echo includes without directory:
find .. \( -name '*.h' -or -name '*.hpp' -or -name '*.m' -or -name '*.mm' -or -name '*.cpp' \) -exec grep -HGn "\#include \"[^\.]\+" {} \;
