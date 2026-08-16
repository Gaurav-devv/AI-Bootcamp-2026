"""
File handling:-

-> You all know what are files any name with an extension is
file.
-> Now that extension can be .py , .txt , .mp3 etc. and when we
want to handle these files we will use file handling.
-> File handling means Creating, Reading, Updating,
Deleting(CRUD) operations that we can perform in files.
"""


p = open('01-Python/Module-10_File_Handelng/fileHandeling.py', 'r')
#read a file
print(p.read())



r = open("test.txt ",'w') #Create a file or overwrite a file
r.write("Hello this is Gaurav and I am writing inside this file")
r.close()


r = open("test.txt ",'a') # add to end of a file
r.write("And i am appending some content inside this file")
r.close()
