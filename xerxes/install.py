import os
os.system("apt install php")
print("Installing XERXES")
os.system("gcc xerxes.c -o xerxes")
os.system("php servers.php")
print("XERXES Installed, you can run it by doing - sudo ./xerxes fakesite.com 80")
