# Battery Module

## Purpose

The Battery Module simulates a rechargeable LiPo battery for testing.

It publishes battery information using ROS2.

---

## Published Topic

/battery_state

Message

sensor_msgs/msg/BatteryState

---

## Simulated Parameters

State of Charge (SOC)

Voltage

Current

Power

Temperature

Remaining Time

Battery Status

---

## Battery Status Levels

FULL

GOOD

NORMAL

LOW

CRITICAL

---

## Configuration

Battery parameters are loaded from

config/battery.yaml

---

## Terminal Display

Example

[████████████████████]

SOC : 100 %

Voltage : 16.8 V

Temperature : 25 °C

Status : FULL

---

## Logger

Every update is stored inside

logs/battery.log