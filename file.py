'''

#1
file1=open('my_file.txt', 'r')

#directory=specify the location
#mode = r,w,a,r+
reading_file=file1.read()
reading_file1=file1.readline()
print(reading_file)
print(reading_file1) #it is printing only one line
file1.close()
'''




with open('my_file.txt', 'r') as file1:
    reading_file1=file1.read()
    print(reading_file1) #it is printing only one line