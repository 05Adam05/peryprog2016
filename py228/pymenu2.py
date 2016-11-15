import xml.etree.ElementTree as et
tree = et.parse('menu2.xml')
root = tree.getroot()
print(root.tag)
for child in root:
    print('тэг:',child.tag,'атрибут:',child.attrib)
    for grandchild in child:
        print('\t\tтэг:',grandchild.tag,'атрибут:',grandchild.attrib)
        print('\t',grandchild.text)