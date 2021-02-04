#pip install num2words
from num2words import num2words
import collections
word=str(input())
length=""
count=1
if len(word)>1:
    for i in range(1,len(word)):
       if word[i-1]==word[i]:
          count+=1
       else :
           length += num2words(count)+" "+word[i-1]+"'s"+" and "
           count=1
    length += ("and "+num2words(count)+" "+word[i]+"'s")
else:
    i=0
    length += ("and "+num2words(count)+" "+word[i]+"'s")
print (length)
l=list(word)
p=[]
for i in l:
    p.append(int(i))
c = collections.Counter(p)
for key, value in c.items():
   print(f"{num2words(value)}{( key)}")

