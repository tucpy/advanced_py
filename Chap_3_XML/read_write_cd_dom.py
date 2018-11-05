
from xml.dom.minidom import parse
import xml.dom.minidom
import os.path


# Class CD
class CD ():
    def __init__(self,ten, ca_si, so_bai_hat, gia_thanh):
        self.ten = ten
        self.ca_si = ca_si
        self.so_bai_hat = so_bai_hat
        self.gia_thanh = gia_thanh


# Ghi CD vao XML
def make_xml(ten_file, cd):

    if (os.path.isfile(ten_file)):
        doc = xml.dom.minidom.parse(ten_file)
        root_xml = doc.documentElement
    else:
        doc = Document()
        root_xml = doc.createElement('cds')
        doc.appendChild(root_xml)

    child_node = doc.createElement('cd')

    child_node.setAttribute('ten', cd.ten)
    root_xml.appendChild(child_node)

    ca_si = doc.createElement('ca_si')
    ca_si.appendChild(doc.createTextNode(cd.ca_si))
    child_node.appendChild(ca_si)

    so_bai_hat = doc.createElement('so_bai_hat')
    so_bai_hat.appendChild(doc.createTextNode(cd.so_bai_hat))
    child_node.appendChild(so_bai_hat)

    gia_thanh = doc.createElement('gia_thanh')
    gia_thanh.appendChild(doc.createTextNode(cd.gia_thanh))
    child_node.appendChild(gia_thanh)

    return doc

# Doc danh sach CD tu file XML:

def read_xml(ten_file):
    DOMTree = xml.dom.minidom.parse(ten_file)
    collection = DOMTree.documentElement

    cds = collection.getElementsByTagName("cd")

    for cd in cds:
        print("---- CD ----")
        if cd.hasAttribute("ten"):
            print("Ten CD: %s" % cd.getAttribute("ten"))
        ca_si = cd.getElementsByTagName('ca_si')[0]
        print("Ca si: %s" % ca_si.childNodes[0].data)
        so_bai_hat = cd.getElementsByTagName('so_bai_hat')[0]
        print("Format: %s" % so_bai_hat.childNodes[0].data) 
        gia_thanh = cd.getElementsByTagName('gia_thanh')[0]
        print("Rating: %s" % gia_thanh.childNodes[0].data)
    return

if __name__=="__main__":
    tiep_tuc = 1
    while tiep_tuc ==1:
        i = int(input("Ban muon lam gi? 1: Them CD moi, 2: Xem danh sach CD\t"))
        if i == 1:
            ten = input("Nhap ten CD:\t")
            ca_si = input("Nhap ten ca si:\t")
            so_bai_hat = input("Nhap so bai hat:\t")
            gia_thanh = input("Gia thanh:\t")

            cd = CD(ten, ca_si, so_bai_hat, gia_thanh)
            make_xml('files/cd.xml', cd).writexml(open(file='files/cd.xml', mode ='w', encoding='utf8'), indent='', addindent='', newl='')
            print("Da them CD")
        
        elif i ==2:
            read_xml('files/cd.xml')
        
        tiep_tuc = int(input("Ban co muon tiep tuc ko? 1: Co, 0: Khong\t"))