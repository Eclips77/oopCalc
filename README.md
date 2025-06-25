# 📐 Shape Calculator

A Python-based object-oriented geometry calculator for working with multiple shape types.

---

## 🔍 Project Overview

This project allows you to create, manage, and perform operations on geometric shapes such as:

- Square
- Rectangle
- Circle
- Triangle
- Hexagon

All shape logic follows OOP principles, including inheritance and operator overloading.

---

## ✅ Features

- Create and store shapes
- Display all shapes with their details
- Compare the area between two shapes
- Add or subtract shapes of the same type → creates a new shape
- Divide the area of one shape by another
- Show the shape with the largest or smallest area

---

## 🗂️ Project Structure

```
oopCalc/
│
├── app.py               # Main app logic and menu system
├── calculator.py        # Shape classes (Square, Circle, etc.)
├── input_handler.py     # User input per shape
├── colors.py            # Colored console output (uses colorama)
├── main.py              # Entry point (runs ShapeApp)
└── README.md            # This file
```

---

## 💡 Notes

- Adding two shapes of the same type returns a **new shape object**.
- Adding two different shapes returns only the **combined area as a float**.
- New shapes are automatically added to the list when applicable.
- The app uses ANSI color output via the `colorama` library.

---

## ⚙️ Requirements

- Python 3.10+
- `colorama` library:

```bash
pip install colorama
```

---

## 🚀 Run the App

```bash
python main.py
```

---

## 🧠 Example

```
Main Menu:
1. Create new shape
2. Show all shapes
3. Compare two shapes
4. Add areas of two shapes
5. Subtract areas of two shapes
6. Show shape with largest area
7. Show shape with smallest area
8. Divide area of one shape by another
0. Exit
```

---

Built by Yaakov
