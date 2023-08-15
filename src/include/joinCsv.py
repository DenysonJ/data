from sys import argv
import pandas as pd

def joinCSV(files: list[str], out: str) -> None:
  first = True
  for file in files:
    df = pd.read_csv(file)
    if first:
      df.to_csv(out, index=False)
      first = False
      continue
    df.to_csv(out, mode='a', index=False, header=False)

if __name__ == "__main__":
  if len(argv) < 3:
    print("Correct usage: python joinCsv.py path_to_file1 path_to_file2 ...")
    exit()
  joinCSV(argv[1:])
