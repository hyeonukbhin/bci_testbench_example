#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
import rospy
from std_msgs.msg import String
from signal import signal, SIGINT
from termcolor import colored
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


def cb_output(data):
    recieved_data = data.data

    print('Output Topic Name : {}'.format(colored("/test_topic", 'white', attrs=['bold'])))
    print('Distance : {}'.format(colored(recieved_data, 'white', attrs=['bold'])))


def termination_handler(signal_received, frame):
    print(colored('SIGINT or CTRL-C detected. Exiting gracefully', 'white', attrs=['bold']))
    sys.exit(0)


def main():
    rospy.init_node('output_listener', anonymous=False)
    rospy.Subscriber("/test_topic", String, cb_output)
    rospy.spin()


if __name__ == '__main__':
    signal(SIGINT, termination_handler)

    main()
