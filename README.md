# obstacle_avoidance
A simple obstacle avoidance ROS project using Turtlebot3 and Gazebo

## Problem:
Use ROS, connected with Gazebo of Turtlebot3, make a controlling program which keeps moving avoiding obstacles in the standard world set.

Under conditions of:
- ROS version is Noetic
- Using Python
- Should be able to be built in the CPU of our side, and should be able to be checked of its movements
- Using move-base

## Pre-requisites
- Python3
- Gazebo
- TurtleBot3
- ROS Noetic

## Installation
1. Copy the attached package (obstacle_avoidance) folder to ~/catkin_ws/src folder
2. Build.
```
cd ~/catkin_ws/
catkin_make
```

## Usage
1. Launch Gazebo Simulation World
```
export TURTLEBOT3_MODEL=burger
roslaunch turtlebot3_gazebo turtlebot3_world.launch
```
2. In a separate terminal window, run obtacle avoidance program
```
rosrun obstacle_avoidance avoid_obstacle.py
```
3. Launch TurtleBot3 simulation
```
export TURTLEBOT3_MODEL=burger
roslaunch turtlebot3_gazebo turtlebot3_simulation.launch
```

## Note
This is implemented on Ubuntu 20.04.3 LTS
