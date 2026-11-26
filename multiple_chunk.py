text= """

text or pdf

"""

chunking = text.strip().split("\n")
ch=[]

for i in range(0,len(chunking),2):
    newlist= "".join(chunking[i:i+2])
    ch.append(newlist)

print(ch)
