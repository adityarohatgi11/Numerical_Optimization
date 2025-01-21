# Numerical Optimization using Grid Search and Newton-Raphson

This repository contains an implementation of two numerical optimization methods — **Grid Search** and **Newton-Raphson** — for finding the maximum of a given mathematical function.

## Project Overview

### Assignment Description
The project compares the performance of **Grid Search** and **Newton-Raphson** methods in optimizing a mathematical function \( f: \mathbb{R}^2 \rightarrow \mathbb{R} \). Both methods compute the maximum value of the function within specific constraints and measure the number of function calls made during execution.

### Key Functions
1. **`gridsearch`**: Uses a brute-force grid search algorithm to find the maximum of the function \( f \) over a defined interval with a given precision.
2. **`newton`**: Implements the Newton-Raphson method to find the maximum of the function \( f \) using its gradient and Hessian matrix.

---

## Getting Started

### Prerequisites
This project requires Python 3.x. No additional libraries are needed.

### Files
- **`optimization.py`**: Python script containing the implementations of `gridsearch` and `newton` functions.
- **Documentation**: This README and the assignment description document provide details about the methods and implementation.

---

## Usage

### Running the Code
1. Clone this repository.
2. Open `optimization.py` in your favorite Python IDE or text editor.
3. The code includes predefined test cases:
   - **Newton-Raphson**: 
     ```python
     newton([0,0], 0.001, f, f1, f2)
     ```
     Tests the method with an initial guess of \([0, 0]\) and \( \epsilon = 0.001 \).
   - **Grid Search**: 
     ```python
     gridsearch([-10,-10], [10,10], 0.01, f)
     ```
     Tests the method over the interval \([-10, 10]\) for both dimensions with a precision of \( 0.01 \).

4. Run the script:
   ```bash
   python optimization.py
