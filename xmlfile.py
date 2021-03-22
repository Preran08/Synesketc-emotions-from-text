import xml.etree.ElementTree as ET
def checknegation(listwords):
	tree = ET.parse('/home/preran/Downloads/Synesketch/bin/data/lex/keywords.xml')
	root = tree.getroot()
	x = root.tag
	y = root.attrib
	z = "no, not, don't, haven't, weren't, wasn't, didn't, hadn't, shouldn't, wouldn't, won't, dont, havent, werent, wasnt, didnt, hadnt, shouldnt, wouldnt, wont"
	#for child in root:
	#	print(child.tag, child.attrib)
	#z = root[1].text
	strings = z.split(',')
	s = root[0].text
	for i in listwords:
		if i in strings:
			return 1
	return 0

	
