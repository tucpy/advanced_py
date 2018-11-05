import xml.sax

class StudentHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.CurrentData = ""
        self.ids = ""
        self.name = ""
        self.date = ""

    # Call when an element starts
    def startElement(self, tag, attributes):
        self.CurrentData = tag
        if tag == "student":
            print("*****Student*****")
            ids = attributes['id']
            print ("ID", ids)
    
    # Call when an element ends:
    def endElement(self,tag):
        if self.CurrentData == "id":
            print("ID:", self.ids)
        elif self.CurrentData == "name":
            print("Name:", self.name)
        elif self.CurrentData == "date":
            print("Date:", self.date)
        self.CurrentData = ""
    
    # Call when a character is read:
    def characters(self, content):
        if self.CurrentData == "id":
            self.ids = content
        elif self.CurrentData == "name":
            self.name = content
        elif self.CurrentData == "date":
            self.date = content

if (__name__ == "__main__"):
    # create an XMLReader
    parser = xml.sax.make_parser()
    # turn off namespaces
    parser.setFeature(xml.sax.handler.feature_namespaces, 0)
    # overide the default ContentHandler
    Handler = StudentHandler()
    parser.setContentHandler(Handler)

    parser.parse("files/student.xml")