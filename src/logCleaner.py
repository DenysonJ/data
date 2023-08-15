import sys

def cleaner(file: str) -> None:
  players = {}

  with open(file, "r") as f:
    for line in f:

      cleanLine = line.replace("[CSGOLogger.smx]", "").replace("L ", "").replace(" - ", " ").split("->")[0] + "\n"
      
      if "->" not in line:
        cleanLine = cleanLine.replace("\n\n", "\n")
        for name in players:
          players[name].write(cleanLine)
        continue
      
      name = line.split("->")[-1].lower().replace(" ", "").replace("\n", "")

      if name not in players:
        players[name] = open(file.split(".")[0] + "_" + name + ".log", "x")
      
      players[name].write(cleanLine)
  
  for name in players:
    players[name].close()



def main(argv: list[str]) -> None:
  if len(argv) < 2:
    print("Correct usage: python program.py path_to_file")
    exit()
  
  cleaner(argv[1])

if __name__ == "__main__":
  main(sys.argv)