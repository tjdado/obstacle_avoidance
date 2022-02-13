#! /usr/bin/env python

import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

def callback(msg):
	# For checking purposes only
	print('===========================================================')
	print('Range value of front laser:		{}'.format(msg.ranges[0]))
	print('Range value of 45deg left laser:		{}'.format(msg.ranges[45]))
	print('Range value at 45deg right laser:	{}'.format(msg.ranges[315]))
	print('===========================================================')
	
	# Check if there is an obstacle in front and 45 degrees left and right
	if msg.ranges[0] > 0.5 and msg.ranges[45] > 0.5 and msg.ranges[315] > 0.5:
		move.linear.x = 0.5	# go forward
		move.angular.z = 0.0	# do not rotate
	else:
		move.linear.x = 0.0	# stop
		move.angular.z = 0.5	# rotate counter-clockwise
		
		# After rotation, check again if there is an obstacle in front and 45 degrees left and right
		if msg.ranges[0] > 0.5 and msg.ranges[45] > 0.5 and msg.ranges[315] > 0.5:
		   	move.linear.x = 0.5	# go forward
		   	move.angular.z = 0.0	# do not rotate
		   				
	pub.publish(move)	# publish the move object

rospy.init_node('obstacle_avoidance')
move = Twist()
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)		# Publishes 'move' object
sub = rospy.Subscriber('/scan', LaserScan, callback)		# Subscribes to 'scan' topic and gets laser data

rospy.spin()
