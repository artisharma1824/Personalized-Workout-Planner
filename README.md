# 🏋️‍♂️ Smart Fitness & Nutrition Planner (Python CLI)

[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)
[![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)](#)
[![Domain](https://img.shields.io/badge/Domain-Health%20%26%20Fitness-brightgreen?style=for-the-badge)](#)

A interactive, rule-based Python Command Line Interface (CLI) application designed to generate customized workout routines, pure vegetarian clean diet plans, and holistic wellness recommendations based on individual body goals, timeline, and fitness experience.

---

## 🌟 Key Features

* **Multi-Goal Program Selection:** Supports 4 distinct fitness tracks:
  1. **Weight Loss:** Tailored circuit training and low-calorie vegetarian diet charts.
  2. **Weight Gain:** Caloric-surplus meal charts paired with heavy weight-training routines.
  3. **Muscle Building:** Dynamic macro-protein target calculation based on body weight ($1.8\text{g} \times \text{body weight in kg}$) with experience-based scaling (`easy`, `medium`, `hard`).
  4. **General Fitness & Wellness:** Balanced routine combining Yoga, Pranayam, hydration, skincare, and daily physical activity based on available workout minutes.
* **Target & Timeline Logic:** Dynamically adjusts workout intensity and diet plans based on whether target goals are short-term ($\le 30$ days) or long-term ($> 30$ days).
* **Pure Vegetarian Clean Diet Charts:** Focuses on accessible, nutritious Indian vegetarian food items (e.g., Moong Dal Chilla, Sprouts, Oats, Paneer, Soya Chunks, Makhana, Rajma, and Khichdi).

---

## 🧠 System Logic & Architecture

