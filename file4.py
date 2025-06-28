# r+ -----> write and read

file4 = open('myfile4.txt', 'r+')
writing_file4=file4.write('welcome India!')
file4.close()

file4=open('myfile4.txt','r+')
reading_file4=file4.read()
print(reading_file4)
file4.close()