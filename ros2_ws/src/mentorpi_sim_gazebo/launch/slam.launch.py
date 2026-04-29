import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource


def generate_launch_description():
    sim_path = get_package_share_directory("mentorpi_sim_gazebo")
    slam_path = get_package_share_directory("slam_toolbox")

    spawn_launch_path = os.path.join(sim_path, "launch", "spawn.launch.py")
    slam_params_path = os.path.join(
        sim_path,
        "config",
        "slam_toolbox_online_async.yaml",
    )

    return LaunchDescription(
        [
            IncludeLaunchDescription(
                PythonLaunchDescriptionSource(spawn_launch_path),
            ),
            IncludeLaunchDescription(
                PythonLaunchDescriptionSource(
                    os.path.join(slam_path, "launch", "online_async_launch.py")
                ),
                launch_arguments={
                    "slam_params_file": slam_params_path,
                    "use_sim_time": "true",
                }.items(),
            ),
        ]
    )
