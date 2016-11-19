import subprocess
import os
import shutil

cwd_dir = r'C:\Users\cheng\workspace\gxp\apps\gfe\gfeclient'
git_dir = r'"C:\Program Files\Git\bin\git.exe"'

pr=subprocess.Popen(git_dir + " " + 'log --name-status HEAD^..HEAD',
    cwd=os.path.abspath(cwd_dir),
    stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=False)
# (out,error)=pr.communicate()
# print """\
# print '%s\n'
# """ % out

file_changed_list = []

while True:
  line = pr.stdout.readline()
  if line != '':
    if line.startswith("M\t") or line.startswith("A\t"):
        print "file changed/added:", line.rstrip()
        file_changed_list.append(line)
  else:
    break

# additional file to copy
# file_changed_list.append(r"Mtest/atp-automation/crimson_testcases/telemetry/telemetrytest_base.py")

print "list: " + str(file_changed_list)

dbgpkg_dir = r'\\netapp-hq03\atpdataus\atp\Applications\GFE3\dbgpkg\dbgpkg_cheng'

if os.path.isdir(dbgpkg_dir):
    print "Deleting: " + dbgpkg_dir
    shutil.rmtree(dbgpkg_dir)

print "Making: " + dbgpkg_dir
os.mkdir(dbgpkg_dir)

def copytree(fullpath):
    path = fullpath.split("/")
    file_name = path[-1]
    path = path[1:-1]
    print "path: " + str(path)
    print "file_name: " + file_name

    folder = ""
    for f in path:
        folder += r"\\" + f
        if not os.path.isdir(dbgpkg_dir + folder):
            print "Making: " + dbgpkg_dir + folder
            os.mkdir(dbgpkg_dir + folder)

    fullpath = cwd_dir + '\\' + fullpath.replace('/','\\')
    print "Copying: from " + fullpath + " to " + dbgpkg_dir + folder + r'\\' + file_name
    shutil.copyfile(fullpath, dbgpkg_dir + folder + r'\\' + file_name)

for file in file_changed_list:
    file = file.replace('\n', '')
    file = file.replace('\t', '')
    file = file[1:]
    copytree(file)