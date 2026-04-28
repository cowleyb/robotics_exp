ARG ROS_DISTRO=jazzy
FROM ros:$ROS_DISTRO

SHELL ["/bin/bash", "-c"]

RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y python3-pip
RUN apt-get install -y python3-colcon-common-extensions
RUN apt-get install -y ros-$ROS_DISTRO-joint-state-publisher ros-$ROS_DISTRO-robot-state-publisher ros-$ROS_DISTRO-rviz2 ros-$ROS_DISTRO-xacro

WORKDIR /workspace/ros2_ws

CMD ["bash"]
