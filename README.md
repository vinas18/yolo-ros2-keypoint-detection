# yolo-ros2-keypoint-detection
# Keypoint Detection using YOLO and ROS2 in a Simulated Environment

This repository contains the implementation of a ROS2-based perception system
for real-time keypoint (pose) detection using a YOLOv8 pose estimation model.
The project was developed as part of the Advanced Robot Applications module
in an MSc in Artificial Intelligence programme.

## Project Overview
The system integrates a deep learning pose estimation model into a ROS2
perception pipeline. Camera images published by a simulated robot in Gazebo
are processed in real time to detect human keypoints, which are then published
to a dedicated ROS2 topic for further robotic applications.

## System Architecture
- *Subscribed Topic:* /camera/image_raw
- *Processing Pipeline:*
  - ROS2 image message conversion using cv_bridge
  - YOLOv8 pose estimation inference
  - Keypoint extraction
- *Published Topic:* /pose_estimation

## Technologies Used
- ROS2 (Humble)
- Python
- Ultralytics YOLOv8 (Pose Estimation)
- OpenCV
- Gazebo Simulation
- TurtleBot3

## Installation
Clone the repository into your ROS2 workspace:

```bash
cd ~/ros2_ws/src
