#!usr/bin/env python
'''This code returns the generic service name corresponding to the provided robot name and action name,
    here action is defined as the name of the command that will be sent to the dashboard.

    Note, this is for dashboard service only!!! Other services will be coming up lately
 '''
class Robot:
    def __init__(self):
        # the name of the robot is obtained from the previously set up node name (inside package ur_robot_driver/launch/3_dual.launch)
        # this is the node name/ namespace that is corresponding to each robot
        # /pickAndPlace_robot/ur_hardware_interface/dashboard/

        self.service_general_name = '/ur_hardware_interface/dashboard/'
        self.pp_dashboard = '/pickAndPlace_robot' + self.service_general_name
        self.disp_dashboard = '/dispense_robot' + self.service_general_name
        self.dispense_robot_on = False
        self.pick_robot_on = False

    def name(self, robot_name, srv_name):
        '''The robot name is referring pickAndPlace robot node and dispense robot node
            The srv_name is the name of action in the service that we are trying to call, for example 'power_on' or 'set_IO'
            for the purpose of simplicity, the srv_name is used in dashboard_dual_service
        '''
        if robot_name.lower() == 'p':
            self.dispense_robot_on = False
            self.pick_robot_on = True
            self.service_name = self.pp_dashboard + srv_name
        elif robot_name.lower() == 'd':
            self.dispense_robot_on = True
            self.pick_robot_on = False
            self.service_name =  self.disp_dashboard + srv_name        
        else:
            raise ValueError('The provided robot name does not exist, please enter either "p" or "d" to indcate which robot you are referring to')

        return self.service_name