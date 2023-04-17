#! usr/bin/env python

''' Check if the program has finished, if finished, then load a specific program

    This is the general flow of the whole program

    If the location between each program is too far away, it may not work?
 '''
from dashboard_dual_service import Dashboard_Client
from ur_dashboard_msgs.srv import Load, LoadRequest, RawRequest,RawRequestRequest,Popup, PopupRequest, IsInRemoteControl,IsInRemoteControlRequest, GetRobotMode, GetRobotModeRequest, IsProgramRunning, IsProgramRunningRequest
from std_srvs.srv import Trigger, TriggerRequest
import time

'''GET THIS BUILD NUMBER FROM USER INPUT'''
build_num = 6


class Pick_and_Place_Program:
    def __init__(self):
        pass

    def start(self):
        total_sub_prog = ['reach_PCB', 'move_to_break_off', 'hold_PCB']
        Program_Communication.check_prog_fail(total_sub_prog)
        pass

    def mid(self):
        # check the status of the previous program, whether that is running or not

        # How many programs we have
        total_sub_prog = ['reach_PCB', 'move_to_break_off', 'hold_PCB']
        Program_Communication.check_prog_fail(total_sub_prog)

    def end(self):
        # check the status of the previous program, whether that is running or not        
        # How many programs we have
        total_sub_prog = ['reach_PCB', 'move_to_break_off', 'hold_PCB']
        Program_Communication.check_prog_fail(total_sub_prog)

        pass


class Dispense_Program:
    def __init__(self):
        self.simulation = Dashboard_Client('load_program', Load, LoadRequest(),'') 
        self.dispense = Dashboard_Client('load_program', Load, LoadRequest(),'d') 
        # ['0','1', '2', '3','4','5','6','7','8', '9', '10', '11','12', '13', '14']
        self.sub_prog_names = list(range(0,15))
        for i in self.sub_prog_names:
            self.sub_prog_names[i] = str(i)
        
    def start(self):
        prog_name = self.sub_prog_names[0]
        self.simulation.load(file_name=prog_name)

    def mid(self):
        ''' loops forever '''     
        # Program_Communication.check_prog_fail(self.total_sub_prog)
        # prog_name = self.sub_prog_names[1]
        # print(self.sub_prog_names[1])
        # self.simulation.load(file_name=prog_name[1])
        for j in range(1, len(self.sub_prog_names)-1):
            # dispense_robot = Dashboard_Client('play', Trigger, TriggerRequest(),'d')
            # pick_and_place_robot = Dashboard_Client('play', Trigger, TriggerRequest(),'p')
            self.simulation.load(file_name = self.sub_prog_names[j])
            # time.sleep(2)

            # self.simulation.play()

            # if self.simulation.program_runing() != True:
            #     self.simulation.play()

            # print(f"starting program: {prog_name[i]}")
            # while self.simulation.program_runing():
            #     # time.sleep(1)
            #     print(f" Program: {prog_name[i]}")
        self.simulation.load(file_name = self.sub_prog_names[-1])
    # def end(self):
    #     prog_name = self.sub_prog_names[-1]
    #     self.simulation.load(file_name=prog_name)


class Dispense_Correction:
    def __init__(self):    
        self.dispense = Dispense_Program()

    def pad_input(self, retry_pad):
        self.dispense.simulation.load(file_name = 'retry')
        self.dispense.simulation.load(file_name = self.dispense.sub_prog_names[retry_pad])

class Program_Communication:
    def __init__(self,build_num):
        self.build_num = build_num

        self.simulation = Dashboard_Client('play', Trigger, TriggerRequest(),'')        
        self.dispense_robot = Dashboard_Client('play', Trigger, TriggerRequest(),'d')
        self.pick_and_place_robot = Dashboard_Client('play', Trigger, TriggerRequest(),'p')

        self.program_running = Dashboard_Client.program_runing()
        self.play = Dashboard_Client.program_runing()

    # def check_program_finished(self):
    #     pass

    def pick_and_place_program_check(self):
        pass

    def dispense_program_check(self):
        pass

    def check_prog_fail(self, program_list):
        '''error testing for robot'''
        # digital output from camera
        failed = True

        # if one of the program had failed, go back to the previous program
        for i in range(0,len(program_list)):
            # load the file name
            Dashboard_Client.load(file_name=program_list[i])
            # if the program is running, then put the program to slee
            while self.program_running:
                time.sleep(1)
            # play program

            # if the first one fail, repeat the first one
            if i ==0 and failed:
                # paste out dried paste
                # reach a safe position 
                # load specific program
                pass
            elif failed:
            # if the remaining fail, repease the i-1 program
                pass
        pass

    def run_dispense(self):
        Dispense_Program.start()

        for i in range(1,len(build_num)-1):
            ''' The middle build range between the 2nd and the 2nd last
                Each i is for each complete movement of the middle build
            '''
            # Run middle program
            Dispense_Program.mid()
        Dispense_Program.end()

    def run_pick_and_place(self):
        Dispense_Program.start()
        for i in range(1,len(build_num)-1):
            Dispense_Program.mid()
        Dispense_Program.end()
        
''' This is to loop through predefine number of program'''
# dispense = Dispense_Program()
# user_input = 3
# dispense.start()
# for i in range(0,user_input):
#     dispense.mid()  

''' Dispensing correction after camera input, determining which pad require touch up'''
dispense_correct = Dispense_Correction()
dispense_correct.pad_input(retry_pad = 10)

# program_list = dispense.sub_prog_names
# simulation = Dashboard_Client('load_program', Load, LoadRequest(),'')    

# ''' individual program load and play test'''
# # simulation.load(file_name=program_list[2])
# # print(program_list[0])

# # simulation.load(file_name=program_list[0])
# # simulation.load(file_name='5')
# # simulation.play()
# # print('starting program')

# '''looping throught the program for testing'''
# for i in range(0,len(program_list)):
#     # load the file name
#     # print(i)
#     # dispense_robot = Dashboard_Client('play', Trigger, TriggerRequest(),'d')
#     # pick_and_place_robot = Dashboard_Client('play', Trigger, TriggerRequest(),'p')
#     simulation.load(file_name=program_list[i])
#     time.sleep(2)
#     simulation.play()

#     if simulation.program_runing() != True:
#         simulation.play()

#     print(f"starting program: {program_list[i]}")
#     while simulation.program_runing():
#         # time.sleep(1)
#         print(f" Program: {program_list[i]}")
    