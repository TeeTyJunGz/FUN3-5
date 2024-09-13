# **ROS2 Motor Simulation**

This repository provides a **ROS2-based motor simulation** that allows you to set various motor control parameters such as Kp, Ki, Kd. The simulation makes it easy to tune the PID controller to optimize the motor's response.

## **Features**

- **Customizable PID controller:** You can assign your values for **Kp**, **Ki** and **Kd**.
- **Easy integration with ROS2:** Run the simulation using the standard ROS2 launch commands.
- **Real-time motor simulation:** Visualize and simulate motor behavior based on your PID controller settings.
- **Multi-Motor simulation:** Run the simulation using multiple motor that controlled by random position.

## **Prerequisites**

- [ROS2 Humble (or your preferred ROS2 distribution)](https://docs.ros.org/en/humble/Installation.html)
- Colcon build system

## **Installation**

1. Clone this repository:
   ```bash
   git clone https://github.com/TeeTyJunGz/FUN3-5.git
   ```
2. Navigate to the project directory:
   ```bash
   cd FUN3-5
   ```
3. Build the workspace:
   ```bash
   colcon build
   ```
4. Source the workspace:
   ```bash
   source install/setup.bash
   ```
   
## **Usage**
To run the motor simulation:
   ```bash
   ros2 launch motorsim motorsim.launch.py
   ```
   A standard launch will run with 3 motor attached (namespace)

Check position of motor:
   ```bash
   ros2 topic echo <motor_name>/motor_position
   ```
   Replace <motor_name> with your assign motor name in **Launch file**
Example:
   ```bash
   ros2 topic echo motor_6551/motor_position
   ```
