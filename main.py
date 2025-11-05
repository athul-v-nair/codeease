import argparse
from core.watcher import watch_logs
from core.fixer import suggest_fix
from core.runner import implement_fix
from core.runner import re_run

def main(command: str, filepath: str):
    logs=watch_logs(command=command, filepath=filepath)

    if not logs:
        # Code should not contain errors
        return

    if logs.get('error'):
        print("\n⚠️ Error detected. Asking Fixer...")
        fixed_code=suggest_fix(logs.get("error"))
        
        if fixed_code:
            print("\n💡 Suggested Fix:")
            print(fixed_code)

            # Implementing the fix in the code
            write_fix=implement_fix(fix=fixed_code, filepath=filepath)
            
            # Checking if correct code is injected into the file
            # If yes, rerun the code if user wishes to
            if write_fix:
                re_run(command=command)
        else:
            print("No fix could be generated.")
    else:
        print("\n✅ Program ran successfully. No fixes needed.")

if __name__=="__main__":
    parser = argparse.ArgumentParser(description="Run a Python script and print its output.")
    parser.add_argument("command",type=str,help="Input the command to run")
    parser.add_argument("filepath",type=str,help="Input the Filepath")
    args = parser.parse_args()

    if args.command and args.filepath:
        main(args.command, args.filepath)         