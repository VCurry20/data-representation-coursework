# Exercise 1.1
# Create an XML file that stores data for a library (You can create this manually, I am not asking you to create a program to do this). 
# The library has two catalogues (technical books, and for cookery books).
# Each catalogue can contain a number of books (say 2 for the purpose of this exercise) . 
# Books will have an ISBN, title and author.


# https://www.geeksforgeeks.org/create-xml-documents-using-python/
# https://stackoverflow.com/questions/66651767/how-to-create-xml-file-using-python
# https://towardsdatascience.com/processing-xml-in-python-elementtree-c8992941efd2


import xml.etree.cElementTree as ET
import xml.dom.minidom

m_encoding = 'UTF-8'

root = ET.Element("Catalogue")
doc1 = ET.SubElement(root, "Book", name="Book")
doc = ET.SubElement(root, "Book", name="Book")
ET.SubElement(doc, "ISBN").text = "ISBN = 1245262784"
ET.SubElement(doc, "Title").text = "Tech Book1"
ET.SubElement(doc, "Author").text = "Joe Walsh"

doc = ET.SubElement(root, "Book", name="Book")
ET.SubElement(doc, "ISBN", ISBN ="4590937402").text = "ISBN"
ET.SubElement(doc, "Title", Title="Tech Book1").text = "Tech Book12"
ET.SubElement(doc, "Author", Author="Joe Walsh").text = "Joe Walsh"

dom = xml.dom.minidom.parseString(ET.tostring(root))
xml_string = dom.toprettyxml()
part1, part2 = xml_string.split('?>')

with open("FILE.xml", 'w') as xfile:
    xfile.write(part1 + 'encoding=\"{}\"?>\n'.format(m_encoding) + part2)
    xfile.close()