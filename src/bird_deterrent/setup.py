from setuptools import setup

package_name = 'bird_deterrent'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    py_modules=['bird_detector_node', 'bird_motion_node'],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='bird_deterrent_system',
    maintainer_email='bird_deterrent_system@todo.todo',
    description='Bird deterrent ROS 2 package with detector and motion nodes',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'bird_detector_node = bird_detector_node:main',
            'bird_motion_node = bird_motion_node:main',
        ],
    },
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/resource', ['resource/' + package_name]),
        ('lib/' + package_name, [
            'scripts/bird_detector_node',
            'scripts/bird_motion_node',
            'scripts/bird_detector_node_exec.py',
            'scripts/bird_motion_node_exec.py',
        ]),
    ],
)
