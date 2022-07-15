#! /usr/bin/env python

import rospy
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint


def my_publisher():
    # control part

    control_publisher = rospy.Publisher('/head_controller/command', JointTrajectory, queue_size=10)
    i=0
    while not i==500:
        msg = JointTrajectory()
	i=i+1
        msg.header.stamp = rospy.Time.now()
        msg.header.frame_id = ''
        msg.joint_names = ['head_1_joint', 'head_2_joint']

        point = JointTrajectoryPoint()

        point.positions = [0.00, -0.01]
        point.velocities = []
        point.accelerations = []
        point.effort = []
        point.time_from_start = rospy.Duration(1)

        msg.points.append(point)

        control_publisher.publish(msg)
        rospy.loginfo(msg)


if __name__ == '__main__':
    rospy.init_node('head_control_python_node')
    my_publisher()
