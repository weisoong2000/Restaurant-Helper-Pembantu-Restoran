# Pembantu-Restoran

## Author
1. `Wong Wei Soong (A180106)`
2. `Muhammad Afif Imran bin Azman (A181594)`
3. `Iman Farhana binti Rosli (A186144)`

## Instructions
### LAUNCH WORLD
`roslaunch tiago_2dnav_gazebo tiago_navigation.launch public_sim:=true robot:=steel world:=restaurant`

### RUN FIRST GOAL
`rosrun play_motion SendGoal1.py`

### RUN PICK UP STACK
`roslaunch tiago_pick_demo pick_demo.launch`

### START TO PICK OBJECT
`rosservice call /pick_gui`

### NAVIGATE TO DESTINATION, PUT OBJECT INTO DROPBOX AND BACK TO INITIAL POSITION
`rosrun tiago_trajectory_controller initial_pose.py`

### Repeat same step for GOAL2 and GOAL3:
##### `rosrun play_motion SendGoal2.py`
##### `rosrun play_motion SendGoal3.py`

## Note
'Change the path for import destination.py in the initial_pose.py based on your path where the destination.py located in your computer.'
