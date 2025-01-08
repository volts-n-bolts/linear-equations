# linear-equations
A lightweight Python library for solving systems of linear equations without external dependencies. Built with modularity in mind, this implementation can be easily adapted to other programming languages.

## Overview
This library implements matrix operations and linear algebra algorithms from first principles, making it ideal for educational purposes and situations where using NumPy or similar libraries isn't feasible.

The codebase is available in two formats:
- `main.py` - Modular implementation with separate classes for each operation
- `combined.py` - Single-file version containing all functionality

## Limitations
- Optimized for systems with up to 9 variables
- Uses Leibniz formula for determinant calculation
- While not the fastest implementation, prioritizes clarity and portability

## Project Structure
├── main.py
├── combined.py
├── LICENSE
├── README.md
└── src/
    ├── matrix_operations/
    │   ├── adjugate.py
    │   ├── determinant.py
    │   ├── inverse.py
    │   ├── minor_matrices.py
    │   └── multiplication.py
    └── utils/
        ├── array_calculator.py
        └── heaps_algorithm.py
