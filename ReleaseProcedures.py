import os
import shutil

local_procedure_path = r"C:\Users\cheng\Perforce\cheng_CHENG-LT_3558\sw\qa\AtpTestcases"
share_procedure_paths = [r"\\netapp-hq03\atpdataus\atp\Procedures", r"\\netapp-pu02\atpdatapune\atp\Procedures", r"\\vel-tdc-2\atpdatatdc\atp\Procedures"]
debug_bin_path = r"bin\Debug"

#  setting
project_folder_name = ""
procedure_folder_name = r"MultipleDisplayDrag"
file_to_copy = ["MultipleDisplayDrag.exe", "MultipleDisplayDrag.pdb"]
#  setting

if project_folder_name == "":
    project_folder_name = procedure_folder_name
source_path = os.path.join(local_procedure_path, procedure_folder_name, project_folder_name, debug_bin_path)
print "source: " + source_path

for file_name in file_to_copy:
    print "Trying to copy: " + file_name
    src = os.path.join(source_path, file_name)
    print "src: " + src
    for dst in share_procedure_paths:
        dst = os.path.join(dst, procedure_folder_name, file_name)
        print "copying to: " + dst
        shutil.copyfile(src, dst)
