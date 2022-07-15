#! /usr/bin/env python

import rospy
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint
import random


def my_publisher():
    # control part

    #rospy.init_node('arm_control_python_node')
    control_publisher = rospy.Publisher('/arm_controller/command', JointTrajectory, queue_size=10)
    i=0
    while not i==1000:
        msg = JointTrajectory()
	i=i+1
        msg.header.stamp = rospy.Time.now()
        msg.header.frame_id = ''
        msg.joint_names = ['arm_1_joint', 'arm_2_joint', 'arm_3_joint', 'arm_4_joint', 'arm_5_joint', 'arm_6_joint', 'arm_7_joint']

        point = JointTrajectoryPoint()
        #j1 = 2 * (random.random() - 0.5)  # 0 - 1 -> -0.5 - 0.5
        #j2 = 2 * (random.random() - 0.5)
        #j3 = 2 * (random.random() - 0.5)

        point.positions = [0.67, -0.32, -1.63, 0.85, 1.0, 0.06, 2.07]
        point.velocities = []
        point.accelerations = []
        point.effort = []
        point.time_from_start = rospy.Duration(1)

        msg.points.append(point)

        control_publisher.publish(msg)
        rospy.loginfo(msg)


if __name__ == '__main__':
    rospy.init_node('arm_control_python_node')
    my_publisher()
