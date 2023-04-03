# This folder contain all the python script for the dual robot communication.
## Before running the script, please make sure the robot configuration is correctly launched & setup. When running dual robots, _3_dual.launch_ should be launched. MAKE SURE the robot ip address has changed to match your own desireable robot in 1_pp_robot_bringup.launch and 2_d_robot_bringup.launch
folder path: **src/Universal_Robots_ROS_Driver/ur_robot_driver/launch**

---

There are many ways for dual robot commmunication. Here we demonstrate 2 ways
1. IO
2. Robot program status

---

script summary <to be completed>
Io_state_Check.py: 
Robot_name.py: provide the rosservice name of the selected robot. name 'p' stands for robot pick and place, name 'd' stands for dispensing robot 
Timer.py
dashboard_dual_service.py
dispense_listen.py
dual_IO.py
simplified_dual_move_d.py
simplified_dual_move_p.py

xml_testing.py
dispense_robot_io_pub
