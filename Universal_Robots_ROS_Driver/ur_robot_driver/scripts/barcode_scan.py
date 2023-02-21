import glob
import os
from xml_files import XML_files

# chang this to the local file path directory
path = '/home/cheungy'

# Get the most RECENT file in the folder
def latest_file_search():
    lst = glob.glob(path+'/*.xml')
    # return the full path name of the latest file
    latest_file = max(lst, key = os.path.getctime)
    # 'A1023.xml'
    base_name = os.path.basename(latest_file)
    # 'name' + format, e.g. 'A1023' + '.xml'
    cur_file_name = os.path.splitext(base_name)
    # 'A1023'
    max_unit_name = cur_file_name[0]
def get_input():

    while True:
        # put every 2 scan into info_hold
        info_hold = []
        for i in range(0,2):
            info_hold.append(input() + '\n')

        enclosure_serial = info_hold[0]
        pcb_serial = info_hold[1]
        # current file name = unit name; enclosure serial number
        cur_file_name = path + '/' + enclosure_serial.split()[0] + '.xml'
        print(cur_file_name)
        if enclosure_serial != pcb_serial:
            xml = XML_files(pcb_serial.split()[0],enclosure_serial.split()[0], cur_file_name)#cur_file_name)
            xml.generate_xml()
get_input()