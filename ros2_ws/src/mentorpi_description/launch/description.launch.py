import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.substitutions import Command
from launch_ros.actions import Node


def generate_launch_description():
    package_path = get_package_share_directory("mentorpi_description")
    xacro_path = os.path.join(package_path, "urdf", "mentorpi.xacro")

    robot_description = Command(["xacro ", xacro_path])

    return LaunchDescription(
        [
            Node(
                package="robot_state_publisher",
                executable="robot_state_publisher",
                name="robot_state_publisher",
                output="screen",
                parameters=[{"robot_description": robot_description}],
            )
        ]
    )
