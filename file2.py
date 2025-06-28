file2 = open('myfile2.txt', 'w')

writing_file=file2.write('Hello Wolrd, i am currently reading pyhon')
print(writing_file)

file2.close()

file2=open('myfile2.txt','r')
reading_file2 = file2.read()
print(reading_file2)
file2.close()