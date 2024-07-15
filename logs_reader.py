import sys

def parse_log_line(line):
  try:
    data = line.split()
    return {
      "date": data[0],
      "time": data[1],
      "level": data[2],
      "message": " ".join(data[3:]),
    }
  except IndexError:
      print(f"Line with wrong format was skipped: {line}")

def load_logs(file_path):
  levels = []
  with open(file_path, 'r',encoding='utf-8') as file:
    lines = file.readlines()
    for line in lines:
      log = parse_log_line(line)
      if log:
        levels.append(log)
  return levels

def count_logs_by_level(logs):
  result = {}
  for log in logs:
    level = log["level"]
    if level in result:
      result[level] += 1
    else:
      result[level] = 1

  return result

def filter_logs_by_level(logs, level):
  return list(filter(lambda item: item["level"] == level, logs))

def display_log_counts(info):
  print("Level of logs | Amount")
  print("--------------|----------")

  for key, value in info.items():
    print(f"{key:<13} | {value}")

def display_logs_by_level(logs_by_level, level):
  print(f"\nLogs details for level '{level}':")
  for log in logs_by_level:
    print(f"{log["date"]} {log["time"]} - {log["message"]}")

def main(argv):
  path_to_logs = argv[1]
  try:
    logs = load_logs(path_to_logs)
    logs_by_level_amount = count_logs_by_level(logs)
    display_log_counts(logs_by_level_amount)

    if len(argv) == 3:
      level = argv[2]
      logs_by_level = filter_logs_by_level(logs, level)
      display_logs_by_level(logs_by_level, level)
  except FileNotFoundError:
    print(f"File with path: '{path_to_logs}', not found")
  except IndexError:
    print("Please add path to logs file")
  except IsADirectoryError:
    print(f"We expect path to file, but got directory: '{path_to_logs}'")
  except PermissionError:
    print(f"Sorry we haven't permission to read this file: '{path_to_logs}'")


if __name__ == "__main__":
  main(sys.argv)