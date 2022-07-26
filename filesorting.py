import os
import shutil

# This was made for a backup drive of mine that sorts out the extra files Apple creates with photos

name = input("Name of folder to be procesed\n >")
inputfolder = "E:/Photos Backup/" + name
outputfolder = "E:/Photos Backup/Processed " + name

# If you want to use this elsewhere, uncomment that ↓↓↓ (Remember to use / instead of \ in your directory)

#inputfolder = input("Directory of input folder (ex. D:/Downloads/coolfolder)\n  >")
#outputfolder = input("Directory of output folder\n  >")

filelist = []
duplicateslist = []

# Get all files from input folder, split files from suffix
filedump = os.listdir(inputfolder)
for file in filedump:
    filelist.append([os.path.splitext(file)[0], os.path.splitext(file)[1]])

# Making sure no files were missed
print(len(filelist), "files found. Correct?")
wait = input()

# Find files with .AAE suffix, tag them for sorting
for file in filelist:
    if file[1] == ".AAE":
        duplicateslist.append(file[0])

# Making sure all duplicates were found
print(duplicateslist)
print(len(duplicateslist), "duplicates found. Correct?")
wait = input()

# Sort out .AAE and the pre-edited file with same name
newlist = [file for file in filelist if file[0] not in duplicateslist]
print("New list is", len(newlist), "files")


newlist = [file[0] + file[1] for file in newlist]
print(newlist)

for file in newlist:
    shutil.copy(inputfolder + "/" + file, outputfolder)



