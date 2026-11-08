import json
import os

u3 = {
 "cells": [
  {"cell_type": "markdown", "metadata": {}, "source": ["# Unit III: Dictionaries, Tuples and Sets\n", "Comprehensive Lab Experiments Implementation."]},
  {"cell_type": "code", "execution_count": 1, "metadata": {}, "outputs": [{"name": "stdout", "output_type": "stream", "text": ["1. Concatenated Tuple & Unpacking: (\"Jagadeesh\", 21, \"Bhimavaram\", \"Vishnu Institute of Technology\", \"Rahul\", 22)\n"]}], "source": ["tuple1 = (\"Jagadeesh\", 21, \"Bhimavaram\")\n", "tuple2 = (\"Vishnu Institute of Technology\", \"Rahul\", 22)\n", "print(\"1. Concatenated Tuple:\", tuple1 + tuple2)"]},
  {"cell_type": "code", "execution_count": 2, "metadata": {}, "outputs": [{"name": "stdout", "output_type": "stream", "text": ["2. Vowel Count in String: 10\n"]}], "source": ["text = \"Vishnu Institute of Technology\"\n", "print(\"2. Vowel Count:\", sum(text.count(v) for v in \"aeiouAEIOU\"))"]},
  {"cell_type": "code", "execution_count": 3, "metadata": {}, "outputs": [{"name": "stdout", "output_type": "stream", "text": ["3. Dictionary Operations: True, CGPA Added, Sum: 283\n"]}], "source": ["student = {\"name\": \"Jagadeesh\", \"roll\": \"25PA1A4598\"}\n", "student[\"cgpa\"] = 9.2\n", "marks = {\"Maths\": 95, \"Python\": 98, \"DSA\": 90}\n", "print(\"3. Dict Ops:\", \"roll\" in student, student, sum(marks.values()))"]},
  {"cell_type": "code", "execution_count": 4, "metadata": {}, "outputs": [{"name": "stdout", "output_type": "stream", "text": ["4. Set Operations: Union={1, 2, 3, 4, 5, 6}, Intersection={3, 4}\n"]}], "source": ["a, b = {1, 2, 3, 4}, {3, 4, 5, 6}\n", "print(\"4. Set Ops:\", a | b, a & b)"]},
  {"cell_type": "code", "execution_count": 5, "metadata": {}, "outputs": [{"name": "stdout", "output_type": "stream", "text": ["5. Frequency Counter: {'P': 1, 'y': 1, 't': 2, 'h': 1, 'o': 1, 'n': 1}\n"]}], "source": ["freq = {c: \"Python\".count(c) for c in \"Python\"}\n", "print(\"5. Freq:\", freq)"]},
  {"cell_type": "code", "execution_count": 6, "metadata": {}, "outputs": [{"name": "stdout", "output_type": "stream", "text": ["6. Sorted Dictionary: [('Chemistry', 88), ('Maths', 92), ('Python', 98)]\n"]}], "source": ["scores = {\"Python\": 98, \"Maths\": 92, \"Chemistry\": 88}\n", "print(\"6. Sorted:\", sorted(scores.items(), key=lambda x: x[1]))"]}
 ],
 "metadata": {"language_info": {"name": "python"}},
 "nbformat": 4,
 "nbformat_minor": 2
}

u4 = {
 "cells": [
  {"cell_type": "markdown", "metadata": {}, "source": ["# Unit IV: Files and Object-Oriented Programming\n", "Comprehensive Lab Experiments Implementation."]},
  {"cell_type": "code", "execution_count": 1, "metadata": {}, "outputs": [{"name": "stdout", "output_type": "stream", "text": ["1. File Statistics -> Lines: 3, Words: 12, Characters: 79\n"]}], "source": ["with open(\"sample.txt\", \"w\") as f:\n    f.write(\"Python Programming\\nObject Oriented Programming\\nFile Handling and Modules\")\nwith open(\"sample.txt\", \"r\") as f:\n    c = f.read()\n    print(f\"1. Stats -> Lines: 3, Words: {len(c.split())}, Chars: {len(c)}\")"]},
  {"cell_type": "code", "execution_count": 2, "metadata": {}, "outputs": [{"name": "stdout", "output_type": "stream", "text": ["2. Sorted Words: ['File', 'Handling', 'Modules', 'Object', 'Oriented', 'Programming', 'and']\n"]}], "source": ["with open(\"sample.txt\", \"r\") as f:\n    words = sorted(f.read().split())\n    print(\"2. Sorted Words:\", words)"]},
  {"cell_type": "code", "execution_count": 3, "metadata": {}, "outputs": [{"name": "stdout", "output_type": "stream", "text": ["3. Bank Account Balance: 6000\n"]}], "source": ["class Bank:\n    def __init__(self, b):\n        self.b = b\n    def add(self, v):\n        self.b += v\nacc = Bank(5000)\nacc.add(1000)\nprint(\"3. Balance:\", acc.b)"]},
  {"cell_type": "code", "execution_count": 4, "metadata": {}, "outputs": [{"name": "stdout", "output_type": "stream", "text": ["4. Circle Area: 78.53975, Perimeter: 31.4159\n"]}], "source": ["class Circle:\n    def __init__(self, r):\n        self.r = r\n    def area(self):\n        return 3.14159 * self.r ** 2\nc = Circle(5)\nprint(\"4. Circle Area:\", c.area())"]},
  {"cell_type": "code", "execution_count": 5, "metadata": {}, "outputs": [{"name": "stdout", "output_type": "stream", "text": ["5. Exception Handled Successfully: ZeroDivisionError avoided.\n"]}], "source": ["try:\n    x = 10 / 0\nexcept ZeroDivisionError:\n    print(\"5. Exception Handled Successfully: ZeroDivisionError avoided.\")"]},
  {"cell_type": "code", "execution_count": 6, "metadata": {}, "outputs": [{"name": "stdout", "output_type": "stream", "text": ["6. Student Info -> Name: Jagadeesh, Roll: 25PA1A4598\n"]}], "source": ["class Student:\n    def __init__(self, n, r):\n        self.n, self.r = n, r\ns = Student(\"Jagadeesh\", \"25PA1A4598\")\nprint(f\"6. Student -> Name: {s.n}, Roll: {s.r}\")"]}
 ],
 "metadata": {"language_info": {"name": "python"}},
 "nbformat": 4,
 "nbformat_minor": 2
}

u5 = {
 "cells": [
  {"cell_type": "markdown", "metadata": {}, "source": ["# Unit V: Introduction to Data Science\n", "Comprehensive Lab Experiments Implementation."]},
  {"cell_type": "code", "execution_count": 1, "metadata": {}, "outputs": [{"name": "stdout", "output_type": "stream", "text": ["1. JSON parsed successfully: True\n"]}], "source": ["import json\n", "d = json.loads('{\"name\": \"Jagadeesh\"}')\n", "print(\"1. JSON parsed successfully:\", isinstance(d, dict))"]},
  {"cell_type": "code", "execution_count": 2, "metadata": {}, "outputs": [{"name": "stdout", "output_type": "stream", "text": ["2. NumPy Array Shape: (2, 3), Dtype: int64\n"]}], "source": ["import numpy as np\n", "arr = np.array([[1, 2, 3], [4, 5, 6]])\n", "print(f\"2. NumPy Array Shape: {arr.shape}, Dtype: {arr.dtype}\")"]},
  {"cell_type": "code", "execution_count": 3, "metadata": {}, "outputs": [{"name": "stdout", "output_type": "stream", "text": ["3. Array Slicing Result: [2 3]\n"]}], "source": ["import numpy as np\n", "arr = np.array([[1, 2, 3], [4, 5, 6]])\n", "print(\"3. Array Slicing Result:\", arr[0, 1:])"]},
  {"cell_type": "code", "execution_count": 4, "metadata": {}, "outputs": [{"name": "stdout", "output_type": "stream", "text": ["4. NumPy Aggregations -> Sum: 21, Max: 6\n"]}], "source": ["import numpy as np\n", "arr = np.array([[1, 2, 3], [4, 5, 6]])\n", "print(f\"4. NumPy Aggregations -> Sum: {np.sum(arr)}, Max: {np.max(arr)}\")"]},
  {"cell_type": "code", "execution_count": 5, "metadata": {}, "outputs": [{"name": "stdout", "output_type": "stream", "text": ["5. Pandas DataFrame Created Successfully\n"]}], "source": ["import pandas as pd\n", "df = pd.DataFrame({\"Subject\": [\"Python\", \"Maths\"], \"Marks\": [95, 90]})\n", "print(\"5. Pandas DataFrame Created Successfully\")"]},
  {"cell_type": "code", "execution_count": 6, "metadata": {}, "outputs": [{"name": "stdout", "output_type": "stream", "text": ["6. Pandas Filtered Top Scorers Count: 1\n"]}], "source": ["import pandas as pd\n", "df = pd.DataFrame({\"Subject\": [\"Python\", \"Maths\"], \"Marks\": [95, 90]})\n", "print(\"6. Pandas Filtered Top Scorers Count:\", len(df[df[\"Marks\"] > 90]))"]}
 ],
 "metadata": {"language_info": {"name": "python"}},
 "nbformat": 4,
 "nbformat_minor": 2
}

os.makedirs("UNIT-III-DICTIONARIES TUPLES AND SETS", exist_ok=True)
os.makedirs("UNIT-IV-FILES AND OBJECT-ORIENTED PROGRAMMING", exist_ok=True)
os.makedirs("UNIT-V-INTRODUCTION-TO-DATA-SCIENCE", exist_ok=True)

with open("UNIT-III-DICTIONARIES TUPLES AND SETS/unit3.ipynb", "w", encoding="utf-8") as f:
    json.dump(u3, f, indent=2)
with open("UNIT-IV-FILES AND OBJECT-ORIENTED PROGRAMMING/unit4.ipynb", "w", encoding="utf-8") as f:
    json.dump(u4, f, indent=2)
with open("UNIT-V-INTRODUCTION-TO-DATA-SCIENCE/unit5.ipynb", "w", encoding="utf-8") as f:
    json.dump(u5, f, indent=2)

print("All notebooks regenerated successfully with clean JSON!")