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

