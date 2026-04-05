import tkinter as tk
from tkinter import messagebox
import random

# ============================================
# Rock Paper Scissors - Colorful Rule-Based AI
# Assignment 5 - AI Logic Implementation
# ============================================

player_history = []
player_score = 0
ai_score = 0
round_num = 1

# ── Colors ──────────────────────────────────
BG        = "#f8f7ff"
ROCK_BG   = "#EEEDFE"
ROCK_BD   = "#AFA9EC"
ROCK_FG   = "#3C3489"
PAPER_BG  = "#E6F1FB"
PAPER_BD  = "#85B7EB"
PAPER_FG  = "#185FA5"
SCIS_BG   = "#FAEEDA"
SCIS_BD   = "#FAC775"
SCIS_FG   = "#854F0B"
WIN_BG    = "#E1F5EE"
WIN_FG    = "#085041"
LOSE_BG   = "#FAECE7"
LOSE_FG   = "#712B13"
DRAW_BG   = "#EEEDFE"
DRAW_FG   = "#26215C"
RULE_BG   = "#FAEEDA"
RULE_FG   = "#854F0B"

# ── AI Logic ────────────────────────────────
def ai_move():
    if len(player_history) < 3:
        return random.choice(["rock", "paper", "scissors"])
    last3 = player_history[-3:]
    counts = {"rock": 0, "paper": 0, "scissors": 0}
    for m in last3:
        counts[m] += 1
    most_used = max(counts, key=counts.get)
    counter = {"rock": "paper", "paper": "scissors", "scissors": "rock"}
    return counter[most_used]

def get_winner(player, ai):
    if player == ai:
        return "Draw"
    elif (player=="rock" and ai=="scissors") or \
         (player=="paper" and ai=="rock") or \
         (player=="scissors" and ai=="paper"):
        return "Player Wins"
    else:
        return "AI Wins"

# ── Game Logic ──────────────────────────────
def play(player_move):
    global player_score, ai_score, round_num
    if round_num > 5:
        return

    ai = ai_move()
    player_history.append(player_move)
    result = get_winner(player_move, ai)

    emojis = {"rock": "🪨", "paper": "📄", "scissors": "✂️"}
    move_label.config(text=f"You: {emojis[player_move]}   VS   AI: {emojis[ai]}")

    if result == "Player Wins":
        player_score += 1
        result_label.config(text="You Win! 🎉", fg=WIN_FG)
        result_frame.config(bg=WIN_BG)
        move_label.config(bg=WIN_BG)
        result_label.config(bg=WIN_BG)
        move_name_label.config(bg=WIN_BG)
    elif result == "AI Wins":
        ai_score += 1
        result_label.config(text="AI Wins! 🤖", fg=LOSE_FG)
        result_frame.config(bg=LOSE_BG)
        move_label.config(bg=LOSE_BG)
        result_label.config(bg=LOSE_BG)
        move_name_label.config(bg=LOSE_BG)
    else:
        result_label.config(text="It's a Draw! 🤝", fg=DRAW_FG)
        result_frame.config(bg=DRAW_BG)
        move_label.config(bg=DRAW_BG)
        result_label.config(bg=DRAW_BG)
        move_name_label.config(bg=DRAW_BG)

    move_name_label.config(text=f"You: {player_move}  |  AI: {ai}")
    p_score_label.config(text=str(player_score))
    ai_score_label.config(text=str(ai_score))

    # Update AI Rule
    if len(player_history) < 3:
        rule_label.config(text="AI Rule: Not enough history — playing randomly")
    else:
        last3 = player_history[-3:]
        counts = {"rock": 0, "paper": 0, "scissors": 0}
        for m in last3:
            counts[m] += 1
        most_used = max(counts, key=counts.get)
        counter = {"rock": "paper", "paper": "scissors", "scissors": "rock"}
        rule_label.config(text=f"AI Rule: Your most used '{most_used}' → AI played '{counter[most_used]}'")

    # Update History
    colors = {"rock": ROCK_FG, "paper": PAPER_FG, "scissors": SCIS_FG}
    history_label.config(text="History: " + "  ".join([f"{emojis[m]} {m}" for m in player_history]))

    round_num += 1
    round_label.config(text=f"Round: {min(round_num, 5)} / 5")

    if round_num > 5:
        if player_score > ai_score:
            messagebox.showinfo("Game Over 🏆", f"You Won the Game!\nScore: You {player_score} – AI {ai_score}")
        elif ai_score > player_score:
            messagebox.showinfo("Game Over 🤖", f"AI Won the Game!\nScore: You {player_score} – AI {ai_score}")
        else:
            messagebox.showinfo("Game Over 🤝", f"It's a Draw!\nScore: You {player_score} – AI {ai_score}")

def reset_game():
    global player_history, player_score, ai_score, round_num
    player_history = []
    player_score = 0
    ai_score = 0
    round_num = 1
    move_label.config(text="Choose your move!", bg=BG)
    result_label.config(text="", bg=BG)
    move_name_label.config(text="", bg=BG)
    result_frame.config(bg=BG)
    p_score_label.config(text="0")
    ai_score_label.config(text="0")
    round_label.config(text="Round: 1 / 5")
    rule_label.config(text="AI Rule: Playing randomly for the first 3 rounds")
    history_label.config(text="History: ")

# ── GUI Setup ───────────────────────────────
root = tk.Tk()
root.title("Rock Paper Scissors - Rule-Based AI")
root.geometry("520x600")
root.resizable(False, False)
root.configure(bg=BG)

# Title
tk.Label(root, text="Rock  Paper  Scissors", font=("Arial", 22, "bold"),
         bg=BG, fg="#534AB7").pack(pady=(15, 0))
tk.Label(root, text="Rule-Based AI Game  •  5 Rounds", font=("Arial", 11),
         bg=BG, fg="#888").pack(pady=(2, 15))

# Score Board
score_frame = tk.Frame(root, bg=BG)
score_frame.pack(padx=30, fill="x", pady=(0, 15))

# Player Score
p_frame = tk.Frame(score_frame, bg=WIN_BG, bd=1, relief="solid")
p_frame.pack(side="left", expand=True, fill="both", padx=(0, 5))
tk.Label(p_frame, text="You", font=("Arial", 11, "bold"), bg=WIN_BG, fg=WIN_FG).pack(pady=(8,0))
p_score_label = tk.Label(p_frame, text="0", font=("Arial", 28, "bold"), bg=WIN_BG, fg=WIN_FG)
p_score_label.pack(pady=(0, 8))

# Round
r_frame = tk.Frame(score_frame, bg="#F1EFE8", bd=1, relief="solid")
r_frame.pack(side="left", expand=True, fill="both", padx=5)
tk.Label(r_frame, text="Round", font=("Arial", 11, "bold"), bg="#F1EFE8", fg="#5F5E5A").pack(pady=(8,0))
round_label = tk.Label(r_frame, text="1 / 5", font=("Arial", 14, "bold"), bg="#F1EFE8", fg="#5F5E5A")
round_label.pack(pady=(0, 8))

# AI Score
ai_frame = tk.Frame(score_frame, bg=LOSE_BG, bd=1, relief="solid")
ai_frame.pack(side="left", expand=True, fill="both", padx=(5, 0))
tk.Label(ai_frame, text="AI", font=("Arial", 11, "bold"), bg=LOSE_BG, fg=LOSE_FG).pack(pady=(8,0))
ai_score_label = tk.Label(ai_frame, text="0", font=("Arial", 28, "bold"), bg=LOSE_BG, fg=LOSE_FG)
ai_score_label.pack(pady=(0, 8))

# Move Buttons
tk.Label(root, text="Choose your move:", font=("Arial", 13),
         bg=BG, fg="#444").pack(pady=(5, 8))

btn_frame = tk.Frame(root, bg=BG)
btn_frame.pack()

btn_styles = [
    ("rock",     "🪨", ROCK_BG,  ROCK_BD,  ROCK_FG),
    ("paper",    "📄", PAPER_BG, PAPER_BD, PAPER_FG),
    ("scissors", "✂️", SCIS_BG,  SCIS_BD,  SCIS_FG),
]

for move, emoji, bg, bd, fg in btn_styles:
    f = tk.Frame(btn_frame, bg=bd, bd=2, relief="solid")
    f.pack(side="left", padx=8)
    tk.Button(f, text=f"{emoji}\n{move.capitalize()}",
              font=("Arial", 15), width=7, height=3,
              command=lambda m=move: play(m),
              bg=bg, fg=fg, relief="flat",
              activebackground=bd, cursor="hand2").pack()

# Result Area
result_frame = tk.Frame(root, bg=BG, bd=1, relief="solid")
result_frame.pack(padx=30, fill="x", pady=15)

move_label = tk.Label(result_frame, text="Choose your move!",
                      font=("Arial", 15), bg=BG, fg="#555")
move_label.pack(pady=(12, 4))

result_label = tk.Label(result_frame, text="",
                        font=("Arial", 18, "bold"), bg=BG)
result_label.pack()

move_name_label = tk.Label(result_frame, text="",
                           font=("Arial", 11), bg=BG, fg="#777")
move_name_label.pack(pady=(4, 12))

# AI Rule Box
rule_frame = tk.Frame(root, bg=RULE_BG, bd=1, relief="solid")
rule_frame.pack(padx=30, fill="x", pady=(0, 10))
rule_label = tk.Label(rule_frame,
                      text="AI Rule: Playing randomly for the first 3 rounds",
                      font=("Arial", 10, "italic"), bg=RULE_BG, fg=RULE_FG,
                      wraplength=440)
rule_label.pack(pady=8)

# History
history_label = tk.Label(root, text="History: ", font=("Arial", 11),
                         bg=BG, fg="#666", wraplength=460)
history_label.pack(pady=(0, 8))

# Reset Button
tk.Button(root, text="Start New Game", font=("Arial", 12),
          command=reset_game, bg="#EEEDFE", fg=ROCK_FG,
          relief="solid", bd=1, cursor="hand2",
          padx=20, pady=6).pack(pady=5)

root.mainloop()