#!/usr/bin/env python
# SPDX-FileCopyrightText: 2025 Kai Nonaka
# SPDX-License-Identifier: BSD-3-Clause:

from setuptools import find_packages, setup

package_name = 'mypkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='akaja',
    maintainer_email='akajaika@icloud.com',
    description='robosys2024_2',
    license='BSD-3-Clause',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'similality_images = mypkg.similality_images:main',
            'test_listener = mypkg.test_listener:main'
        ],
    },
)
