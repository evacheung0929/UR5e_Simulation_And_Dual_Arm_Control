from xml.dom import minidom
from xml.etree import ElementTree as ET
import os

# set up a xml document ready to recieve info
class XML_files():
    def __init__(self,pcb_serial, enclosure_serial, file_path):
        self.pcb_serial = pcb_serial
        self.enclosure_serial = enclosure_serial
        # the path for where the xml will be saved to
        self.file_path = file_path


        ########################################################

        # creating the xml document ready to receive elements
        self.root = minidom.Document()

        # every xml will create a root name inside root
        ##### self.xml = self.root.createElement('TestData')
        self.xml = self.root.createElement('TestData')
        self.op = self.root.createElement('Operator')
        self.enc = self.root.createElement('ParentBarcode')
        self.m = self.root.createElement('Measurements')
        self.m2 = self.root.createElement('Measurement')
        
        self.name = self.root.createElement('Name')
        self.url = self.root.createElement('URL')
        self.seq = self.root.createElement('Sequence')
        self.mtype = self.root.createElement('MeasurementType')
        self.value = self.root.createElement('Value')
        # what is the difference between unit and parent barcode?
        self.Unit = self.root.createElement('Unit')
        self.Nominal = self.root.createElement('Nominal')
        self.LowerLimit = self.root.createElement('LowerLimit')
        self.UpperLimit = self.root.createElement('UpperLimit')
        self.FailDesc = self.root.createElement('FailDesc')
        self.DateAndTime = self.root.createElement('DateAndTime')
        
        # # attribute of the child, since both are using serial number as a metric of registration
        self.data = 'data'
        ##############################################################

    def generate_xml(self):
        # root = ET.Element('TestData')
        # doc = ET.SubElement(root,"Operator")
        # parent = ET.SubElement(doc,'ParentBarcode')
        # ET.SubElement(parent,'').text = 'Unit number'
        
        # m = ET.SubElement(parent,"Measurements")
        # m2 = ET.SubElement(m, 'Measurement')


        # append 'root' from self.xml to the children of minidom.Document
        self.root.appendChild(self.xml)
        self.xml.appendChild(self.op)
        self.op.appendChild(self.enc)
        self.xml.appendChild(self.m)
        self.m.appendChild(self.m2)
        self.m2.appendChild(self.name)
        self.m2.appendChild(self.url)
        self.m2.appendChild(self.seq)
        self.m2.appendChild(self.mtype)
        self.m2.appendChild(self.FailDesc)
        self.m2.appendChild(self.value)
        self.m2.appendChild(self.Unit)
        self.m2.appendChild(self.Nominal)
        self.m2.appendChild(self.LowerLimit)

        self.m2.appendChild(self.UpperLimit)

        self.m2.appendChild(self.DateAndTime)
        

        # attributes = 'serial number' and pcb sreial
        #### product_one = self.root.createElement('Enclosure')
        name_tag_1 = self.enc
        name_tag_1.setAttribute(self.data, self.enclosure_serial)
        # xml.append will make the PCB inside the variable 'root'
        ##### self.xml.appendChild(product_one)
        self.xml.appendChild(name_tag_1)

        # create an element for pcb
        # product_two = self.root.createElement('PCB')
        name_tag_2 = self.m
        name_tag_2.setAttribute(self.data, self.pcb_serial)
        # self.xml.appendChild(product_two)
        self.xml.appendChild(name_tag_2)
        # convert the entire minidom document with all its children into xml file

        xml_str = self.root.toprettyxml(indent='\t', encoding='utf-8')
        # xml_str = minidom.parseString(ET.tostring(root)).toprettyxml(indent="\t")

        # write the xml file into the provided file path
        # With binary mode, we cannot use the encoding keyword argument when opening a file. Decode required
        with open(self.file_path,'w') as f:
            f.write(xml_str.decode('utf-8'))
        return f