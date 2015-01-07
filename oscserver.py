import argparse
import math

from pythonosc import dispatcher
from pythonosc import osc_server
from FTData_pb2 import (FaceTrackFrame, Point)

def print_volume_handler(unused_addr, args, volume):
  print("[{0}] ~ {1}".format(args[0], volume))

def print_compute_handler(unused_addr, args, volume):
  try:
    print("[{0}] ~ {1}".format(args[0], args[1](volume)))
  except ValueError: pass

def recvFtf(unused_addr, args, bytes_ftf):
  ftf = FaceTrackFrame()
  ftf.ParseFromBytes(bytes_ftf)
  print(ftf.label)

if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument("--ip",
      default="127.0.0.1", help="The ip to listen on")
  parser.add_argument("--port",
      type=int, default=5005, help="The port to listen on")
  args = parser.parse_args()

  dispatcher = dispatcher.Dispatcher()
  dispatcher.map("/kinect/face", recvFtf)
  dispatcher.map("/debug", print)
  dispatcher.map("/logvolume", print_compute_handler, "Log volume", math.log)
  #dispatcher.set_default_handler(print)

  server = osc_server.ThreadingOSCUDPServer(
      (args.ip, args.port), dispatcher)
  print("Serving on {}".format(server.server_address))
  server.serve_forever()