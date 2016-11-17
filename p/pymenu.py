import xml.etree.ElementTree as et
tree = et.parse('menu1.xml')
root = tree.getroot()
print(root.tag)
for child in root:
	print('тэг:', child.tag,'атрибут: ', child.attrib)
	for grandchild in child:
		print('\tтэг:', grandchild.tag)
		print('\t\t',grandchild.text)

print(root[1][2].text)