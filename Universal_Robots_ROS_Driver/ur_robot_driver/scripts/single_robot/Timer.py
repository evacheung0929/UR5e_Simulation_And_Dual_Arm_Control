import timeit
import time
import rospy
from std_srvs.srv import TriggerRequest
class Time_Out_Check:
    def __init__(self):
        self.start_time = timeit.default_timer()
        self.duration = timeit.default_timer() - self.start_time
        self.time_out_limit = 10000

    def time_out(self, result, Msg_Request_Name):
        while (result.success == False) and (self.time_out_limit > self.duration):
            self.duration = timeit.default_timer()
            time.sleep(5)
            request = Msg_Request_Name

            # raise SystemError(result)
            print('Switch to Remote control and re-initiate the controller ')
            raise SystemError(result)
            
        
    # def dashboard_srv(self, result, Request_Srv):
    #     while result.success == False and self.time_out_limit > self.duration:
    #         # print(result.answer)
    #         # print('============')
    #         self.duration = timeit.default_timer()
    #         request = Request_Srv
    #         raise SystemError(result.answer)