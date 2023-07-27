#This is fixed file
f = open("myfile.txt", "w")
f.write("This is my first file!")
f.close()

f = open("myfile.txt")
print(f.read())
f.close()

f = open("myfile.txt", "a")
f.write(" And second ...")
f.close()
f = open("myfile.txt")
print(f.read())
f.close() 
import os

file_name = "myfile.txt"

# Get the current working directory
current_dir = os.getcwd()

# Combine the current working directory with the file name to get the full file path
file_path = os.path.join(current_dir, file_name)
print("Dir path:", current_dir)
print("File Path:", file_path)