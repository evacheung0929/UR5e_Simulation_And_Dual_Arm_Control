# UR5_ROS_Simulation_to_Dual_Arm_Control
This repository summarises my learning of Universal Robot from simulation to actual robot connection using ROS, Dashboard and ur_rtde. It's a working process, so stay tunned!

#### **Goal**: UR5e Pick and place simulation + real-robot motion planning with screwdriver & customised Airpick.
#### **Progress**: xml file saved in a desireable format that can be integrated with Factory Logix after robot movement finished

ROS Distro: Melodic (Ubuntu 18.04 LTS)
Polyscope version: 5.13.0
UR packages: [UR_ROS_Driver](https://github.com/UniversalRobots/Universal_Robots_ROS_Driver), as the industrial robot package will not support e-series 5.XX
- for usage of how to use the ur_robot_driver, look at [Tutorial](https://github.com/UniversalRobots/Universal_Robots_ROS_Driver/blob/master/ur_robot_driver/doc/usage_example.md)

---
## Rviz/Gazebo
**BOLD TEXT HERE**

- [x] Use Rviz for motion planning purposes, demonstrating the robot's perception of the world (what the robot think it's happening)
- [] Use Gazebo visualise the reality of what is happening

---
Installing Rvis with the UR5 Robot, assumed a prefred ROS distribution is already installed
`$ sudo apt-get install ros-$ROS_DISTRO-rviz`

Install ROS packages that publis the robot joint state:
``` sh
$ sudo apt-get install ros-$ROS_DISTRO-joint-state-publisher-gui
```
In order to tell Rviz what the robot looks like, install universal-robot pakage from the [ROS industrial](http://wiki.ros.org/universal_robot/Tutorials/Getting%20Started%20with%20a%20Universal%20Robot%20and%20ROS-Industrial) project
```js
~/catkin_ws/src$ git clone -b $ROS_DISTRO-devel https://github.com/ros-industrial/universal_robot.git
```

```html
<html><html>
```

---ould not have any m
problems that I had run into with Ubuntu

1. sudo apt update fetch problem
```
W: Failed to fetch http://gb.archive.ubuntu.com/ubuntu/dists/bionic/InRelease  Could not resolve ‘gb.archive.ubuntu.com’
W: Failed to fetch http://gb.archive.ubuntu.com/ubuntu/dists/bionic-updates/InRelease  Could not resolve ‘gb.archive.ubuntu.com’
W: Failed to fetch http://gb.archive.ubuntu.com/ubuntu/dists/bionic-backports/InRelease  Could not resolve ‘gb.archive.ubuntu.com’
W: Failed to fetch http://security.ubuntu.com/ubuntu/dists/bionic-security/InRelease  Could not resolve ‘security.ubuntu.com’
W: Some index files failed to download. They have been ignored, or old ones used instead.
```
solved by

```
sudo apt clean
sudo apt update
```


### Pre-resiquite
CAD files of the end-effectors are correctly provided

### URDF

**explain how to create a urdf file with customised end-effectors
- xcaro, urdf, srdf illustrated, customed & explained

## URSim setup
In order to test out the ur_robot_driver package as mentioned above, connection to a real/simulated robot is necessary. This is where URSim comes in.

Download the corresponding URSim from the [official website](https://www.universal-robots.com/download/software-e-series/simulator-non-linux/offline-simulator-e-series-ur-sim-for-non-linux-5120/). Follow the steps
- Virtual Machine maybe necessary. This project used Virtual box & 7zip (extraction)
- if ran into vagrant shared folder problem, go to the VM setting & delete the shared folder, followed by reboot

Set up the network as following the providd [Tutorial](https://github.com/UniversalRobots/Universal_Robots_ROS_Driver/blob/master/ur_robot_driver/doc/usage_example.md)

## Connection with URSim (VM) to ROS (VM)
configure both network to Bridge
get the ip addresss of each using 'ifconfig'

- scan the ports avaliable on the URSim
```
# if nmap is not install
sudo apt install nmap

# scan the network ports
nmap <custom_ip>

# scan for networks, but more thorough
nmap <custom_ip> -p-

>>>
Starting Nmap 7.60 ( https://nmap.org ) at 2023-01-16 14:46 GMT
Nmap scan report for ursim (192.168.1.33)
Host is up (0.00029s latency).
Not shown: 65523 closed ports
PORT      STATE SERVICE
22/tcp    open  ssh
502/tcp   open  mbap
29919/tcp open  unknown
29999/tcp open  bingbang
30001/tcp open  pago-services1
30002/tcp open  pago-services2
30003/tcp open  amicon-fpsu-ra
30004/tcp open  amicon-fpsu-s
30011/tcp open  unknown
30012/tcp open  unknown
30013/tcp open  unknown
30020/tcp open  unknown

Nmap done: 1 IP address (1 host up) scanned in 3.67 seconds
```

In order to connect to the desire port via terminal
```
netcat <custom_ip> <port>
```

type in command 'play' to start playing the program
type in command 'stop' to stop playing the program

### URCap file
Make sure to have installed all the [extensions](https://www.virtualbox.org/wiki/Download_Old_Builds_6_1) for your Virtual Machine in order for it to recognise USB devices
Install .uRcap file from official website
Follow [official tutorial for URCap & URSim](https://dof.robotiq.com/discussion/204/how-to-install-robotiq-s-urcaps-on-ursim) and [External Control setup](https://github.com/UniversalRobots/Universal_Robots_ROS_Driver/blob/master/ur_robot_driver/doc/install_urcap_e_series.md) to get .urcap file to work in URSim

Make sure to change the default Host IP from URCap to the device that will be running ROS
Make sure ROS and URSim are on the same network
192.168.X.XX (ROS)
192.168.X.XX (URSim)
## Connection with the real robot to PC
### network setup
**Physical connection**
* phycial ethernet connection, enable remote control in robot setting

**Window host**
* Edit the IP address of the ethernet in "Network & Internet"
* ```ipconfig``` in window terminal should be able to show the ipv4 address, subnet mask etc, manually type in this information into the 'static address' within the robot  
* IPv4 address should be on the same network as the robot with last digit differences: 192.168.1.6
* Subnet mask sets the network format: 255.255.255.0
*  IPv4 gateway sets the universal network (like WiFi) for the communication: 192.168.1.1
*  The DNS will be obtained from the robot in the next step. Manually type it in after obtaining the info.

**Virtual Box**
* Choose the VM that will be running ROS on virtual box
  1) Go to _File_ ---> Make sure the Host Network Manager is empty otherwise the network limits what the VM network can see (VM-A can only see VM-B but cannot see the ethernet)
  2) Go to VM _setting_ --> _Network_ --> _Adapter_, set one of the apater to be _**"Bridge Adapter"**_, with _**Name:<ethernet_name>**_. The ethernet name can be obtained from window host _ethernet description_ in "Network & Internet"
  3) Run the virtual machine, within the virtual machine go to _Device_ --> _Network_, unselect the previous network adaptor that was being used for URSim, and choose the one with the ethernet connection
    ---
**Network setups are all completed!**
 
 ports connection
 
 * Check avaliable ports
    * ```nmap <ip address> -p-```
    * 
        * Sub-nested bullet etc
  * Bullet list item 2
 #### If you want ssh connection
1) ssh connection; the defualt username = root, password = easybot
  i) using MobaX: ssh ---> start new session ---> host name = ipv4 address, password = easybot
  ii) using terminal >> ssh ip_address
  >> enter password
4) 
---
## Digital I/O in remote control
**How to assign IO to ur command script?

* Bullet list
    * Nested bullet
        * Sub-nested bullet etc
* Bullet list item 2
* 
[put the robot in free drive mode using external program](https://forum.universal-robots.com/t/use-digital-input-mapped-to-freedrive-in-remote-mode/2944)


[ros-planning](https://github.com/ros-planning/moveit_tutorials/tree/melodic-devel) with moveit

