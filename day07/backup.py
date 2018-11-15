#!/usr/local/bin/python3.6
import time
import os
import tarfile
import hashlib
import pickle
def check(fname):
    md5dict={}
    for path,folders,files in os.walk(fname):
        for file in files:
            data=os.path.join(path,file)
            m=hashlib.md5()
            m.update(data.encode('utf-8'))
            md5_value=m.hexdigest()
            md5dict.update({data:md5_value})
    return md5dict
    pass
def full_backup(src_dir,dst_dir,md5_file):
    fname=os.path.basename(src_dir.rstrip())
    fname="%s_full_%s.tar.gz" % (fname,time.strftime("%Y%m%d"))
    fname=os.path.join(dst_dir,fname)
    tar=tarfile.open(fname,"w:gz")
    tar.add(src_dir)
    tar.close()

    # fname=os.path.join(dst_dir,"md5.data")
    md5_data=check(src_dir)
    with open(md5_file,"wb") as fobj:
        pickle.dump(md5_data,fobj)
    pass
def incr_backup(src_dir,dst_dir,md5_file):
    with open(md5_file,"rb") as fobj:
        old_md5=pickle.load(fobj)
    md5_data = check(src_dir)
    with open(md5_file,"wb") as fobj:
        pickle.dump(md5_data,fobj)
    fname = os.path.basename(src_dir.rstrip())
    fname = "%s_incr_%s.tar.gz" % (fname, time.strftime("%Y%m%d"))
    fname = os.path.join(dst_dir, fname)
    tar = tarfile.open(fname, "w:gz")
    for key in md5_data:
        if  old_md5.get(key) != md5_data[key]:
            tar.add(key)
        else:
            return
    tar.close()

    pass

if __name__ == '__main__':
    src_dir="/tmp/demo/security"
    dst_dir="/tmp/demo/backup"
    md5_file="/tmp/demo/backup/md5.data"
    if time.strftime("%a")=="Thu":
        full_backup(src_dir,dst_dir,md5_file)
    else:
        incr_backup(src_dir,dst_dir,md5_file)
    # print(check("/usr/local"))