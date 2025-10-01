import os
import re
import shutil
import subprocess

def implement_fix(fix: str, filepath: str):
    choice=input('Are you sure you want to inject the fix into the code(y/n):')

    if choice.lower()=='y' and fix:
        # Extracting the code from the returned code block
        code_block=re.findall(r"```(?:python)?\n(.*?)```",fix, re.DOTALL)

        if code_block:
            # Removing the newlines and tabs
            fixed_code = code_block[0].strip()
        else:
            return False

        target_file=os.path.basename(filepath)
        
        # Creating a backupfile
        backup_file = os.path.dirname(filepath)+ "\\" + target_file + ".bak"
        # Copying contents to backup file
        shutil.copyfile(filepath, backup_file)
        print(f"📂 Backup created at {os.path.dirname(filepath)+ "\\" + backup_file}")

        # writing corrected code into the file
        with open(filepath,mode="w",encoding="utf-8") as f:
            f.write(fixed_code)

        return True
    else:
        return False

def re_run(command):
    choice=input('Do you want to rerun the code(y/n):')

    if choice.lower()=='y' and command:
        print("\n▶️ Re-running the program with the applied fix...\n")
        
        result = subprocess.run(command, text=True, capture_output=True, shell=True)

        if result.returncode == 0:
            print("🎉 Program ran successfully after fix!")
            print(result.stdout)
            return True
        else:
            print("⚠️ Program still has errors after fix.")
            print(result.stderr)
            return False