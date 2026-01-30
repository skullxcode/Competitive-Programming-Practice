# Competitive Programming Practice

This repository is a comprehensive technical archive of algorithmic solutions. Each file is named directly after the specific problem it addresses, providing a clear and searchable map of solved challenges.

---

## 🏛 Solution Philosophy

Each solution within this repository is developed with a focus on three core pillars of competitive programming:

### 1. Mathematical Analysis
Before implementation, each problem undergoes a rigorous analysis phase to identify the underlying mathematical properties, such as:
* **Combinatorics & Number Theory** (Primality testing, modular arithmetic).
* **Parity & Invariants** (Identifying states that remain constant under operations).
* **Game Theory** (Minimax strategies and Grundy numbers).

### 2. Algorithmic Efficiency
I prioritize solutions that optimize the balance between time and space complexity. The goal is to reach the theoretical lower bound of complexity for every challenge:
* **Time Complexity:** Aiming for $O(1)$, $O(\log N)$, or $O(N)$ for large constraints ($N \approx 10^7$).
* **Space Complexity:** Minimizing memory footprints to stay within strict competitive limits.

### 3. Implementation Precision
Solutions are written to be robust and readable, utilizing:
* **Fast I/O:** Custom input/output routines to handle massive datasets.
* **Standard Library Optimization:** Efficient use of the STL (C++) or standard collections to reduce overhead.

---

## 🔍 Navigation & Usage

The repository uses a flat structure where **File Name = Question Name**. This allows for rapid searching and indexing.

### How to Search
You can find a specific solution by using `Ctrl + F` (or `Cmd + F`) on the GitHub file list and typing the name of the problem.

### Compiling and Running
To execute a solution (assuming C++), use the following optimization flags to simulate a competitive environment:
```bash
g++ -O3 -Wall "Question_Name.cpp" -o solution
./solution < input.txt
