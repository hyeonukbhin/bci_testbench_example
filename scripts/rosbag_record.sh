#!/bin/bash

rosbag record -b 1024 -o rosbag_bci.bag --split --duration=10m /recognition/image_raw/compressed /test_topic