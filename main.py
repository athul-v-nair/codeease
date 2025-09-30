import argparse
from core.watcher import watch_logs
from core.fixer import suggest_fix
from core.runner import implement_fix

def main(command: str, filepath: str):
    logs=watch_logs(command=command, filepath=filepath)

    if not logs:
        # Code should not contain errors
        return

    if logs.get('error'):
        print("\n⚠️ Error detected. Asking Fixer...")
        fixed_code=suggest_fix(logs.get("error"), mode="fix")
        
        if fixed_code:
            print("\n💡 Suggested Fix:")
            print(fixed_code)

            # Implementing the fix in the code
            implement_fix(fix=fixed_code)
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