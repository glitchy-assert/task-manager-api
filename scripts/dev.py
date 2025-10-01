#!/usr/bin/env python3
import subprocess
import sys
import os


def main():
    try:
        subprocess.run(
            ["uvicorn", "task_manager.main:app", "--reload", "--port", "8000"],
            check=True,
        )
    except KeyboardInterrupt:
        sys.exit(0)
    except Exception as e:
        print(f"Error happened:{os.linesep}{e}")


if __name__ == "__main__":
    main()
