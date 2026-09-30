# Simple Virus & Ransomware Simulation

## About

This repository is a collection of small Python-based cybersecurity research projects designed to demonstrate different malware concepts in a controlled and educational environment.

The project currently contains two complementary components:

- **Simple Virus** — demonstrates basic malware concepts and how simple self-replicating behavior can be implemented.
- **Ransomware Simulation** — demonstrates ransomware-related concepts in a controlled environment for security research and defensive analysis.

The purpose of combining these projects is to provide a practical environment for understanding malware behavior, identifying security indicators, and exploring defensive detection techniques.

> **Purpose:** Educational use, authorized security testing, malware research, and defensive security analysis.


# Simple Virus (Educational PoC)

An educational Python demonstration inspired by NeuralNine illustrating how prepending script modification works. This repository analyzes the mechanics of self-replicating script structures, file introspection, and how Endpoint Detection and Response (EDR) systems identify script modification techniques.

---

## Technical Mechanics

This proof-of-concept (PoC) demonstrates the structure of a **prepending script infector**:

1. **Self-Introspection:** Reads its own source code file using `sys.argv[0]` and extracts code bounded by marker comments (`### THE VIRUS STARTS HERE ###` and `### THE VIRUS ENDS HERE ###`).
2. **Target Discovery:** Uses `glob.glob('*.py')` to locate potential target Python scripts within the working directory.
3. **Infection State Verification:** Checks target files for the existence of the marker comment to prevent infinite self-replication loops.
4. **Prepending Injection:** If uninfected, prepends the extracted code block to the top of the target file while retaining the host file's original code (`Hello, World!`).

---


##  Ransomware Simulation

The `ransomware-simulation/` directory contains a controlled ransomware simulation project.

The purpose is to demonstrate ransomware-related concepts and provide a basis for studying:

- File encryption concepts
- Malware behavior
- Security indicators
- Defensive monitoring
- Incident response
- Detection opportunities

The simulation should only be executed inside an isolated environment containing test data.

## Usage

### Simple Virus

Navigate to the project root and follow the documentation associated with the individual implementation.

### Ransomware Simulation

Navigate to:

```bash
cd ransomware-simulation
```

Then follow the instructions provided in:

```text
ransomware-simulation/README.md
```

**Only use test files inside an isolated laboratory environment.**

## ⚠️ Legal & Ethical Disclaimer

This repository is maintained strictly for educational, academic, and defensive security research purposes.
- Isolated Testing Only: Run this demonstration exclusively inside a temporary virtual machine or dedicated sandbox environment containing non-critical test files.
- Authorized Use: Do not execute file modification scripts on unauthorized systems or production environments.
- Liability: The author assumes no liability or responsibility for any misuse or damage caused by this code.
