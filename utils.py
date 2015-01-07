import numpy as np
from face import Face

def read_faces(file_path, skip=0):
  return [Face(face) for face in read_file(file_path, skip=skip)]

def read_file(file_path, skip=0):
  collect = []
  with open(file_path) as f:
    f.readline()
    for line in f:
      line.strip()
      splitted = line.split()
      converted = [float(x) for x in splitted[skip:]]
      collect.append(converted)
    return np.array(collect)