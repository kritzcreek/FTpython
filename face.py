import numpy as np

def split_into_dimensions(data):
  dataX = []
  dataY = []
  dataZ = []
  for index, val in enumerate(data):
    if index % 3 == 0:
      dataX.append(val)
    elif index % 3 == 1:
      dataY.append(val)
    elif index % 3 == 2:
      dataZ.append(val)
  return dataX, dataY, dataZ

class Face():
  """ 
  This class represents a collection of Data from the Kinect Facetracking Library
  The input data is expected to be in the following Format:
  [Feature1.X, Feature1.Y, Feature1.Z, Feature2.X, Feature2.Y, Feature2.Z,...]
  """
  def __init__(self, data):
    self.featuresX, self.featuresY, self.featuresZ = split_into_dimensions(data)

  def tuples(self):
    return np.array(list(zip(self.featuresX, self.featuresY, self.featuresZ)))

