import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import GroupAction, IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import SetRemap


def generate_launch_description():
    sim_path = get_package_share_directory("mentorpi_sim_gazebo")
    nav2_path = get_package_share_directory("nav2_bringup")

    slam_launch_path = os.path.join(sim_path, "launch", "slam.launch.py")
    nav2_params_path = os.path.join(sim_path, "config", "nav2_params.yaml")

    return LaunchDescription(
        [
            IncludeLaunchDescription(
                PythonLaunchDescriptionSource(slam_launch_path),
            ),
            GroupAction(
                [
                    SetRemap(src="/cmd_vel", dst="/controller/cmd_vel"),
                    SetRemap(src="cmd_vel", dst="/controller/cmd_vel"),
                    IncludeLaunchDescription(
                        PythonLaunchDescriptionSource(
                            os.path.join(nav2_path, "launch", "navigation_launch.py")
                        ),
                        launch_arguments={
                            "params_file": nav2_params_path,
                            "use_sim_time": "true",
                            "autostart": "true",
                        }.items(),
                    ),
                ]
            ),
        ]
    )
