import xml.etree.ElementTree as et

tree = et.parse('menu.xml')
root = tree.getroot()
print(root.tag)
for child in root:
	print('тег:',child.tag,'атрибуты',child.attrib)
	for grandchild in child:
		print('тег:',grandchild.tag,'атрибуты',grandchild.attrib)
		print('\tтекст:',grandchild.text)