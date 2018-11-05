from xml.dom.minidom import Document
import xml.dom.minidom
import os.path

def make_xml(ten_file):

    if (os.path.isfile(ten_file)):
        doc = xml.dom.minidom.parse(ten_file)
        root_xml = doc.documentElement
    else:
        doc = Document()
        root_xml = doc.createElement('books')
        doc.appendChild(root_xml)

    child_node = doc.createElement('book')
    noi_dung = "Duong xa con hat"
    child_node.setAttribute("title", noi_dung)
    root_xml.appendChild(child_node)

    author = doc.createElement("author")
    tac_gia = "Do Nhat Nam"
    author.appendChild(doc.createTextNode(tac_gia))
    child_node.appendChild(author)
    return doc

if __name__=="__main__":
    make_xml('book.xml').writexml(open(file='book.xml', mode='w', encoding='utf8'), indent='', addindent='', newl='')