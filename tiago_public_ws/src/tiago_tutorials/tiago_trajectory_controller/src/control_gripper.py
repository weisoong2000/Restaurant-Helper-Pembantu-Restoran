#! /usr/bin/env python

import rospy
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint

def my_publisher():
    # control part

    #rospy.init_node('gripper_control_python_node')
    control_publisher = rospy.Publisher('/gripper_controller/command', JointTrajectory, queue_size=10)
    i=0
    while not i==1000:
        msg = JointTrajectory()
	i=i+1
        msg.header.stamp = rospy.Time.now()
        msg.header.frame_id = ''
        msg.joint_names = ['gripper_left_finger_joint', 'gripper_right_finger_joint']

        point = JointTrajectoryPoint()

        point.positions = [0.04, 0.04]
        point.velocities = []
        point.accelerations = []
        point.effort = []
        point.time_from_start = rospy.Duration(1)

        msg.points.append(point)

        control_publisher.publish(msg)
        rospy.loginfo(msg)


if __name__ == '__main__':
    rospy.init_node('gripper_control_python_node')
    my_publisher()
