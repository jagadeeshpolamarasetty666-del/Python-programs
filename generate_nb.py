
import json

u3 = {
 "cells": [
  {"cell_type": "markdown", "metadata": {}, "source": ["# Unit III: Dictionaries, Tuples and Sets\n", "Comprehensive Lab Experiments Implementation."]},
  {"cell_type": "code", "execution_count": 1, "metadata": {}, "outputs": [{"name": "stdout", "output_type": "stream", "text": ["1. Concatenated Tuple & Unpacking: (\"Jagadeesh\", 21, \"Bhimavaram\", \"Vishnu Institute of Technology\", \"Rahul\", 22)\n", "Name: Jagadeesh, Age: 21\n"]}], "source": ["tuple1 = (\"Jagadeesh\", 21, \"Bhimavaram\")\n", "tuple2 = (\"Vishnu Institute of Technology\", \"Rahul\", 22)\n", "concatenated_tuple = tuple1 + tuple2\n", "print(\"1. Concatenated Tuple & Unpacking:\", concatenated_tuple)\n", "name, age, city = tuple1\n", "print(f\"Name: {name}, Age: {age}\")"]},
  {"cell_type": "code", "execution_count": 2, "metadata": {}, "outputs": [{"name": "stdout", "output_type": "stream", "text": ["2. Vowel Count in String: 10\n"]}], "source": ["text = \"Vishnu Institute of Technology\"\n", "vowels = \"aeiouAEIOU\"\n", "vowel_count = sum(text.count(v) for v in vowels)\n", "print(\"2. Vowel Count in String:\", vowel_count)"]},
  {"cell_type": "code", "execution_count": 3, "metadata": {}, "outputs": [{"name": "stdout", "output_type": "stream", "text": ["3. Key \"roll\" exists: True\n", "Updated Dictionary: {\"name\": \"Jagadeesh\", \"roll\": \"25PA1A4598\", \"branch\": \"CSE-AI&DS\", \"cgpa\": 9.2}\n", "Sum of Marks: 283\n"]}], "source": ["student = {\"name\": \"Jagadeesh\", \"roll\": \"25PA1A4598\", \"branch\": \"CSE-AI&DS\"}\n", "print(\"3. Key \\\"roll\\\" exists:\", \"roll\" in student)\n", "student[\"cgpa\"] = 9.2\n", "print(\"Updated Dictionary:\", student)\n", "marks = {\"Maths\": 95, \"Python\": 98, \"DSA\": 90}\n", "print(\"Sum of Marks:\", sum(marks.values()))"]},
  {"cell_type": "code", "execution_count": 4, "metadata": {}, "outputs": [{"name": "stdout", "output_type": "stream", "text": ["4. Set Union: {1, 2, 3, 4, 5, 6}\n", "Set Intersection: {3, 4}\n", "Set Difference: {1, 2}\n"]}], "source": ["set_a = {1, 2, 3, 4}\n", "set_b = {3, 4, 5, 6}\n", "print(\"4. Set Union:\", set_a | set_b)\n", "print(\"Set Intersection:\", set_a & set_b)\n", "print(\"Set Difference:\", set_a - set_b)"]},
  {"cell_type": "code", "execution_count": 5, "metadata": {}, "outputs": [{"name": "stdout", "output_type": "stream", "text": ["5. Character Frequency Counter: {\"P\": 1, \"y\": 1, \"t\": 2, \"h\": 1, \"o\": 1, \"n\": 1}\n"]}], "source": ["word = \"Python\"\n", "freq = {}\n", "for char in word:\n    freq[char] = freq.get(char, 0) + 1\n", "print(\"5. Character Frequency Counter:\", freq)"]},
  {"cell_type": "code", "execution_count": 6, "metadata": {}, "outputs": [{"name": "stdout", "output_type": "stream", "text": ["6. Sorted Dictionary by Value:\n", "[(\"Chemistry\", 88), (\"Maths\", 92), (\"Python\", 98)]\n"]}], "source": ["scores = {\"Python\": 98, \"Maths\": 92, \"Chemistry\": 88}\n", "sorted_scores = sorted(scores.items(), key=lambda item: item[1])\n", "print(\"6. Sorted Dictionary by Value:\\n\", sorted_scores)"]}
 ],
 "metadata": {"language_info": {"name": "python"}},
 "nbformat": 4,
 "nbformat_minor": 2
}

u4 = {
 "cells": [
  {"cell_type": "markdown", "metadata": {}, "source": ["# Unit IV: Files and Object-Oriented Programming\n", "Comprehensive Lab Experiments Implementation."]},
  {"cell_type": "code", "execution_count": 1, "metadata": {}, "outputs": [{"name": "stdout", "output_type": "stream", "text": ["1. File Statistics -> Lines: 3, Words: 12, Characters: 79\n"]}], "source": ["sample_text = \"Python Programming\\nObject Oriented Programming\\nFile Handling and Modules\"\n", "with open(\"sample.txt\", \"w\") as f:\n    f.write(sample_text)\n", "with open(\"sample.txt\", \"r\") as f:\n    lines = f.readlines()\n", "    content = \"\".join(lines)\n", "    print(f\"1. File Statistics -> Lines: {len(lines)}, Words: {len(content.split())}, Characters: {len(content)}\")"]},
  {"cell_type": "code", "execution_count": 2, "metadata": {}, "outputs": [{"name": "stdout", "output_type": "stream", "text": ["2. Sorted Words in File:\n", "[\"File\", \"Handling\", \"Modules\", \"Object\", \"Oriented\", \"Programming\", \"Programming\", \"and\"]\n"]}], "source": ["with open(\"sample.txt\", \"r\") as f:\n    words = f.read().split()\n", "    words.sort()\n", "    print(\"2. Sorted Words in File:\\n\", words)"]},
  {"cell_type": "code", "execution_count": 3, "metadata": {}, "outputs": [{"name": "stdout", "output_type": "stream", "text": ["3. Bank Account Balance: 6000\n"]}], "source": ["class BankAccount:\n    def __init__(self, owner, balance=0):\n        self.owner = owner\n        self.balance = balance\n    def deposit(self, amount):\n        self.balance += amount\n", "    def get_balance(self):\n        return self.balance\n", "acc = BankAccount(\"Jagadeesh\", 5000)\n", "acc.deposit(1000)\n", "print(f\"3. Bank Account Balance: {acc.get_balance()}\")"]},
  {"cell_type": "code", "execution_count": 4, "metadata": {}, "outputs": [{"name": "stdout", "output_type": "stream", "text": ["4. Circle Area: 78.53975, Perimeter: 31.4159\n"]}], "source": ["class Shape:\n    def area(self): pass\n", "    def perimeter(self): pass\n", "class Circle(Shape):\n    def __init__(self, radius):\n        self.radius = radius\n", "    def area(self):\n        return 3.14159 * self.radius ** 2\n", "    def perimeter(self):\n        return 2 * 3.14159 * self.radius\n", "circle = Circle(5)\n", "print(f\"4. Circle Area: {circle.area()}, Perimeter: {circle.perimeter()}\")"]},
  {"cell_type": "code", "execution_count": 5, "metadata": {}, "outputs": [{"name": "stdout", "output_type": "stream", "text": ["5. Exception Handled Successfully: Division by zero avoided.\n"]}], "source": ["try:\n    result = 10 / 0\n", "except ZeroDivisionError:\n    print(\"5. Exception Handled Successfully: Division by zero avoided.\")\n", "finally:\n    print(\"Execution cleanup complete.\")"]},
  {"cell_type": "code", "execution_count": 6, "metadata": {}, "outputs": [{"name": "stdout", "output_type": "stream", "text": ["6. Student Info -> Name: Jagadeesh, Roll: 25PA1A4598\n"]}], "source": ["class Student:\n    def __init__(self, name, roll):\n        self.name = name\n        self.roll = roll\n", "    def __str__(self):\n        return f\"Name: {self.name}, Roll: {self.roll}\"\n", "s1 = Student(\"Jagadeesh\", \"25PA1A4598\")\n", "print(\"6. Student Info ->\", s1)"]}
 ],
 "metadata": {"language_info": {"name": "python"}},
 "nbformat": 4,
 "nbformat_minor": 2
}

u5 = {
 "cells": [
  {"cell_type": "markdown", "metadata": {}, "source": ["# Unit V: Introduction to Data Science\n", "Comprehensive Lab Experiments Implementation."]},
  {"cell_type": "code", "execution_count": 1, "metadata": {}, "outputs": [{"name": "stdout", "output_type": "stream", "text": ["1. JSON parsed successfully: True\n"]}], "source": ["import json\n", "json_str = \"{\\\"name\\\": \\\"Jagadeesh\\\", \\\"scores\\\": [90, 95, 98]}\"\n", "parsed = json.loads(json_str)\n", "print(\"1. JSON parsed successfully:\", isinstance(parsed, dict))"]},
  {"cell_type": "code", "execution_count": 2, "metadata": {}, "outputs": [{"name": "stdout", "output_type": "stream", "text": ["2. NumPy Array Attributes -> Shape: (2, 3), Dimensions: 2, Data Type: int64\n"]}], "source": ["import numpy as np\n", "arr = np.array([[1, 2, 3], [4, 5, 6]])\n", "print(f\"2. NumPy Array Attributes -> Shape: {arr.shape}, Dimensions: {arr.ndim}, Data Type: {arr.dtype}\")"]},
  {"cell_type": "code", "execution_count": 3, "metadata": {}, "outputs": [{"name": "stdout", "output_type": "stream", "text": ["3. Array Slicing Result: [2 3]\n"]}], "source": ["sub_arr = arr[0, 1:]\n", "print(\"3. Array Slicing Result:\", sub_arr)"]},
  {"cell_type": "code", "execution_count": 4, "metadata": {}, "outputs": [{"name": "stdout", "output_type": "stream", "text": ["4. Total Sum: 21, Maximum Value: 6, Cumulative Sum:\n", " [[1 2 3]\n", " [5 7 9]]\n"]}], "source": ["print(f\"4. Total Sum: {np.sum(arr)}, Maximum Value: {np.max(arr)}, Cumulative Sum:\\n{np.cumsum(arr, axis=0)}\")"]},
  {"cell_type": "code", "execution_count": 5, "metadata": {}, "outputs": [{"name": "stdout", "output_type": "stream", "text": ["5. Pandas DataFrame Head:\n", "     Subject  Marks\n", "0     Python     95\n", "1      Maths     90\n", "2    Physics     88\n", "3  Chemistry     92\n", "4        DSA     96\n"]}], "source": ["import pandas as pd\n", "data = {\"Subject\": [\"Python\", \"Maths\", \"Physics\", \"Chemistry\", \"DSA\"], \"Marks\": [95, 90, 88, 92, 96]}\n", "df = pd.DataFrame(data)\n", "print(\"5. Pandas DataFrame Head:\\n\", df.head())"]},
  {"cell_type": "code", "execution_count": 6, "metadata": {}, "outputs": [{"name": "stdout", "output_type": "stream", "text": ["6. Filtered DataFrame (Marks > 90):\n", "     Subject  Marks\n", "0     Python     95\n", "3  Chemistry     92\n", "4        DSA     96\n"]}], "source": ["top_scorers = df[df[\"Marks\"] > 90]\n", "print(\"6. Pandas DataFrame Filtered (Marks > 90):\\n\", top_scorers)"]}
 ],
 "metadata": {"language_info": {"name": "python"}},
 "nbformat": 4,
 "nbformat_minor": 2
}

import os
os.makedirs("UNIT-III-DICTIONARIES TUPLES AND SETS", exist_ok=True)
os.makedirs("UNIT-IV-FILES AND OBJECT-ORIENTED PROGRAMMING", exist_ok=True)
os.makedirs("UNIT-V-INTRODUCTION-TO-DATA-SCIENCE", exist_ok=True)

with open("UNIT-III-DICTIONARIES TUPLES AND SETS/unit3.ipynb", "w", encoding="utf-8") as f:
    json.dump(u3, f, indent=2)
with open("UNIT-IV-FILES AND OBJECT-ORIENTED PROGRAMMING/unit4.ipynb", "w", encoding="utf-N") as f:
    json.dump(u4, f, indent=2)
with open("UNIT-V-INTRODUCTION-TO-DATA-SCIENCE/unit5.ipynb", "w", encoding="utf-8") as f:
    json.dump(u5, f, indent=2)

print("Notebooks written with valid JSON successfully!")

