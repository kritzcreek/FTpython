import utils
import plot
from face import Face

def analyze(file=""):
  with open(file):
    #skip=2 here denotes removing label and timestamp
    faces = utils.read_faces(file, skip=2)
    
    plot.scatterFacePlot(faces[0])

    
if __name__ == '__main__':
  import argparse

  parser = argparse.ArgumentParser(description='Analyze Facetracking Data from the Kinect.')
  parser.add_argument('file', help='the destination of the Facetracking data file')

  args = parser.parse_args()
  analyze(args.file)