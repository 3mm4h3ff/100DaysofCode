#sequential
name = input('Enter file: ')
handle = open(name, 'r')

counts = dict()
#repeated 
for line in handle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word,0) + 1

#sequential
bigcount = None
bigword = None

#repeated
for word,count in counts.items():
    #conditional
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

#sequential
print(bigword,bigcount)
