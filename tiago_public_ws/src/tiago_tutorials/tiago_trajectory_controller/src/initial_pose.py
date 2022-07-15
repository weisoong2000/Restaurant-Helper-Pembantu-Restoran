#!/usr/bin/env python

import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
import reset_arm as rarm
import control_arm as carm
import control_gripper as gripper
import control_head as head
import sys
sys.path.append('/home/wong/tiago_public_ws/src/play_motion/play_motion/src')
import destination as dest

def movebase_client():
    client = actionlib.SimpleActionClient('move_base', MoveBaseAction)
    client.wait_for_server()

    goal = MoveBaseGoal()
    goal.target_pose.header.frame_id = "map"
    goal.target_pose.header.stamp = rospy.Time.now()
    goal.target_pose.pose.position.x = -0.65
    goal.target_pose.pose.position.y = 0.0
    goal.target_pose.pose.position.z = -0.03
    goal.target_pose.pose.orientation.x = 0.0
    goal.target_pose.pose.orientation.y = 0.0
    goal.target_pose.pose.orientation.z = 0.0
    goal.target_pose.pose.orientation.w = 1.0

    client.send_goal(goal)
    wait = client.wait_for_result()
    if not wait:
        rospy.logerr("Action server not available!")
        rospy.signal_shutdown("Action server not available")
    else:
        return client.get_result()


if __name__ == "__main__":
    rospy.init_node('movebase_client_py')
    dest.movebase_client()
    carm.my_publisher()
    gripper.my_publisher()
    rarm.my_publisher()
    head.my_publisher()
    try:
        #rospy.init_node('movebase_client_py')
        result = movebase_client()
        if result:
            rospy.loginfo("Goal execution done!")
    except rospy.ROSInterruptException:
        rospy.loginfo("Navigation test finished,")

