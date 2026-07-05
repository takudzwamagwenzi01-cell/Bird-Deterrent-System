# Bird Deterrent System

## Overview

This repository contains a complete prototype for an intelligent bird deterrent system designed for agricultural environments. The project combines computer vision, simulation, and robotics concepts to detect birds near crops and provide a foundation for testing deterrent strategies before deployment in the real world.

The system is split into two complementary parts:

- A Python-based vision pipeline for detecting birds from images, video files, and live camera feeds.
- A ROS 2 and Gazebo simulation environment that models a farm field with crop rows, fences, paths, and several bird-deterrent objects.

Together, these components form a development platform for building, testing, and extending bird monitoring and deterrence solutions.

## What the project does

The core idea is simple: use object detection to identify birds or bird-like objects in the environment, then use that information as the basis for warnings, deterrent activation, or further automation. In its current form, the project focuses on the detection side and provides a realistic farm-like simulation environment for evaluating the overall system concept.

The vision module uses YOLOv8 to identify objects in visual input and annotate the results with bounding boxes and confidence scores. The simulation workspace provides a visual test bed where deterrent assets and field layouts can be arranged and explored.

## Main components

### 1. Vision detection module

The detection pipeline lives in the companion project directory and is built around YOLOv8. It can:

- Process single images
- Analyze video files
- Use a webcam or live camera stream
- Save annotated results to disk
- Display detection output in a window for interactive testing

This part of the project is intended as a practical baseline for bird detection and can be expanded to trigger actions such as alarms, sprinkler activation, or robotic responses.

### 2. ROS 2 and Gazebo simulation environment

The ROS 2 workspace provides a simulated agricultural field where different deterrent concepts can be represented in a realistic scene. The world includes:

- Crop plots and crop rows
- Dirt paths and field boundaries
- Fences and perimeter structures
- Deterrent models such as motion sprinklers, reflective spinners, scare banners, and scare posts

This simulation layer makes it easier to prototype the surrounding environment and visualize how deterrents might be arranged in a real farm setting.

### 3. Extensibility and future integration

The project is structured to support future integration between perception and actuation. A natural next step is to connect the detection system to ROS topics or services so that bird detections can trigger hardware actions or simulation events in real time.

## Repository structure

- [bird_deterrent_project](bird_deterrent_project): The computer vision application, including the detection script, dependencies, and sample assets.
- [ros2_ws](ros2_ws): The ROS 2 workspace containing simulation assets, world files, and models.
- [ros2_ws/worlds](ros2_ws/worlds): The Gazebo world definition for the agricultural field simulation.
- [ros2_ws/models](ros2_ws/models): SDF model assets representing field elements and deterrent objects.

## Features

- Real-time or near-real-time bird detection using YOLOv8
- Support for image, video, and live camera input
- Annotated detection output with confidence values
- Farm-like simulation environment for visualization and testing
- Modular structure that can be extended for robotics and automation workflows

## Prerequisites

To work with the project, you will typically need:

- Python 3.8 or newer
- pip and a Python virtual environment
- PyTorch, OpenCV, and Ultralytics for the detection workflow
- A ROS 2 installation and Gazebo support for the simulation environment

## Getting started

### 1. Set up the vision component

From the project directory, create and activate a virtual environment, then install the required Python packages:

```bash
cd bird_deterrent_project
python3 -m venv yolovenv
source yolovenv/bin/activate
pip install -r requirements.txt
```

Run the demo detection script:

```bash
python bird_deterrent.py --demo
```

You can also process a specific image or video file, or use a webcam as the input source.

### 2. Explore the simulation workspace

Open the ROS 2 workspace and load the Gazebo world defined in the simulation assets. The environment is intended as a visual testbed for field layout and deterrent placement.

If ROS 2 and Gazebo are installed on your machine, you can launch the simulation world directly from the workspace with:

```bash
cd /home/bird_deterrent_system/ros2_ws
source /opt/ros/humble/setup.bash
export GAZEBO_MODEL_PATH=$GAZEBO_MODEL_PATH:$(pwd)/models
gazebo worlds/bird_deterrent_field.world
```

This starts the farm-style Gazebo scene with the field, crop rows, paths, fences, and deterrent models included in the workspace. If you are using a different ROS distribution, replace the setup file with the appropriate one for your installation.

## Intended use

This repository is best understood as a research and development prototype. It demonstrates how machine vision and simulation can be combined to create a bird deterrence concept for precision agriculture. It is well suited for experimentation, educational purposes, and further development toward a practical field-ready system.

## Future development ideas

Possible extensions include:

- Publishing detections through ROS topics
- Triggering deterrent actions from detected bird events
- Adding a live camera feed from a robot or drone
- Improving detection accuracy with custom training data
- Integrating real hardware such as speakers, sprinklers, or robotic actuators

## Summary

The Bird Deterrent System is a multi-part project that brings together perception and simulation to address bird intrusion in agricultural settings. It provides a solid starting point for building a more advanced autonomous deterrence platform and serves as a foundation for future robotics and computer vision work.
