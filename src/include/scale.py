from sys import argv
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler

def scaleData(file: str) -> None:
  scaler = MinMaxScaler(feature_range=(0, 1))

  df = pd.read_csv(file)

  df['yaw'] = scaler.fit_transform(np.array(df['yaw']).reshape(-1, 1)).flatten()
  df['pitch'] = scaler.fit_transform(np.array(df['pitch']).reshape(-1, 1)).flatten()

  df.to_csv("scaled.csv", index=False)

if __name__ == "__main__":
  if len(argv) < 2:
    print("Correct usage: python scale.py path_to_file")
    exit()
  scaleData(argv[1])