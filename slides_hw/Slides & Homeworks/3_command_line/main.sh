# main.sh
# make the books directory
mkdir books

# change directory into bokos
cd books

# print the present working directory
pwd

# check if there's any files in directory
ls

# download Pride & Prejudice
curl -o 1342-0.txt https://www.gutenberg.org/files/1342/1342-0.txt

# list to make sure the file is download
ls

# rename the file 
mv 1342-0.txt pnp.txt

# list to make sure the renaming worked
ls