from setuptools import setup, find_packages
from glob import glob
import os

package_name = "s24_zero_sensor_simulator"

setup(
    name=package_name,
    version="0.0.1",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    include_package_data=True,
    install_requires=[
        "setuptools",
        "PyYAML",
        "numpy",
    ],
    zip_safe=True,
    maintainer="Chetanya Barodiya",
    maintainer_email="chetanyabarodiya@gmail.com",
    description="S24 Zero Sensor Simulator",
    license="MIT",
    tests_require=["pytest"],
    entry_points={
        "console_scripts": [
            "battery_node=s24_zero_sensor_simulator.battery.battery_node:main",
        ],
    },
    
    data_files=[
    (
        'share/ament_index/resource_index/packages',
        ['resource/s24_zero_sensor_simulator'],
    ),
    (
        'share/' + package_name,
        ['package.xml'],
    ),
    (
        os.path.join('share', package_name, 'launch'),
        glob('launch/*.py'),
    ),
    (
        os.path.join('share', package_name, 'config'),
        glob('config/*.yaml'),
    ),
    (
        os.path.join('share', package_name, 'docs'),
        glob('docs/*.md'),
    ),
    ],
)