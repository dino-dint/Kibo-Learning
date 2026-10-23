import platform
import sys


def print_system_info():
  print("=== System Information ===")
  print(f"Operating System: {platform.system()} {platform.release()}")
  print(f"Version: {platform.version()}")
  print(f"Machine Architecture: {platform.machine()}")
  print(f"Processor: {platform.processor()}")
  print(f"Python Version: {sys.version.split()[0]}")


def main():
  # Change this to your actual team name
  team_name = "DevLab"

  print(f"Team Name: {team_name}\n")
  print_system_info()


if __name__ == "__main__":
  main()