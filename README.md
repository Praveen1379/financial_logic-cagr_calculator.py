# 📈 Financial Logic: CAGR Calculator

![Python](https://img.shields.io/badge/Language-Python_3-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Domain](https://img.shields.io/badge/Domain-Financial_Analysis-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)
![Status](https://img.shields.io/badge/Status-Tested_&_Live-success?style=for-the-badge)

## 💼 Project Overview
This repository hosts a Python-based financial tool designed to calculate the **Compound Annual Growth Rate (CAGR)**. As a Fintech Analyst, I built this to automate the process of determining the mean annual growth rate of an investment over a specified time period longer than one year.

## 🧮 The Financial Logic
CAGR is one of the most accurate ways to calculate and determine returns for anything that can rise or fall in value over time.

**The Formula Implemented:**
> CAGR = (Ending Value / Beginning Value) ^ (1 / n) - 1

*Where:*
* **Ending Value** = Future Value (FV)
* **Beginning Value** = Present Value (PV)
* **n** = Number of years

## ⚙️ Key Features
* **User Input Validation:** Ensures that negative values or zero years cannot be entered, preventing mathematical errors.
* **Automated Analysis:** The script doesn't just calculate numbers; it provides an **Analyst Insight** (High Growth vs. Low Growth) based on the result.
* **Error Handling:** robust management of non-numeric inputs.

## 🚀 Example Output
```text
--- CAGR Financial Calculator ---
Enter Initial Investment Value (PV): 10000
Enter Final Investment Value (FV): 20000
Enter Number of Years (n): 5

The Compound Annual Growth Rate is: 14.87%
Analysis: This is a high-growth investment (beats average market returns).
