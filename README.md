🎮 Game Analytics Dashboard

   

A Flask-based game analytics dashboard that simulates and analyzes player performance data using custom metrics, statistical analysis, and interactive web views.

This project demonstrates how raw game data can be transformed into actionable insights and ranked leaderboards, similar to real esports analytics platforms.


---

🚀 Live Concept

> A lightweight esports-style analytics dashboard built with Python.



It simulates player performance and visualizes:

Skill ranking systems

Performance metrics

Comparative analytics

Game-style statistics



---

📊 Features

🏆 Player Leaderboard

Dynamic ranking system based on SkillScore

Automatically sorts players by performance


🧠 SkillScore System

A custom performance formula combining:

Kills

Assists

Accuracy

Deaths (penalty)

Reaction time (penalty)


📈 Analytics Insights

Average accuracy across players

Reaction time impact analysis

Performance trend summaries


🌐 Web Dashboard

Built with Flask

Multi-page navigation

Clean, minimal UI



---

⚙️ Tech Stack

Python 🐍

Flask 🌐

Pandas 📊

NumPy 🔢

HTML / CSS 🎨



---

🧱 Project Structure

Game-Analytics-Dashboard/
│
├── app.py                  # Main Flask application
├── data.py                 # Dataset generation (if separated)
├── analytics.py            # Core calculations (optional refactor)
│
├── templates/
│   ├── index.html          # Dashboard home
│   ├── leaderboard.html    # Player rankings
│   ├── insights.html       # Analytics summary
│
├── static/
│   ├── style.css           # Styling
│
├── requirements.txt
└── README.md


---

🧠 How It Works

1. Data Generation

Player stats are generated using simulated values:

Kills

Deaths

Assists

Accuracy

Reaction time



---

2. SkillScore Calculation

Each player is ranked using a weighted formula:

SkillScore =
(Kills × 2)
+ (Assists × 1.5)
+ Accuracy
- (Deaths × 1.2)
- (ReactionTime × 0.05)


---

3. Ranking System

Players are sorted in descending order of SkillScore to generate a leaderboard.


---

4. Web Dashboard

Flask renders:

Main dashboard (overview)

Leaderboard page

Insights page



---

📊 Example Insights

Higher accuracy strongly improves ranking performance

Reaction time negatively impacts SkillScore

Balanced players outperform high-risk builds

Support-style roles (high assists) remain competitive



---

🎯 Learning Objectives

This project demonstrates:

Flask web development fundamentals

Data analysis with Pandas

Feature engineering (SkillScore system)

Game analytics modeling

Backend-to-frontend data rendering

Dashboard design concepts



---

🚀 Future Improvements

📊 Add interactive charts (Plotly / Chart.js)

🗄️ Load real CSV match data

🔍 Add filters (class, rank, stat range)

🌐 Deploy live (Render / Railway)

🧑‍🤝‍🧑 Add multiplayer comparison mode

📥 Add data upload system



---

📸 Screenshots (Recommended)

> Add screenshots here for maximum impact



Leaderboard view

Player stats table

Insights page



---

👤 Author

RetroMatt2077

Focused on:

Python development

Game systems design

Data analysis & visualization

Flask web applications



---

⭐ Why This Project Matters

This project simulates a real-world game analytics platform, similar to systems used in:

Esports dashboards

Player performance tracking tools

Game balancing systems

Competitive ranking engines


It combines data science + backend development + UI design into one cohesive application.

---

🧭 Summary

A full-stack Python web dashboard that turns raw game statistics into meaningful insights and rankings using a custom-built analytics engine.

🚀 HOW TO RUN
Bash
pip install flask pandas numpy
python app.py
Open:

http://127.0.0.1:5000
