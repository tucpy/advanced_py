import xml.sax

class StudentHandler(xml.sax.ContentHandler):
    sl = 0;

    def __init__(self):
        self.CurrentData = ""
        self.phone = ""
        self.name = ""
    
    # Call when an element starts
    def startElement(self, tag, attributes):
        self.CurrentData = tag
        print("List of contacts:")

        if tag == "contact":
            print("--- Contact ", StudentHandler.sl,"---")
            name = attributes["name"]
            print("Name:", name)
            phone = attributes["phone"]
            print("Phone:", phone)
        StudentHandler.sl +=1

if (__name__ == "__main__"):

    # Create an XMLReader
    parser = xml.sax.make_parser()

    # turn off namespaces
    parser.setFeature(xml.sax.handler.feature_namespaces, 0)
    # overide the default ContentHandler
    Handler = StudentHandler()
    parser.setContentHandler(Handler)

    parser.parse("files/contact.xml")