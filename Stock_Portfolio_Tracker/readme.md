# Stock Portfolio Tracker

## Overview
The Stock Portfolio Tracker is a simple Python application that allows users to calculate the total value of their stock investments based on predefined stock prices. Users can enter stock symbols and quantities, and the program computes the total portfolio value. The result can also be saved to a text file.

---

## Features
- Accepts user input for stock symbols and quantities.
- Uses a hardcoded dictionary to store stock prices.
- Calculates individual stock investment values.
- Calculates total portfolio value.
- Handles unavailable stock symbols gracefully.
- Optionally saves the portfolio summary to a text file.

---

## Technologies Used
- Python 3
- Dictionaries
- Loops
- Conditional Statements
- File Handling

---

## Project Structure

```text
stock_portfolio_tracker/
│
├── stock_portfolio_tracker.py
├── portfolio_report.txt   # Generated after saving results
└── README.md
```

---

## Stock Prices Used

| Stock Symbol | Price ($) |
|-------------|-----------|
| AAPL | 180 |
| TSLA | 250 |
| GOOGL | 140 |
| MSFT | 330 |
| AMZN | 145 |

You can modify these values directly in the `stock_prices` dictionary.

---

## How to Run

### 1. Clone or Download the Project

```bash
git clone https://github.com/your-username/stock-portfolio-tracker.git
```

Or simply download the Python file.

### 2. Run the Program

```bash
python stock_portfolio_tracker.py
```

---

## Example Usage

```text
How many different stocks do you own? 2

Enter stock symbol #1: AAPL
Enter quantity: 10

Enter stock symbol #2: TSLA
Enter quantity: 5

----- Portfolio Summary -----
AAPL: 10 shares × $180 = $1800
TSLA: 5 shares × $250 = $1250

Total Investment Value = $3050

Do you want to save the result? (yes/no): yes
Report saved as 'portfolio_report.txt'
```

---

## Example Output File

```text
Portfolio Summary
-----------------
AAPL: 10 shares × $180 = $1800
TSLA: 5 shares × $250 = $1250

Total Investment Value = $3050
```

---

## Concepts Demonstrated
- Dictionary Data Structure
- User Input and Output
- Iteration using Loops
- Conditional Logic
- Arithmetic Calculations
- File Handling in Python

---

## Future Enhancements
- Load stock prices from a CSV file.
- Fetch real-time stock prices using an API.
- Store multiple portfolios.
- Export results to CSV format.
- Add graphical user interface (GUI).

---

## Author
Developed as a beginner-friendly Python project to practice dictionaries, loops, input/output operations, and file handling.