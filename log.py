from sys import argv
from datetime import datetime
import pandas as pd

class AimLog:
  pitch = []
  yaw = []
  aimingAtClient = []
  timing = []
  parsed = []
  output = []

  def __init__(self, file: str) -> None:
    with open(file) as f:
      for line in f:
        month = int(line.split("/")[0])
        day = int(line.split("/")[1])
        year = int(line.split("/")[2].split(" ")[0])
        hour = int(line.split(":")[0].split(" ")[1])
        minute = int(line.split(":")[1])
        seconds = int(line.split(":")[2])
        self.timing.append(datetime(year, month, day, hour, minute, seconds))
        if ("ROUND" in line) or ("map" in line) or ("Map" in line):
          self.aimingAtClient.append(float('inf'))
          self.pitch.append(float('inf'))
          self.yaw.append(float('inf'))
          continue
        self.aimingAtClient.append(bool(int(line.split("AimingAtClient =")[1].split(" ")[1])))
        self.pitch.append(float(line.split("Pitch =")[1].split(" ")[1]))
        self.yaw.append(float(line.split("Yaw =")[1].split(" ")[1]))

  def get_times_aiming_client(self, steps: int, cheating: bool) -> None:
    i = 0
    while i < len(self.timing) - steps:
      if self.aimingAtClient[i+steps]:
        j = i + 1
        while j < i + steps + 1:
          self.parsed.append(self.yaw[j])
          self.parsed.append(self.pitch[j])
          j += 1
        i += steps
        self.output.append(int(cheating))
      i += 1
  
  def save_to_csv(self, nameInput: str, nameOutput: str) -> None:
    data = { 'data': self.parsed }
    df = pd.DataFrame(data)
    df.to_csv(nameInput, index=False)

    data = { 'data': self.output }
    df = pd.DataFrame(data)
    df.to_csv(nameOutput, index=False)

def main(argv: str) -> None:
  aim = AimLog(argv)

  aim.get_times_aiming_client(10, False)
  aim.save_to_csv("X.csv", "Y.csv")

if __name__ == "__main__":
  main(argv[1])