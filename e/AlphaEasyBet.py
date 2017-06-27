#counts = {}
#def countChars(word):
#    for x in word:
#        if(ord(x) < 91): x = chr(ord(x) + 32)
#        counts.__setitem__(x, 1) if not counts.__contains__(x) else counts.__setitem__(x, counts.get(x) + 1) 
#    for y in counts: print("%s: %d" %(y, counts.get(y)))
   
#countChars(input("Type a sentence: "))   

#counts, word = {}, input("Type a sentence: ")
#for x in word:
#    if(ord(x) < 91): x = chr(ord(x) + 32)
#    counts.__setitem__(x, 1) if not counts.__contains__(x) else counts.__setitem__(x, counts.get(x) + 1) 
#for y in counts: print("%s: %d" %(y, counts.get(y)))

counts, word = {}, input("Type a sentence: ")
for x in word:
    if(ord(x) < 91): x = chr(ord(x) + 32)
    counts.__setitem__(x, 1) if not counts.__contains__(x) else counts.__setitem__(x, counts.get(x) + 1) 
for y in counts: print("%s: %d" %(y, counts.get(y)))