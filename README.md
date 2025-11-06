# Greedy and Divide-and-Conquer Approaches to Real-World Optimization  
### *COT5405 – Analysis of Algorithms*  
**University of Florida**

---

## 🧩 Project Overview

This repository contains the complete implementation, report, and experimental artifacts for our **Analysis of Algorithms (AOA) project**, titled:

> **“Greedy and Divide-and-Conquer Approaches to Real-World Optimization: Trail Signage and City Soundscape Analysis.”**

The objective of this project is to demonstrate how two classical algorithmic paradigms — **Greedy** and **Divide-and-Conquer** — can be effectively applied to model and solve complex real-world optimization problems. The project integrates theoretical modeling, algorithmic analysis, correctness proofs, and empirical validation through Python simulations and data visualization.

---

## 👩‍💻 Team Members

| Name | UFID | Role |
|------|------|------|
| **Harshavardhan Reddy Jonnala** | 1511–8670 | Algorithm design, experimental setup, report writing |
| **Tanuja Naga Sai Palapati** | 8947–5480 | Code implementation, performance analysis, LaTeX report formatting |

**Course:** COT5405 – Analysis of Algorithms  
**Instructor:** *[Add your professor’s name]*  
**Term:** Fall 2025  
**Institution:** University of Florida  

---

## 📘 Problem Statements

### 1️⃣ Greedy Algorithm Problem — *Minimal Trail Signage*
- **Domain:** Environmental and infrastructure optimization.
- **Objective:** Minimize the number of trail signs installed such that every visibility segment on a scenic trail is covered by at least one sign.  
- **Abstraction:** Interval Stabbing / Hitting Set Problem.  
- **Approach:** Greedy selection based on earliest finishing interval.
- **Complexity:** \( O(n \log n) \)
- **Proof:** Optimality shown using an exchange argument.  
- **Result:** The algorithm guarantees minimal signage placement with full trail coverage.

### 2️⃣ Divide-and-Conquer Problem — *City Soundscape Outline*
- **Domain:** Urban acoustic monitoring and sound engineering.
- **Objective:** Compute the continuous “sound outline” representing the maximum loudness level over time for overlapping urban events.
- **Abstraction:** Upper Envelope (Skyline) Merge Problem.
- **Approach:** Recursive division of sound intervals followed by merging of partial envelopes.
- **Complexity:** \( O(n \log n) \)
- **Proof:** Inductive correctness proof and merge consistency.
- **Result:** Produces an accurate and scalable soundscape model for large datasets.

---

## 🧠 Algorithmic Insights

| Technique | Strategy | Key Property | Application |
|------------|-----------|---------------|--------------|
| **Greedy** | Local optimal choice (rightmost interval endpoint) | Exchange argument proves global optimality | Trail Signage |
| **Divide-and-Conquer** | Recursive splitting and merging of outlines | Inductive proof ensures correctness | Soundscape Outline |

Both algorithms demonstrate \( O(n \log n) \) time complexity, confirmed experimentally.

---

## ⚙️ Repository Structure

aoa-project/
│
├── AOA_Project_Report.pdf # Final IEEE-formatted report
├── code/
│ ├── signage_greedy.py # Greedy algorithm implementation
│ └── soundscape_skyline.py # Divide-and-conquer algorithm implementation
│
├── data/
│ ├── signage_greedy_timings.csv # Experimental timings for greedy algorithm
│ ├── soundscape_skyline_timings.csv # Experimental timings for divide & conquer
│ ├── signage_greedy_runtime.png # Runtime vs input size (greedy)
│ └── soundscape_skyline_runtime.png # Runtime vs input size (skyline)
│
├── appendix/
│ └── LLM_prompts.txt # Prompts used for LaTeX and code generation
│
└── README.md # Project documentation (this file)
