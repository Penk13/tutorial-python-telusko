# 65 - FILE HANDLING

f = open('text','r')    #('file_name','mode')   #r = read mode

print(f)
#print(f.read())    #will print all contents in that file
#print(f.readline(), end="")     #will print the first line in that file
#print(f.readline())     #will print the next line in that file
print()

f2 = open('text2','w')     #w = write mode
#if there is no file, it will create file automatically
f2.write('abc')     #it will send 'abc' to text2 file
# it will only send, not save

f2 = open('text2','a')     #a = append
f2.write('hello')   #it will send 'hello' to text2 file
#it will be saved, not only send

#send everything in text file to text2 file:
for data in f:
    f2.write(data)

#in files we have 2 different mode (character mode and binary mode)
f3 = open('view.JPG','rb')     #rb = read binary

for i in f3:
    print(i)    #image is binary