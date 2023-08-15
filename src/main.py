from sys import argv
from include.log import AimLog
from include.joinCsv import joinCSV
from include.scale import scaleData

def main(argv: list[str]):
  steps = int(argv[0])
  listInputFiles = []
  listOutputFiles = []

  # log to csv getting only the data when the player is aiming 
  # at the client with the given number of steps
  for i in range(1, len(argv), 2):
    log = AimLog(argv[i])
    log.get_times_aiming_client(steps, argv[i+1] == "True")
    log.save_to_csv( "yaw_pitch" + str(i) + ".csv", "output" + str(i) + ".csv")
    listInputFiles.append("yaw_pitch" + str(i) + ".csv")
    listOutputFiles.append("output" + str(i) + ".csv")

  # join all csv files into one
  joinCSV(listInputFiles, "input.csv")
  joinCSV(listOutputFiles, "output.csv")

  # scale data
  scaleData("input.csv")

  

if __name__ == "__main__":
  main(argv[1:])