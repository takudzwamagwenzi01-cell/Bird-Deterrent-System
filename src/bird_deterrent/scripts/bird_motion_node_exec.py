#!/usr/bin/env python3
import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))
INSTALL_PREFIX = os.path.dirname(os.path.dirname(os.path.dirname(SCRIPT_DIR)))
EXECUTABLE = os.path.join(INSTALL_PREFIX, 'bin', 'bird_motion_node')

if __name__ == '__main__':
    os.execv(EXECUTABLE, [EXECUTABLE] + sys.argv[1:])
