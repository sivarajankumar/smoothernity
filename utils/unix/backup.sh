FILE=smoothernity-backup-`date "+%Y-%m-%d"`.tar.bz2
rm $FILE
echo Creating backup \"$FILE\"...
tar --exclude .hg -cjf $FILE `dirname $0`/../../../repo `dirname $0`/../../../repo.wiki `dirname $0`/../../../repo.stable
echo Done.
md5 $FILE
