import subprocess

def try_input(input_string):
    try:
        output = subprocess.check_output(['./bomb'], input=input_string, universal_newlines=True, timeout=5)
        return output.strip()
    except subprocess.CalledProcessError as e:
        return e.output.strip()
    except subprocess.TimeoutExpired:
        return "TimeoutExpired"

def main():
    phase1_input = ""
    phase2_input = ""
    phase3_input = ""
    phase4_input = ""

     for i in range(ord('a'), ord('z')+1):
       for j in range(ord('a'), ord('z')+1):
          for k in range(ord('a'), ord('z')+1):
             for l in range(ord('a'), ord('z')+1):
                for m in range(ord('a'), ord('z')+1):
                   for n in range(ord('a'), ord('z')+1):
                       input_string = f"{phase1_input}\n{phase2_input}\n{phase3_input}\n{phase4_input}\n{char(i)} {char(j)} {char(k)} {char(l)} {char(m)} {char(m)}\n"
                       output = try_input(input_string)
                       if "blown" not in output:
                           print(f"Safe {char(i)} {char(j)} {char(k)} {char(l)} {char(m)} {char(m)}")
                           print(output)
                           return
                       elif "TimeoutExpired" in output:
                           return
                       else:
                           print(f"Tried: {char(i)} {char(j)} {char(k)} {char(l)} {char(m)} {char(m)}, Result: {output}")

if __name__ == "__main__":
    main()

