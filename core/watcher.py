import subprocess
import os

def watch_logs(command: str, filepath: str):
    try:
        # if file exists in the path
        if(os.path.isfile(filepath)):
            result=subprocess.run(command, text=True, capture_output=True)
            logs={"output": result.stdout, "error": result.stderr}
            return logs
        else:
            print("File does not exist in the provided directory")
    except Exception as e:
        return f"Runner error: {e}"