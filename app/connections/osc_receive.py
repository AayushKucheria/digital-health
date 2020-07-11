import argparse
import time
import atexit
import os
import signal
import sys
import multiprocessing

from pythonosc import dispatcher
from pythonosc import osc_server

from csv import reader


# Print received message to console
def print_message(*args):
    try:
        current = time.time()
        # print("(%f) RECEIVED MESSAGE: %s %s" % (current, args[0], ",".join(str(x) for x in args[1:])))  # Prints the address
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
                        default="localhost", help="The ip to listen on")
    parser.add_argument("--port",
                        type=int, default=12345, help="The port to listen on")
    parser.add_argument("--address",
                        default="/openbci", help="address to listen to")
    parser.add_argument("--option",
                        default="print", help="Debugger option")
    parser.add_argument("--patient",
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
        i = 0
        while os.path.exists(("data/" + args.patient + "%s.csv") % i):
            i += 1
        filename = ("data/" + args.patient + "%i.csv") % i
        textfile = open(filename, "w")
        textfile.write("time,address,messages\n")
        textfile.write("-------------------------\n")
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
    print("NAME:", args.patient)
    print("TIME:", args.time)
    print('--------------------')
    print("%s option selected" % args.option)

    signal.alarm(args.time)
    connect_server()


