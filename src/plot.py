import matplotlib.pyplot as plt
import numpy as np
from include.log import AimLog
from sys import argv

def plotFromLog(logFile):
  aim = AimLog(logFile)

  y1points = np.array(aim.pitch)
  y2points = np.array(aim.yaw)
  xpoints = np.array(aim.timing)
  mask = np.array(aim.aimingAtClient)

  print("count total: " + str(len(xpoints)))
  print("count pitch: " + str(len(mask[mask == 1])))

  y1 = [y1points[i] if mask[i] == 1 else 0 for i in range(len(y1points))]
  y2 = [y2points[i] if mask[i] == 1 else 0 for i in range(len(y2points))]

  plt.plot(xpoints, y1)
  plt.show()

  plt.plot(xpoints, y2)
  plt.show()

  plt.plot(y1, y2)
  plt.show()
  
def main(file):
  plotFromLog(file)


if __name__ == "__main__":
  main(argv[1])