# Child Safety Checker

A beginner-friendly Python command-line tool to check if a child can safely use a product (like a car seat, high chair, or stroller) based on age, weight, and height requirements.

## Features
- Enter child info (name, age, weight, height)
- See which products are safe for the child
- Color-coded results (green = safe, red = unsafe)
- Easy to extend with new products

## Setup Instructions

1. **Clone or download this project.**
2. **Open a terminal and navigate to the project folder.**
3. **Create a virtual environment:**
   ```
   python -m venv venv
   ```
4. **Activate the virtual environment:**
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On Mac/Linux:
     ```
     source venv/bin/activate
     ```
5. **Install dependencies:**
   ```
   pip install -r requirements.txt
   ```
6. **Run the program:**
   ```
   python main.py
   ```

## Requirements
- Python 3.7+
- Packages: colorama, tabulate

## Project Structure
- `main.py` — Entry point
- `child_safety_checker.py` — Main logic and classes
- `data/` — (For future data files)
- `tests/` — (For future tests)

---

*Created for learning Python and solving real-world problems!*

