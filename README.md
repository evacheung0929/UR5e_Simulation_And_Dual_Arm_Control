# UR5_ROS_Simulation
The foundation of warehouse automation

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

## Digital I/O in remote control
**How to assign IO to ur command script?

[put the robot in free drive mode using external program](https://forum.universal-robots.com/t/use-digital-input-mapped-to-freedrive-in-remote-mode/2944)


[ros-planning](https://github.com/ros-planning/moveit_tutorials/tree/melodic-devel) with moveit


# How to start this project
