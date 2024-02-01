import os
from glob import glob
from setuptools import setup

package_name = 'demo'

setup(
    name=package_name,
    version='0.0.0',
    # Packages to export
    packages=[package_name],
    # Files we want to install, specifically launch files
    data_files=[
        # Install marker file in the package index
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        # Include our package.xml file
        (os.path.join('share', package_name), ['package.xml']),
        # Include all launch files.
        # (os.path.join('share', package_name, 'launch'), glob(os.path.join('launch', '*.launch.py'))),
        ((os.path.join('share', package_name , 'launch/')),
         glob('launch/*launch.[pxy][yma]*')),                   # add the path for the launch file to make it visible to ros2
    ],
    # This is important as well
    install_requires=['setuptools'],
    zip_safe=True,
    author='Ashutosh',
    author_email='ashutosh19082003@gmail.com',
    maintainer='ashutosh',
    maintainer_email='ashutosh19082003@gmail.com',
    keywords=['foo', 'bar'],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: TODO',
        'Programming Language :: Python',
        'Topic :: Software Development',
    ],
    description='My awesome package.',
    license='TODO',
    # Like the CMakeLists add_executable macro, you can add your python
    # scripts here.
    entry_points={
        'console_scripts': [
            'talkerNode = demo.talker_node:main',
            'listenerNode = demo.listener_node:main'
        ],
    },
)

