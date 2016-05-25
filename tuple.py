name=raw_input("Enter file name: ")
if len(name)<1:name="mbox-short.txt"
try:
    fname = open(name)
except:
    print "this file is not exist!"
    quit()
count=dict()
for line in fname:
    line=line.rstrip()
    if line.startswith("From:"):continue
    if line.startswith("From"):
        word=line.split()
        hourtime=word[5].split(":")
        if hourtime[0] not in count:
            count[hourtime[0]]=1
        else:
            count[hourtime[0]]+=1
    else:continue
#lst=list()
#for key,val in count.items():
#    lst.append((key,val))
#lst.sort()
#for key,val in lst:
#    print key,val   输出一对则换行
print sorted([(k,v) for k,v in count.items()])#按照元组的格式（k，v））输出