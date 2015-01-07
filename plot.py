import numpy as np
import matplotlib.pylab as pl
import matplotlib.pyplot as plt

def scatterFacePlot(face):
  xs, ys, zs = np.transpose(face.tuples())
  from mpl_toolkits.mplot3d import Axes3D
  fig = plt.figure()
  ax = fig.add_subplot(111, projection='3d')
  ax.scatter(xs, zs, ys, c='red', marker='o')

  ax.set_xlabel('X')
  ax.set_ylabel('Y')
  ax.set_zlabel('Z')

  plt.show()
