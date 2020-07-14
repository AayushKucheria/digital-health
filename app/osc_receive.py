'''
Getting data from OPENBCI device and storing it in a csv
Run file with params --> --ip='' --port=12345 --option='record --patient='aayush kucheria' --time=180
'''

import argparse
import time
import os
import signal
import sys
import datetime

from pythonosc import dispatcher
from pythonosc import osc_server


# Print received message to console
def print_message(*args):
    try:
        # current = time.time()
        current = str(datetime.datetime.now())
        print("(%f) RECEIVED MESSAGE: %s" % (
            current, ",".join(str(x) for x in args[1:])))  # Time, Channel 1, Channel 2, ..., Channel n

    except ValueError:
        pass


# Clean exit from print mode
def exit_print(signal, frame):
    print("Closing listener")
    sys.exit(0)


# Record received message in text file
def record_to_file(*args):
    textfile.write(str(time.time()) + ",")
    textfile.write(",".join(str(x) for x in args[1:]))
    textfile.write("\n")


# Save recording, clean exit from record mode
def close_file(*args):
    print("\nFILE SAVED")
    textfile.close()
    sys.exit(0)


# connect server
def connect_server():
    server = osc_server.ThreadingOSCUDPServer(
        (args.ip, args.port), dispatcher)
    server.serve_forever()


if __name__ == "__main__":

    messages = []
    # Collect command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip",
                        default="127.0.0.1", help="The ip to listen on")  # Was default="localhost"
    parser.add_argument("--port",
                        type=int, default=12345, help="The port to listen on")
    parser.add_argument("--address",
                        default="/openbci", help="address to listen to")
    parser.add_argument("--option",
                        default="record", help="Record to csv or print to terminal?")
    parser.add_argument("--name",
                        default='test', help="The patient's name", required=True)
    parser.add_argument("--time",
                        default=3, type=int, help="How long to capture data in seconds")
    args = parser.parse_args()

    # Set up necessary parameters from command line
    dispatcher = dispatcher.Dispatcher()
    if args.option == "print":
        dispatcher.map("/openbci", print_message)  # Prints any messages associated with this address
        signal.signal(signal.SIGINT, exit_print)

    elif args.option == "record":
        filename = ("data/" + "emg_" + args.name + "_" + str(time.time()) + ".csv")
        textfile = open(filename, "w")
        # textfile.write("time,address,messages\n")
        print("Recording to %s" % filename)
        dispatcher.map("/openbci", record_to_file)
        signal.signal(signal.SIGINT, close_file)

    # Display server attributes
    print('--------------------')
    print("-- OSC LISTENER -- ")
    print('--------------------')
    print("IP:", args.ip)
    print("PORT:", args.port)
    print("ADDRESS:", args.address)
    print("NAME:", args.name)
    print("TIME:", args.time)
    print('--------------------')
    print("%s option selected" % args.option)

    signal.alarm(args.time)
    connect_server()
