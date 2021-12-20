import csv
import os
import json

def csv_to_json(path: str):

  with open(path, "r") as fp:
    csv_list = list(csv.DictReader(fp))

  file_name = os.path.basename(path).split(".")[0]

  with open(f"./{file_name}.json", "w") as fp:
    json.dump(csv_list, fp)

def main():
  csv_to_json("./benchmark.csv")

main()