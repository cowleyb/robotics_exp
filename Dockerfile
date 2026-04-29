ARG ROS_DISTRO=jazzy
FROM ros:$ROS_DISTRO

SHELL ["/bin/bash", "-c"]

RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y python3-pip python3-colcon-common-extensions
RUN apt-get install -y ros-$ROS_DISTRO-joint-state-publisher ros-$ROS_DISTRO-robot-state-publisher ros-$ROS_DISTRO-rviz2 ros-$ROS_DISTRO-xacro
RUN apt-get install -y ros-$ROS_DISTRO-ros-gz ros-$ROS_DISTRO-ros-gz-bridge ros-$ROS_DISTRO-ros-gz-sim 
RUN apt-get install -y ros-$ROS_DISTRO-slam-toolbox

WORKDIR /workspace/ros2_ws

RUN echo "source /opt/ros/$ROS_DISTRO/setup.bash" >> /root/.bashrc

RUN cat <<'EOF' > /root/.bash_aliases
alias cb='colcon build --symlink-install'
alias cbs='colcon build --symlink-install && source install/setup.bash'
alias ss='source install/setup.bash'
EOF

RUN echo "if [ -f ~/.bash_aliases ]; then . ~/.bash_aliases; fi" >> /root/.bashrc

CMD ["bash"]
