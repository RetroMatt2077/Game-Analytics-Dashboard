from flask import Flask, render_template
import pandas as pd
import numpy as np

app = Flask(__name__)

# -----------------------------
# SAMPLE GAME DATA (replace later with CSV if you want)
# -----------------------------
np.random.seed(42)

players = [
    "Arin", "Lyra", "Kael", "Mira", "Doran",
    "Selene", "Rex", "Nova", "Vex", "Iris"
]

df = pd.DataFrame({
    "Player": players,
    "Kills": np.random.randint(5, 50, len(players)),
    "Deaths": np.random.randint(1, 30, len(players)),
    "Assists": np.random.randint(0, 40, len(players)),
    "Accuracy": np.random.randint(40, 100, len(players)),
    "ReactionTime": np.random.randint(100, 600, len(players))
})

# -----------------------------
# SKILL SCORE (your signature feature)
# -----------------------------
df["SkillScore"] = (
    df["Kills"] * 2 +
    df["Assists"] * 1.5 +
    df["Accuracy"] -
    df["Deaths"] * 1.2 -
    df["ReactionTime"] * 0.05
)

df = df.sort_values("SkillScore", ascending=False)

# -----------------------------
# HOME DASHBOARD
# -----------------------------
@app.route("/")
def home():
    top_player = df.iloc[0]

    return render_template(
        "index.html",
        tables=df.to_html(classes="table", index=False),
        top_player=top_player["Player"],
        top_score=round(top_player["SkillScore"], 2)
    )

# -----------------------------
# LEADERBOARD PAGE
# -----------------------------
@app.route("/leaderboard")
def leaderboard():
    return render_template(
        "leaderboard.html",
        tables=df.to_html(classes="table", index=False)
    )

# -----------------------------
# INSIGHTS PAGE
# -----------------------------
@app.route("/insights")
def insights():
    insights = [
        f"Top Player: {df.iloc[0]['Player']}",
        f"Average Accuracy: {df['Accuracy'].mean():.1f}%",
        f"Average Reaction Time: {df['ReactionTime'].mean():.1f}ms",
        "Higher accuracy strongly improves SkillScore ranking",
        "Reaction time has negative impact on performance"
    ]

    return render_template("insights.html", insights=insights)

# -----------------------------
# RUN APP
# -----------------------------
if __name__ == "__main__":
    app.run(debug=True)
