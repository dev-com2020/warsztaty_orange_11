import xml.etree.ElementTree as ET

tree = ET.parse('dane.xml')

root = tree.getroot()

# print(root.tag)
# print(root.attrib)
#
# for child in root:
#     print(child.tag, child.attrib)

# print([elem.tag for elem in root.iter()])
# for movie in root.iter('movie'):
#     print(movie.attrib)

# for desc in root.iter('description'):
#     print(desc.text)

# for movie in root.findall("./genre/decade/movie/[year='1992']"):
#     print(movie.attrib)
#
# for movie in root.findall("./genre/decade/movie/format/[@multiple='Yes']..."):
#     print(movie.attrib)

b2tf = root.find("./genre/decade/movie[@title='Back 2 the Future']")
b2tf.attrib["title"] = "Powrot do przyszlosci"
print(b2tf.attrib)
tree.write('movies.xml')