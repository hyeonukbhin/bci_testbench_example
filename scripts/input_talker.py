#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
from termcolor import colored
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Transform
from signal import signal, SIGINT
import sys
import numpy as np


reload(sys)
sys.setdefaultencoding('utf-8')


def cb_terminal_input(input_distance):

    list_distance = np.sort(np.arange(0, input_distance + 1, 1))[::-1]
    for val_distance in list_distance:
        current_time = rospy.get_rostime()
        timestamp = '%i.%i' % (current_time.secs, current_time.nsecs)
        pub_input.publish('{}'.format(val_distance))
        print('Timestamp : {}, Distance : {}'.format(colored(timestamp, 'white', attrs=['bold']), colored(val_distance, 'white', attrs=['bold'])))
        rospy.sleep(0.5)

    print(colored('Press Enter to continue', 'white', attrs=['bold']))
    end_flag = raw_input('')


def terminal_loop():
    while True:
        print('=============================================')
        print('입력한 숫자로부터 0.5초마다 1씩 감소되는 토픽 발행됩니다')
        input_distance = int(raw_input('-> '))
        cb_terminal_input(input_distance)


def termination_handler(signal_received, frame):
    print(colored('SIGINT or CTRL-C detected. Exiting gracefully', 'white', attrs=['bold']))
    sys.exit(0)


def main():
    global pub_input

    rospy.init_node('input_talker', anonymous=False)
    pub_input = rospy.Publisher('/test_topic', String, queue_size=100)
    terminal_loop()
    rospy.spin()


if __name__ == '__main__':
    signal(SIGINT, termination_handler)
    main()
