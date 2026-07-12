# S24 - Zero Sensor Simulator

## Overview

The **S24 - Zero Sensor Simulator** is a Layer-1 infrastructure module designed to provide dummy sensor interfaces for early software bring-up, testing, and Continuous Integration (CI).

This simulator allows higher-level software such as the Autopilot, Telemetry Pipeline, and Mission Software to boot successfully without requiring real hardware sensors.

## Current Module

### Battery Simulator

The Battery Simulator provides baseline battery information using fixed dummy values.

Current outputs:

* Voltage
* State of Charge (SoC)
* Temperature

These values allow downstream software to detect a valid battery interface during initialization.

## Current Status

* ✅ Battery Simulator implemented
* ✅ Dummy battery metrics available
* ⏳ Logging module (In Progress)
* ⏳ Bring-up validation logs
* ⏳ Documentation
* ⏳ CI integration

## Project Structure

```text
S24-Zero-Sensor-Simulator/
│
├── battery/
│   ├── BatterySimulator.hpp
│   └── BatterySimulator.cpp
│
├── main.cpp
├──.gitignore
└── README.md
```

## Build

```bash
g++ main.cpp battery/BatterySimulator.cpp -o battery_sim
```

Run

```bash
./battery_sim
```

## Expected Output

```text
Battery initialized successfully.
Voltage: 12.6 V
State of Charge: 100 %
Temperature: 25 C
```

## Sprint Progress

Day 1 ✔ Completed

* Dummy Battery Interface
* Baseline Voltage
* Baseline State of Charge (SoC)
* Baseline Temperature

Future sprint tasks will include the logging engine, validation logs, documentation, and CI integration.
