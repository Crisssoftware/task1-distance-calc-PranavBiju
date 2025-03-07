# TurtleBot3 Service Task
Your task is to create a ROS2 service that controls a TurtleBot3 in simulation. The service should accept an integer argument representing the number of seconds the robot should move forward at a constant speed of **1 m/s**.

### Example:
- If the service is called with the argument `5`, the TurtleBot3 should move forward at **1 m/s** for **5 seconds** before stopping.
- If the service is called with `10`, the robot should move forward for **10 seconds** and then stop.
- ```bash
  ros2 run <package_name> <node_name> <no. of seconds>
  ```

By completing this task, you will:
- Learn how to launch a TurtleBot3 simulation in a 3D environment.
- Understand how to create a ROS2 service.
- Implement a simple motion control service.

## Prerequisites
To complete this task, you need to install TurtleBot3 in ROS2. Follow the installation guides based on your ROS2 version:

If you have already installed ROS, please skip and continue with the installation of Gazebo(Simulator)
- **ROS2 Foxy**: [TurtleBot3 Installation for Foxy](http://blog.utem.edu.my/wira_yugi/ros2-and-turtlebot3-installation/)
- **ROS2 Humble**: [TurtleBot3 Installation for Humble](https://emanual.robotis.com/docs/en/platform/turtlebot3/quick-start/#ros-2-humble)
- **ROS2 Jazzy**: [TurtleBot3 Installation for Jazzy](https://docs.google.com/document/d/19ObQR4qn6_gd6mIFPtyNoy-2SDMFzImgR2hkvHJMCIU/edit?usp=sharing)

## Reference Documentation
- [ROS2 Services](https://docs.ros.org/en/foxy/Tutorials/Beginner-Client-Libraries/Writing-A-Simple-Py-Service-And-Client.html)
- [TurtleBot3 Official Documentation](https://emanual.robotis.com/docs/en/platform/turtlebot3/overview/)

## Additional Resources  
You are encouraged to use external resources to understand the task better:  
- **YouTube**: Feel free to watch videos explaining ROS 2 services and TurtleBot3 simulations.  
- **AI Tools**: You can use AI tools to clarify concepts, but **copying code directly from AI-generated responses is not allowed**. Trust me, we know when a code is AI-generated.

### ⚠️ Important Note  
You will be **asked extensively** about how your code works during the interview. Make sure you fully understand your implementation and can explain it in detail.

## Submission
Once you have completed the task, submit the python file(s) for the node(s) and a video of turtlebot moving by giving it a terminal command for a specific set of time.

