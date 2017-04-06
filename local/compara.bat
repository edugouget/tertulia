cscript //nologo tmp.js > tmp.bat
call tmp.bat
python compara.py > compara_LOG_%YYYYMMDD%.txt
del tmp.bat

exit