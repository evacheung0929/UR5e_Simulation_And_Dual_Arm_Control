#!/usr/bin/env python

'''This is dashboard connection command via port, this can be used to perform robot control, but dashboard_client.py is preferred

    Author: Eva Cheung
    Date: 24/02/2023
'''
import socket
import sys
import time
class Dasboard_Server:
    def __init__(self, robot_ip, port):
        self.robot_ip = robot_ip
        self.port = port
    def connection(self):
        # check if robot is connected/ if there is a controller
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((self.robot_ip, self.port))
        return s
    def power_on_and_brake_release(self):
        content = ["power on","brake release",'robotmode']
        # send the data to the socket, hence send commands
        sock = self.connection()
        sock.send(content[0])
        data = sock.recv(1024)
        # for i in range(len(content)):
        #     sock.send(content[i])
        #     time.sleep(0.5)
        # # .recv = read incoming data on the socket
        #     data = sock.recv(1024)
        #     print(data)
        sock.close()

    def play(self):
        content = ["play"]
        # send the data to the socket, hence send commands
        sock = self.connection()
        for i in range(len(content)):
            sock.send(content[i])
            time.sleep(0.5)
        # .recv = read incoming data on the socket
            data = sock.recv(1024)
            print(data)
        # sock.close()

    def load_program(self, program_name):
        content = program_name
        sock=self.connection()
        sock.send(content)
        time.sleep(0.5)
        data = sock.recv(1024)      

robot_ip = "192.168.1.30"
d = Dasboard_Server(robot_ip, 29999)
d.connection()
d.power_on_and_brake_release()

# d.play()

# d.power_on_and_brake_release()

# robot_ip = "192.168.1.29"

# port = 29999 
# s = socket.socket(socket.AF_INET, socket.s)
# s.connect((robot_ip,port))




        



