# S24 - Zero Sensor Simulator

## Overview

The **S24 - Zero Sensor Simulator** is a Layer-1 infrastructure module developed to provide dummy sensor interfaces for software bring-up, integration testing, and Continuous Integration (CI) workflows.

The simulator enables higher-level software components—including the Control Stack, Autopilot, Telemetry Pipeline, and Mission Software—to initialize and operate without requiring physical hardware during the early stages of development.

## Features

* Dummy Battery Interface
* Extensible sensor simulation architecture
* Software bring-up support
* Continuous Integration (CI) testing support
* Modular C++ design for future sensor expansion

## Current Modules

### Battery Simulator

The Battery Simulator provides baseline battery telemetry using predefined values for software validation and system initialization.

Available metrics:

* Voltage
* State of Charge (SoC)
* Temperature

These outputs allow dependent software modules to detect and interact with a simulated battery interface during development and testing.

## Project Structure

```text
S24-Zero-Sensor-Simulator/
│
├── battery/
│   ├── BatterySimulator.hpp
│   └── BatterySimulator.cpp
│
├── logger/
│   ├── Logger.hpp
│   └── Logger.cpp
│
├── logs/
│
├── main.cpp
├── README.md
└── .gitignore
```

## Build

```bash
g++ main.cpp battery/BatterySimulator.cpp logger/Logger.cpp -o battery_sim
```

## Run

```bash
./battery_sim
```

## Example Output

```text
[2026-07-13 19:52:58] Battery : Battery initialized successfully.
Battery initialized successfully.
Voltage: 12.6 V
State of Charge: 100 %
Temperature: 25 C
```

## Repository Guidelines

* Follow the established project structure.
* Keep modules independent and reusable.
* Write clear and maintainable C++ code.
* Test changes before creating a pull request.
* Use descriptive commit messages following the project conventions.

## License

This repository is maintained as part of the Spaceborn autonomous systems development program. Licensing and distribution are governed by the project maintainers.

