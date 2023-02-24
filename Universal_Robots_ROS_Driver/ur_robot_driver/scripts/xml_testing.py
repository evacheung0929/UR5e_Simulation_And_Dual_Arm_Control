
from xml.dom import minidom
from xml.etree import ElementTree as ET
from datetime import datetime

import os

class XML_FILES_2:
    def __init__(self, enc_serial):
        # self.pcb_serial = pcb_serial
        self.enc_serial = enc_serial
        # self.parent_code = "ParentBarcode"
        # the path for where the xml will be saved to
        self.file_path = '/home/cheungy/Barcode/'

        # creating the xml document ready to receive elements
                
    def generate_xml(self):
        t = datetime.utcnow().strftime(("%Y/%m/%d %H:%M:%S:%f"))
        t = t[:-3]
    

        root = ET.Element('TestData')
        ET.SubElement(root,"Operator")
        ET.SubElement(root,'ParentBarcode').text = self.enc_serial
        
        m = ET.SubElement(root,"Measurements")
        m2 = ET.SubElement(m, 'Measurement')
        
        data = {'Name':'Thermal Paste Dispense verification',
                'URL':' ',
                'Sequence':1,
                'MeasurementType':'',
                'Result':'PASSED',
                'DateAndTime':t}
        for i in data:
            ET.SubElement(m2,i).text = str(data[i])
            # print(data[i])  --> 'Thermal paste...'      
        xml = ET.tostring(root)
        # print(xml)
        
        # xml_str = xml.toprettyxml(indent='\t', encoding='utf-8')
        # # xml_str = minidom.parseString(ET.tostring(root)).toprettyxml(indent="\t")
        xmlstr = minidom.parseString(ET.tostring(root)).toprettyxml(indent="   ", encoding = 'utf-8')
        # print(xmlstr)
        self.file_name = self.file_path + str(self.enc_serial)+'.xml'
        
        # # write the xml file into the provided file path
        # # With binary mode, we cannot use the encoding keyword argument when opening a file. Decode required
        with open(self.file_name,'w') as f:
            f.write(xmlstr.decode('utf-8'))
        return f


# def get_input():

#     while True:
#         # put every 2 scan into info_hold
#         info_hold = []
#         for i in range(0,2):
#             info_hold.append(input() + '\n')

#         enclosure_serial = info_hold[0]
#         pcb_serial = info_hold[1]
#         # current file name = unit name; enclosure serial number
#         cur_file_name = path + '/' + enclosure_serial.split()[0] + '.xml'
#         print(cur_file_name)
#         if enclosure_serial != pcb_serial:
#             xml = XML_files(pcb_serial.split()[0],enclosure_serial.split()[0], cur_file_name)#cur_file_name)
#             xml.generate_xml()