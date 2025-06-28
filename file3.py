file3=open('myfile3.txt', 'w')
writing_file=file3.write('hello everyone ')
file3.close()


file3=open('myfile3.txt', 'a')
appending_file=file3.write('Welcome to the world of python')
file3.close()

file3=open('myfile3.txt','r')
reading_file3=file3.read()
print(reading_file3)