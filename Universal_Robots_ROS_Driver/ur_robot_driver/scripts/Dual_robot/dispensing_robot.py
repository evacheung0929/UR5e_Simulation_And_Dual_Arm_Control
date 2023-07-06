#! usr/bin/env python

''' 
    THIS IS FOR SIMULATION ROBOT
    This script test out
    1. Dispensing pad retouch
    2. Load and run sequential program 
    by using dashboard server to call and play pre-writtened program on the UR5 pendant
    It is intend to be integrated with GUI
    Note, if the position between different programs are too too far away, it may fail to execute 'play' 
 '''

from dashboard_dual_service import Dashboard_Client
from ur_dashboard_msgs.srv import Load, LoadRequest, RawRequest,RawRequestRequest,Popup, PopupRequest, IsInRemoteControl,IsInRemoteControlRequest, GetRobotMode, GetRobotModeRequest, IsProgramRunning, IsProgramRunningRequest
from std_srvs.srv import Trigger, TriggerRequest
import time

class Dispense_Program:
    def __init__(self):
        ''' The sub program names on the teach pendant for each dispensing action range from 0 to 14.
            changing the variable type from int to str
        '''
        self.dispense = Dashboard_Client('load_program', Load, LoadRequest(),'d') 
        self.sub_prog_names = list(range(0,15))
        for i in self.sub_prog_names:
            self.sub_prog_names[i] = str(i)
        
    def main_start(self):
        ''' This is for the start of the entire program. Will only run once
            e.g. From safety position to the pad 1, would be more useful for the pick and place robot,
            as in the absence of enclosure in assembnly station require extra waiting period for pasting,
            but this only takes place once'''
        prog_name = 'new_tube'
        self.dispense.load(file_name=prog_name)

    def start_pasting(self):    
        ''' Load and play every single provided program.
            The pause after loading the porgram is to ensure the UR5 controller has time to react to the command
            
            1. Play the program if it is not already playing after the play execution
            2. when the program is running, wait for it to finish
            '''
        for j in range(0, len(self.sub_prog_names)):
            self.dispense.load(file_name = self.sub_prog_names[j])

            time.sleep(2)
            self.dispense.play()

            if self.dispense.program_runing() != True:
                print('wait')
                time.sleep(1)
                self.dispense.play()
            
            while self.dispense.program_runing():
                print(f"starting program: {self.sub_prog_names[j]}")
            # while self.dispense.program_runing():
                time.sleep(1)
                print(f" Running: {self.sub_prog_names[j]}")

    def dispense_correction(self, *retry_pad):
        self.dispense.load(file_name = 'retry')
        self.dispense.play()

        if self.dispense.program_runing() != True:
            print('waiting 4 retry program')
            time.sleep(2)
            self.dispense.play()        

        while self.dispense.program_runing():
            time.sleep(1)
            print('pasting')
        
        for i in range(0,len(retry_pad)):
            self.dispense.load(file_name = self.sub_prog_names[retry_pad[i]])
            self.dispense.play()

            if self.dispense.program_runing() != True:
                print('wait....pad')
                time.sleep(2)
                self.dispense.play()

            while self.dispense.program_runing():
                time.sleep(1)
                print('pasting pad!')
            self.dispense.load(file_name = 'high')
            self.dispense.play()


''' xml thoughts
    When the robot is moving while picking up the board
    launch a new program/shell to just store the serial number
    
    As the UI will be the only program running at the end, it will be the one that takes
    in the keyboard (It should be a touch screen so the scanner should be the only input)

    Can simply do
        for i in programs:
            if i == program_15:
                get_input
                if get_input != True:
                    time.sleep()
                .......
    '''

''' This is to loop through predefine number of program'''
# dispense = Dispense_Program()
# user_input = 3
# dispense.start()
# for i in range(0,user_input):
#     dispense.start_dispensing()  

''' Dispensing correction after camera input, determining which pad require touch up'''
# correction = Dispense_Program()
# correction.dispense_correction(retry_pad = 10)

# program_list = dispense.sub_prog_names
# simulation = Dashboard_Client('load_program', Load, LoadRequest(),'')    

''' individual program load and play test'''
# # simulation.load(file_name=program_list[2])

# # simulation.load(file_name=program_list[0])
# # simulation.load(file_name='5')
# # simulation.play()
# # print('starting program')


'''looping throught the program for testing'''

program = Dispense_Program()
program.start_pasting()


'''Pasting correction check'''
program.dispense_correction(1,2)
