import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node


def generate_launch_description():
    package_path = get_package_share_directory("mentorpi_description")
    description_launch = os.path.join(package_path, "launch", "description.launch.py")
    rviz_config = os.path.join(package_path, "rviz", "mentorpi.rviz")

    return LaunchDescription(
        [
            IncludeLaunchDescription(
                PythonLaunchDescriptionSource(description_launch),
            ),
            Node(
                package="rviz2",
                executable="rviz2",
                name="rviz2",
                output="screen",
                arguments=["-d", rviz_config],
            ),
        ]
    )

