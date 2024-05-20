import subprocess

def try_input(input_string):
    try:
        output = subprocess.check_output(['./bomb49'], input=input_string, universal_newlines=True, timeout=5)
        return output.strip()
    except subprocess.CalledProcessError as e:
        return e.output.strip()
    except subprocess.TimeoutExpired:
        return "TimeoutExpired"

def main():
    phase1_input = ""
    phase2_input = ""
    phase3_input = ""

    for i in range(1000):
        for j in range(1000):
            input_string = f"{phase1_input}\n{phase2_input}\n{phase3_input}\n{i} {j}\n"
            output = try_input(input_string)
            if "blown" not in output:
                print(f"Safe {i} {j}")
                print(output)
                return
            elif "TimeoutExpired" in output:
                return
            else:
                print(f"Tried: {i} {j}, Result: {output}")

if __name__ == "__main__":
    main()
