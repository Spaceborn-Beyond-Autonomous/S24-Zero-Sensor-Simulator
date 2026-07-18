cmake_minimum_required(VERSION 3.8)
project(s24_zero_sensor_simulator)

find_package(ament_cmake REQUIRED)
find_package(ament_cmake_python REQUIRED)

ament_python_install_package(${PROJECT_NAME})

install(
  DIRECTORY
    launch
    config
    docs
  DESTINATION
    share/${PROJECT_NAME}
)

ament_package()