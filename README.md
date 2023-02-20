# UR5_ROS_Simulation
This repository summarises my learning of Universal Robot from simulation to actual robot connection using ROS, Dashboard and ur_rtde
## Rviz 
**BOLD TEXT HERE**

_ITALIC TEXT_
*ITALIC TEXT 2*

~~STRIKE THROUGH~~
1. 
2. hah
3. Lst

* Item 1
* Item 2

- [x] TODO ITEM 2
- [] TODO ITEMM 2

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



## README

This is a testing project for UR5e Pick and place simulation + real-robot motion planning with screwdriver & customised epick.
ROS Distro: Melodic (Ubuntu 18.04 LTS)
Polyscope version: 5.12.0
UR packages: [UR_ROS_Driver](https://github.com/UniversalRobots/Universal_Robots_ROS_Driver), as the industrial robot package will not support e-series 5.XX
- for usage of how to use the ur_robot_driver, look at [Tutorial](https://github.com/UniversalRobots/Universal_Robots_ROS_Driver/blob/master/ur_robot_driver/doc/usage_example.md)

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
  1) phycial ethernet connection, enable remote control
  2) In windows host, Edit the IP address of the ethernet in 'Network & Internet'
      i) IPv4 address should be on the same network as the robot with last digit differences: 192.168.1.6
      ii) Subnet mask sets the network format: 255.255.255.0
      iii) IPv4 gateway sets the universal network (like WiFi) for the communication: 192.168.1.1
      iv) The DNS will be obtained from the robot in the next step. Manually type it in after obtaining the info.
  2) Go to the UR teach pendant, manually change the network setting (static) to be on the same network of the above
    1) IPv4 = 192.168.5
    2) Identical subnet mask
              2. Which is numbered
          2. Which is numbered
          
          
  3) Choose the VM that'll be running ROS on Virtual Box --> File --> Make sure the Host Network Manager is empty otherwise the network limits what it can see (VM.a can only see VM.b but not the ethernet)
    ii) Go to network setting of the ROS VM, Enable Network Adapter  --> 'Bridge Adapter' --> 'Name' = ethernet connection name, which can be obtained from 'Network & Internet' --> ethernet --> Description (in the window host)
    ii) subnet mask: 255255.255.0
    iii) gateway: 192.168.1.1, universally, this last digit has to be 1 for gateway, think of it as an auto-recognition of wifi box
    
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

## Digital I/O in remote control
**How to assign IO to ur command script?

* Bullet list
    * Nested bullet
        * Sub-nested bullet etc
* Bullet list item 2
* 
[put the robot in free drive mode using external program](https://forum.universal-robots.com/t/use-digital-input-mapped-to-freedrive-in-remote-mode/2944)


[ros-planning](https://github.com/ros-planning/moveit_tutorials/tree/melodic-devel) with moveit


# How to start this project
