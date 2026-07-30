# Birthday Paradox Simulator 🎂

An interactive Streamlit app that explores the Birthday Paradox in two different ways.

The project includes a **Probability Simulator** for estimating the probability of shared birthdays through repeated experiments, and a **Visual Simulator** that generates a single group of birthdays and shows which people share the same birthday.

---

## Live Demo

Try the app online:

[Open Birthday Paradox Simulator](https://birthday-paradox-simulation.streamlit.app/)

## Features

### 📊 Probability Simulator

* Input the number of people and simulation trials
* Calculate the probability of at least two people sharing a birthday
* Visualise the result with a bar chart
* View how the probability changes as the number of people increases


### 👥 Visual Simulator

* Choose a group size from 1 to 100 people
* Generate a random birthday for each person and display each person and their birthday
* Detect shared birthdays within the group and highlight them


---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/F-Absalan200/birthday-paradox.git
cd birthday-paradox
```

2. Install the dependencies:

```bash
pip install -r requirements.txt
```

---

## Usage

Run the Streamlit app:

```bash
streamlit run src/app.py
```

After launching the application, use the sidebar to choose between the two simulators.

### Probability Simulator

1. Enter the number of people.
2. Enter the number of simulation trials.
3. Click **Calculate Probability**.
4. View the estimated probability of shared birthdays.
5. Explore the probability chart.

### Visual Simulator

1. Enter the number of people.
2. Click **Generate Birthdays**.
3. View the randomly generated birthdays.
4. Check whether any people share the same birthday.
5. Explore the matching birthday groups.

---

## Project Structure

```text
birthday-paradox/
│
├── src/
│   ├── app.py
│   │
│   ├── probability_simulator/
│   │   ├── __init__.py
│   │   └── logic.py
│   │
│   ├── visual_simulator/
│   │   ├── __init__.py
│   │   └── logic.py
│   │
│   └── __init__.py
│
├── assets/
│   └── ...
│
├── requirements.txt
└── README.md
```

---

## How It Works

The project demonstrates two different approaches to the Birthday Paradox.

The **Probability Simulator** runs the experiment many times and calculates how often at least two people share a birthday.

The **Visual Simulator** performs one experiment at a time. It generates one birthday for each person, checks for duplicates, and visually identifies people with matching birthdays.

This separation makes it possible to explore the Birthday Paradox both statistically and visually.

---

## Author

Absalan | [GitHub](https://github.com/F-Absalan200?tab=repositories)


