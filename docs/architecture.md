# S24 Zero Sensor Simulator Architecture

## Overview

The S24 Zero Sensor Simulator provides dummy sensor data for software
development without requiring physical hardware.

Each sensor is an independent ROS2 module.

---

## Architecture

                    Mission Software
                           │
                           ▼
                  Telemetry Pipeline
                           │
                           ▼
                    Validation Logger
                           │
                           ▼
                      ROS2 Topics
                           │
                           ▼
                   HAL (Hardware Layer)
                           │
        ---------------------------------------
        │        │        │        │          │
        ▼        ▼        ▼        ▼          ▼
       IMU      GPS     LiDAR    Camera    Battery

---

## Battery Module

The Battery Module consists of

Battery Node

Battery Model

Battery State

Validation Logger

Terminal Display

Configuration Loader

---

## Data Flow

battery.yaml

↓

Battery Model

↓

Battery State

↓

ROS2 Publisher

↓

Display

↓

Validation Logger