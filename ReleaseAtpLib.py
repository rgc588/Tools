import os
import shutil

share_paths = [r"\\netapp-hq03\atpdataus\ATP\Libraries", r"\\netapp-pu02\atpdatapune\atp\Libraries", r"\\vel-tdc-2\atpdatatdc\atp\Libraries"]
lib_files = [r"atplib.dll", r"atplib.pdb"]
local_path = r"C:\Users\cheng\Perforce\cheng_CHENG-LT_3558\sw\qa\Atplib1.5.x.x\atplib\bin\Debug"

for path in share_paths:
    for file_name in lib_files:
        src = os.path.join(local_path, file_name)
        dst = os.path.join(path, file_name)
        print "Copying from " + src + "\n"
        "to " + dst
        shutil.copyfile(src, dst)
