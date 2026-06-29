# ⌨️ Python Typing Speed Test

<p align="center">

**A modern desktop application built with Python and Tkinter to measure typing speed (Words Per Minute) and typing accuracy through an interactive graphical interface.**

Designed as an educational Python project demonstrating GUI development, event-driven programming, performance metric calculation, and modular application design.


![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-green)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey)
![License](https://img.shields.io/badge/License-MIT-yellow)
![Status](https://img.shields.io/badge/Status-Active-success)

</p>


# 📑 Table of Contents

* Overview
* Why This Project?
* Features
* Demo
* Screenshots
* Application Workflow
* Architecture
* Technology Stack
* Project Structure
* Installation
* Running the Application
* How It Works
* Difficulty Levels
* Typing Metrics
* High Score Tracking
* Future Enhancements
* Contributing
* License
* Author



# 📖 Overview

Typing proficiency is an important skill for developers, students, writers, and professionals. Measuring typing speed and accuracy helps users monitor improvement over time.

This project provides a desktop application that presents random words to the user, records typing performance, calculates typing speed in **Words Per Minute (WPM)**, measures typing accuracy, and stores high scores for multiple difficulty levels.

The application is implemented using **Python** and **Tkinter**, making it lightweight, portable, and easy to run without external GUI frameworks.


# 🎯 Why This Project?

This project was created to explore several core Python concepts in a practical desktop application, including:

* Event-driven GUI programming
* Keyboard input handling
* Timer-based application logic
* Performance metric calculation
* State management
* Modular code organization
* File-based data persistence
* User interface design with Tkinter

Although simple in scope, the project demonstrates the complete lifecycle of a desktop application—from user interaction to result calculation.



# ✨ Features

* Random word generation for each typing session
* Real-time typing test
* Words Per Minute (WPM) calculation
* Typing accuracy calculation
* Multiple difficulty levels
* High-score tracking
* Simple and responsive Tkinter interface
* Lightweight and easy to run
* Cross-platform support (Python + Tkinter)



# 🎬 Demo

> **Demo GIF Placeholder**

```
docs/demo.gif
```



# 🖼 Screenshots

## Main Window

```
docs/screenshots/home.png
```



## Typing Test

```
docs/screenshots/test.png
```



## Results Screen

```
docs/screenshots/results.png
```



## High Scores

```
docs/screenshots/highscores.png
```



# 🔄 Application Workflow

```text
Launch Application
        │
        ▼
Select Difficulty
        │
        ▼
Generate Random Word
        │
        ▼
User Starts Typing
        │
        ▼
Measure Time
        │
        ▼
Calculate WPM
        │
        ▼
Calculate Accuracy
        │
        ▼
Update High Score
        │
        ▼
Display Results
```



# 🏗 Architecture

```text
+----------------------+
|      Tkinter GUI     |
+----------+-----------+
           |
           ▼
+----------------------+
|  Input Handler       |
+----------+-----------+
           |
           ▼
+----------------------+
| Typing Engine        |
+----------+-----------+
           |
           ▼
+----------------------+
| Statistics Calculator|
+----------+-----------+
           |
           ▼
+----------------------+
| High Score Manager   |
+----------+-----------+
           |
           ▼
+----------------------+
| Local Storage        |
+----------------------+
```



# ⚙️ Technology Stack

| Category             | Technology        |
| -------------------- | ----------------- |
| Programming Language | Python            |
| GUI Framework        | Tkinter           |
| Data Storage         | Local File        |
| IDE                  | VS Code / PyCharm |
| Version Control      | Git               |

---

# 📁 Project Structure

```text
typing-speed-test/

├── assets/
├── data/
├── screenshots/
├── main.py
├── requirements.txt
├── README.md
└── LICENSE
```

> Adjust this structure to match your repository.



# 🚀 Installation

## Clone the Repository

```bash
git clone https://github.com/NoorMahammad-S/python-typing-speed-test.git
```

Navigate into the project directory:

```bash
cd python-typing-speed-test
```



## Create a Virtual Environment (Recommended)

Windows

```bash
python -m venv venv
venv\Scripts\activate
```

Linux/macOS

```bash
python3 -m venv venv
source venv/bin/activate
```



## Install Dependencies

If a `requirements.txt` file exists:

```bash
pip install -r requirements.txt
```

If the project uses only Tkinter, no additional installation is typically required because Tkinter is included with standard Python distributions.



# ▶️ Running the Application

```bash
python main.py
```

The graphical application window will open.

Follow the on-screen instructions to begin the typing test.



# 📝 How It Works

1. Launch the application.
2. Select a difficulty level.
3. A random word is displayed.
4. Begin typing immediately.
5. The application records the elapsed time.
6. WPM is calculated.
7. Typing accuracy is calculated.
8. High scores are updated if a new record is achieved.



# 📊 Typing Metrics

## Words Per Minute (WPM)

Typing speed is measured using the elapsed typing time.

Higher WPM indicates faster typing performance.



## Accuracy

Typing accuracy measures how closely the user's input matches the expected text.

Accuracy helps balance speed with correctness.



# 🏆 High Score Tracking

The application stores the best results separately for each supported difficulty level.

Example:

* Easy
* Medium
* Hard

This allows users to monitor progress over time.



# 💡 Skills Demonstrated

This repository showcases practical experience with:

* Python programming
* Tkinter GUI development
* Event-driven programming
* User input handling
* Timer management
* Application state management
* Performance metric calculation
* Local data persistence
* Modular application design



# 🌱 Future Enhancements

Potential improvements include:

* Sentence-based typing tests
* Paragraph typing mode
* Dark mode
* User profiles
* SQLite database support
* Performance analytics dashboard
* Export statistics
* Global leaderboard
* Multiplayer typing races
* Achievement system



# 🤝 Contributing

Contributions are welcome.

If you have suggestions for improvements or discover a bug:

1. Fork the repository.
2. Create a feature branch.
3. Commit your changes.
4. Submit a Pull Request.

Please read `CONTRIBUTING.md` before submitting major changes.



# 📄 License

This project is licensed under the MIT License.

See the `LICENSE` file for details.



# 👨‍💻 Author

**Noor Mahammad**

Software Engineer | Python Developer | Backend Engineering Enthusiast

Interested in Python, backend systems, automation, scalable software, and AI-powered applications.



# ⭐ Support

If you found this project helpful:

* ⭐ Star the repository
* 🍴 Fork the project
* 🐞 Report issues
* 💡 Suggest improvements

Contributions and feedback are always appreciated.



# 📌 Repository Topics

python • tkinter • typing-speed-test • desktop-application • gui • typing • wpm • typing-practice • productivity • python-project • keyboard-events • event-driven-programming



# 📈 Project Status

**Current Status:** Active

This project serves as a Python desktop application demonstrating GUI programming concepts and typing performance analysis. Future enhancements are tracked in the project roadmap.

---

# 📚 Related Skills

Python • Tkinter • Desktop Applications • GUI Programming • Event-Driven Programming • Typing Speed Analysis • Performance Metrics • Software Development • Object-Oriented Programming • User Interface Design
