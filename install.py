import os

os.system("pkg install python")
os.system("pkg install dos2unix")
os.system("pip install requests colorama")
os.system("cp ~/Spammer_Grab2/spammer.py $PREFIX/bin/Spammer_Grab2")
os.system("dos2unix $PREFIX/bin/Spammer_Grab2")
os.system("chmod 777 $PREFIX/bin/Spammer_Grab2")
os.system("Spammer_Grab2")
