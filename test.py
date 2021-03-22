import nltk
#from xml.dom import minidom
#from xmlfile import checknegation
text = nltk.word_tokenize(input())
x = nltk.pos_tag(text)
print(x)
#negationflag = checknegation(text)
nf = 0
z =["no","not","don't","haven't","weren't","wasn't","didn't","hadn't","shouldn't","wouldn't","won't","dont","havent","werent","wasnt","didnt", "hadnt","shouldnt","wouldnt","wont"]
for i in text:
	if i in z:
		nf = 1
	
count = 0
words = []
for i in x:
	if i[1] == "JJ" or i[1] == "VBG" or i[1] == "VBN" or i[1] == "VBP" or i[1] == "NN":
		count = count + 1
		words.append(i[0])
print(words)
f_ptr = open("/home/preran/Documents/Synesketch/bin/data/lex/synesketch_lexicon.txt", "r")
details = f_ptr.readlines() 
scorelist = []
wordlist = []
for i in details: 
	v = i.split()
	wordlist.append(v[0])
	list1 = []
	list1.append(v[2])
	list1.append(v[3])
	list1.append(v[4])
	list1.append(v[5])
	list1.append(v[6])
	list1.append(v[7])
	scorelist.append(list1)
hcount = 0
scount = 0
acount = 0
fcount = 0 
dcount = 0
sucount = 0
list2 = [0]*6 
list4 = [0]*6
for i in words:
	if i in wordlist:	
		y = wordlist.index(i)
		val = max(scorelist[y])
		#w = scorelist[y].index(val)
		q = scorelist[y].index(val)
		if q == 0:
			hcount = hcount + 1
			list2[0] = hcount
			list4[0] = float(val) 		
		elif q == 1:	
			scount = scount + 1
			list2[1] = scount
			list4[1] = float(val) 
		elif q == 2:
			acount = acount + 1
			list2[2] = acount
			list4[2] = float(val) 
		elif q == 3:
			fcount = fcount + 1
			list2[3] = fcount
			list4[3] = float(val) 
		elif q == 4:
			dcount = dcount + 1
			list2[4] = dcount
			list4[4] = float(val) 
		else:
			sucount = sucount + 1
			list2[6] = sucount
			list4[6] = float(val) 

#list2 = [hcount, scount, acount, fcount, dcount, sucount]
list3 = ['happy', 'sad', 'angry', 'fear', 'disgust', 'surprise']

a = max(list2)
c = max(list4)
b = list2.index(a)
if(list4.index(max(list4))==(b)):
	if nf == 1:
		if list3[b] == 'happy':
			print("sad")
		elif list3[b] == 'sad':
			print("happy")
		elif list3[b] == 'fear':
			print("confident")
		elif list3[b] == 'angry':
			print("surprise")
		elif list3[b] == 'surprise':
			print("happy")
	else:
		print(list3[b])

	#print(list3[b])



#print(scorelist)


#print(count)
#print(x)
