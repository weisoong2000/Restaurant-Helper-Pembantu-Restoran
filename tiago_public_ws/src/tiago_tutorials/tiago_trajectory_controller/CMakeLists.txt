cmake_minimum_required(VERSION 2.8.3)
project(tiago_trajectory_controller)

find_package(catkin REQUIRED COMPONENTS
  roscpp
  actionlib
  control_msgs
  trajectory_msgs
)

catkin_package()

include_directories(
  SYSTEM
  ${catkin_INCLUDE_DIRS}
)

add_executable(run_traj_control src/run_traj_control.cpp)
target_link_libraries(run_traj_control ${catkin_LIBRARIES})

add_executable(run_arm src/run_arm.cpp)
target_link_libraries(run_arm ${catkin_LIBRARIES})


### INSTALL ###

install(TARGETS run_traj_control
  ARCHIVE DESTINATION ${CATKIN_PACKAGE_LIB_DESTINATION}
  LIBRARY DESTINATION ${CATKIN_PACKAGE_LIB_DESTINATION}
  RUNTIME DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
