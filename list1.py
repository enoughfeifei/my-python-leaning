fname = raw_input("Enter file name: ")
try:
    fh = open(fname)
except:
    print "this file is not exist!"
    quit()
lst = list()
for line in fh:
    i=0
    word=line.split()
    if lst:
        for i in range(len(word)):
            if word[i] in lst:
                i=i+1
            else:
                lst.append(word[i])
                i=i+1
    else:
        lst.append(word[i])
        i=i+1
        for i in range(len(word)):
            if word[i] in lst:
                i=i+1
            else:
                lst.append(word[i])
                i=i+1
lst.sort()
print lst