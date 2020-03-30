## IMAGEZMQ CLIENT ##
# This client allows realtime video transmission with no video broker
# and high performance to a server. PiCamera supported by uncommenting
# line 34 and commenting line 35.
# Modified from: https://www.pyimagesearch.com/2019/04/15/live-video-streaming-over-network-with-opencv-and-imagezmq/

# USAGE
# python client.py --server-ip SERVER_IP

# import the necessary packages
from imutils.video import VideoStream
import imagezmq
import argparse
import socket
import time
import imutils

OUTPUT_VIDEO_WIDTH = 320 # Video resizing for performance.

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-s", "--server-ip", required=True,
	help="ip address of the server to which the client will connect")
args = vars(ap.parse_args())

# initialize the ImageSender object with the socket address of the
# server
sender = imagezmq.ImageSender(connect_to="tcp://{}:5555".format(
	args["server_ip"]))

# get the host name, initialize the video stream, and allow the
# camera sensor to warmup
rpiName = socket.gethostname()
#vs = VideoStream(usePiCamera=True).start()
vs = VideoStream(src=0).start()
time.sleep(2.0)
 
while True:
	# read the frame from the camera and send it to the server
	frame = vs.read()
	frame = imutils.resize(frame, width=OUTPUT_VIDEO_WIDTH) # Added resize for performance
	sender.send_image(rpiName, frame)
