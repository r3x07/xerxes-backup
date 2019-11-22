import os
os.system("sudo apt install php")
print("Installing XERXES")
os.system("gcc xerxes.c -o xerxes")
os.system("sudo php server.php")
print("XERXES Installed, you can run it by doing - sudo ./xerxes fakesite.com 80")
