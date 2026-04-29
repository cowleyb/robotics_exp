import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    nav2_path = get_package_share_directory("nav2_bringup")
    rviz_config_path = os.path.join(nav2_path, "rviz", "nav2_default_view.rviz")

    return LaunchDescription(
        [
            Node(
                package="rviz2",
                executable="rviz2",
                name="rviz2",
                output="screen",
                arguments=["-d", rviz_config_path],
                parameters=[{"use_sim_time": True}],
            ),
        ]
    )
