from xml.dom.minidom import parse
import xml.dom.minidom

# Open XML document using minidom parser
DOMTree = xml.dom.minidom.parse("files/student.xml")
collection = DOMTree.documentElement
if collection.hasAttribute("shelf"):
    print("Root element: %s" %collection.getAttribute("shelf"))

# Get all the student in the collection
students = collection.getElementsByTagName("student")

# Print detail of each student
for student in students:
    print("*****Student*****")
    if student.hasAttribute("id"):
        print("ID:%s" %student.getAttribute("id"))
    name = student.getElementsByTagName('name')[0]
    print("Name: %s" % name.childNodes[0].data)
    date = student.getElementsByTagName("date")[0]
    print("Date of birth: %s" % date.childNodes[0].data)

