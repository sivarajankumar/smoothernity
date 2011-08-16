echo =========================
echo modules without scheduler
echo =========================
echo
find ../common \( -name '*.h' -or -name '*.hpp' -or -name '*.m' -or -name '*.mm' -or -name '*.cpp' \) -exec grep -Hn "class shy_common_" {} \;|grep -v stateless|grep -v consts

echo
echo ==================================
echo not-injections headers with ifndef
echo ==================================
echo
find .. \( -name '*.h' -or -name '*.hpp' -or -name '*.m' -or -name '*.mm' -or -name '*.cpp' \) -exec grep -Hn \#ifndef {} \;|grep -v injections\\.|grep -v /injections/

echo
echo ======================
echo incorrect ifndef names
echo ======================
echo
find .. \( -name '*.h' -or -name '*.hpp' -or -name '*.m' -or -name '*.mm' -or -name '*.cpp' \) -exec grep -Hn \#ifndef {} \;|grep -v injections_included$|grep -v _shy_injections_

echo
echo ==========================
echo includes without directory
echo ==========================
echo
find .. \( -name '*.h' -or -name '*.hpp' -or -name '*.m' -or -name '*.mm' -or -name '*.cpp' \) -exec grep -HGn "\#include \"[^\.]\+" {} \;

echo
echo =====================
echo files with tabulation
echo =====================
echo
find .. \( -name '*.h' -or -name '*.hpp' -or -name '*.m' -or -name '*.mm' -or -name '*.cpp' \) -exec grep -Hn \.* {} \; | awk '/\t/'

