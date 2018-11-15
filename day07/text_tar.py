import tarfile
import os
tar=tarfile.open("/tmp/a.tar.gz","w:gz")
os.chdir("/etc")
tar.add("passwd")
tar.add("fstab")
tar.close()
try:
    os.makedirs("/tmp/a")
except FileExistsError:
    print("目录已存在,不再重新创建")
os.chdir("/tmp/a")
tar=tarfile.open("/tmp/a.tar.gz","r:gz")
tar.extractall()
tar.close()