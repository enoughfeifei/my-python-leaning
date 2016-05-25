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
    if not line.startswith("From"):continue
    if line.startswith("From:"):
        word=line.split()
        if word[1] not in count:
            count[word[1]]=1
        else:
            count[word[1]]+=1
bigname=None
bigcount=None
for words,counts in count.items():
    if counts is None or counts>bigcount:
        bigname=words
        bigcount=counts
print  bigname,",",bigcount
