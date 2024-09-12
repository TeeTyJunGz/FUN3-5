from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import ExecuteProcess, DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration, FindExecutable

def generate_launch_description():
    
    launch_description = LaunchDescription()
    
    # turtle_name_controller = LaunchConfiguration('turtle_name_controller')
    # controller_launch_arg = DeclareLaunchArgument(
    #     'turtle_name_controller',
    #     default_value = 'turtle1'
    # )
    
    # launch_description.add_action(controller_launch_arg)
    
    # turtle_name_crazy = LaunchConfiguration('turtle_name_crazy')
    # crazy_launch_arg = DeclareLaunchArgument(
    #     'turtle_name_crazy',
    #     default_value = 'turtle2'
    # )
    
    # launch_description.add_action(crazy_launch_arg)
    
    # turtlesim_node = Node(
    #     package = 'turtlesim_plus',
    #     namespace = '',
    #     executable = 'turtlesim_plus_node.py',
    #     name = 'turtlesim'
    # )
    # launch_description.add_action(turtlesim_node)
    
    package_name = 'motorsim'
    
    executable_name = ['motorsim_node', 'controller_node', 'encoder_node', 'scheduler_node', 'random_point_node']
    motor_name = ['motor_6551', 'motor_6506', 'motor_6537']
    kp = 0.1
    ki = 0.0
    kd = 0.0
    U_max = 18.0

    for i in range(len(executable_name)):
        if executable_name[i] == 'motorsim_node':
            motor_node = Node(
                package = package_name,
                namespace = '',
                executable = executable_name[i] + '.py',
                name = executable_name[i],
                )
            
            for j in range(len(motor_name)):
                spawnMotor = ExecuteProcess(
                    cmd=[
                        f"ros2 service call /spawn_motor motorsim_interfaces/srv/MotorSpawn \"{{name: '/{motor_name[j]}'}}\""
                        ],
                    shell=True,
                    )
                launch_description.add_action(spawnMotor)
            launch_description.add_action(motor_node)
                
        elif executable_name[i] == 'controller_node':
            for j in range(len(motor_name)):
                controller_node = Node(
                    package = package_name,
                    namespace = motor_name[j],
                    executable = executable_name[i] + '.py',
                    name = executable_name[i],
                    parameters=[
                        { 'Kp': kp },
                        { 'Ki': ki },
                        { 'Kd': kd },
                        { 'U_max': U_max }
                    ]
                    ) 
                launch_description.add_action(controller_node)
                
        elif executable_name[i] == 'encoder_node':
            for j in range(len(motor_name)):
                encoder_node = Node(
                    package = package_name,
                    namespace = motor_name[j],
                    executable = executable_name[i] + '.py',
                    name = executable_name[i],
                    ) 
                launch_description.add_action(encoder_node)
                
        elif executable_name[i] == 'scheduler_node':
            for j in range(len(motor_name)):
                scheduler_node = Node(
                    package = package_name,
                    namespace = motor_name[j],
                    executable = executable_name[i] + '.py',
                    name = executable_name[i],
                    ) 
                launch_description.add_action(scheduler_node)
                
        elif executable_name[i] == 'random_point_node':
            for j in range(len(motor_name)):
                random_point_node = Node(
                    package = package_name,
                    namespace = motor_name[j],
                    executable = executable_name[i] + '.py',
                    name = executable_name[i],
                    ) 
                launch_description.add_action(random_point_node)
                
        else:
            node = Node(
                package = package_name,
                namespace = '',
                executable = executable_name[i] + '.py',
                name = executable_name[i],
            )
            launch_description.add_action(node)
        
    return launch_description