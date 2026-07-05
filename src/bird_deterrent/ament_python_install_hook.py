from setuptools import setup

setup(
    name='bird-deterrent',
    version='0.0.0',
    py_modules=['bird_detector_node', 'bird_motion_node'],
    packages=['bird_deterrent'],
    install_requires=['setuptools'],
    entry_points={
        'console_scripts': [
            'bird_detector_node = bird_detector_node:main',
            'bird_motion_node = bird_motion_node:main',
        ],
    },
)
