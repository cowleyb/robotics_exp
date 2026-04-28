import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, SetEnvironmentVariable
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import Command
from launch_ros.actions import Node


def generate_launch_description():
    description_path = get_package_share_directory("mentorpi_description")
    gazebo_path = get_package_share_directory("ros_gz_sim")
    sim_path = get_package_share_directory("mentorpi_sim_gazebo")

    xacro_path = os.path.join(sim_path, "urdf", "mentorpi_gz.xacro")
    world_path = os.path.join(sim_path, "worlds", "empty.world")

    robot_description = Command(["xacro ", xacro_path])

    return LaunchDescription(
        [
            SetEnvironmentVariable(
                name="GZ_SIM_RESOURCE_PATH",
                value=os.path.dirname(description_path),
            ),
            IncludeLaunchDescription(
                PythonLaunchDescriptionSource(
                    os.path.join(gazebo_path, "launch", "gz_sim.launch.py")
                ),
                launch_arguments={"gz_args": world_path}.items(),
            ),
            Node(
                package="robot_state_publisher",
                executable="robot_state_publisher",
                name="robot_state_publisher",
                output="screen",
                parameters=[{"robot_description": robot_description}],
            ),
            Node(
                package="ros_gz_sim",
                executable="create",
                arguments=[
                    "-topic",
                    "robot_description",
                    "-name",
                    "mentorpi_a1",
                    "-x",
                    "0.0",
                    "-y",
                    "0.0",
                    "-z",
                    "0.0",
                ],
                output="screen",
            ),
            Node(
                package="ros_gz_bridge",
                executable="parameter_bridge",
                arguments=[
                    "/scan_raw@sensor_msgs/msg/LaserScan[gz.msgs.LaserScan",
                    "/ascamera/camera_publisher/rgb0/image@sensor_msgs/msg/Image[gz.msgs.Image",
                    "/ascamera/camera_publisher/rgb0/camera_info@sensor_msgs/msg/CameraInfo[gz.msgs.CameraInfo",
                ],
                output="screen",
            ),
        ]
    )
