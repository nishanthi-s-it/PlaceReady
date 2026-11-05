import tkinter as tk
from tkinter import ttk, messagebox
import database

# =====================================
# PLACEREADY PYTHON EDITION
# =====================================

root = tk.Tk()
root.title("PlaceReady - Smarter Placement Journey")
root.geometry("1000x650")
root.minsize(800, 550)
root.configure(bg="#f3f6fb")

database.create_tables()

# =====================================
# HEADER
# =====================================

header = tk.Frame(root, bg="#23395d", height=100)
header.pack(fill="x")
header.pack_propagate(False)

tk.Label(
    header,
    text="PlaceReady",
    font=("Arial", 26, "bold"),
    fg="white",
    bg="#23395d"
).pack(pady=(15, 0))

tk.Label(
    header,
    text="Smarter Placement Journey",
    font=("Arial", 12),
    fg="#dce6f5",
    bg="#23395d"
).pack()

# =====================================
# MAIN DASHBOARD
# =====================================

content = tk.Frame(root, bg="#f3f6fb")
content.pack(fill="both", expand=True, padx=30, pady=25)

tk.Label(
    content,
    text="Welcome to PlaceReady!",
    font=("Arial", 22, "bold"),
    fg="#23395d",
    bg="#f3f6fb"
).pack(anchor="w", pady=(5, 10))

tk.Label(
    content,
    text="Prepare for placements, assess your skills, and track your progress.",
    font=("Arial", 12),
    fg="#4b5563",
    bg="#f3f6fb"
).pack(anchor="w", pady=(0, 25))

# Dashboard cards
cards_frame = tk.Frame(content, bg="#f3f6fb")
cards_frame.pack(fill="x")

cards = [
    ("Coding", "Practice programming skills"),
    ("SQL", "Improve database knowledge"),
    ("Aptitude", "Develop problem-solving skills"),
    ("Communication", "Build communication skills")
]

for index, (name, detail) in enumerate(cards):
    card = tk.Frame(
        cards_frame,
        bg="white",
        highlightbackground="#d9e2ef",
        highlightthickness=1,
        padx=15,
        pady=20
    )

    card.grid(
        row=index // 2,
        column=index % 2,
        padx=10,
        pady=10,
        sticky="nsew"
    )

    tk.Label(
        card,
        text=name,
        font=("Arial", 16, "bold"),
        fg="#23395d",
        bg="white"
    ).pack(anchor="w")

    tk.Label(
        card,
        text=detail,
        font=("Arial", 10),
        fg="#4b5563",
        bg="white",
        wraplength=300
    ).pack(anchor="w", pady=(8, 0))

cards_frame.columnconfigure(0, weight=1)
cards_frame.columnconfigure(1, weight=1)

# =====================================
# ASSESSMENT QUESTIONS
# =====================================

question_bank = {
    "Coding": [
        ("Which data type stores a whole number in Python?",
         ["int", "str", "list", "dict"], 0),
        ("Which keyword defines a function?",
         ["class", "def", "function", "new"], 1),
        ("Which symbol is used for comments in Python?",
         ["//", "#", "/*", "<!--"], 1),
        ("What is the output of print(2 + 3)?",
         ["23", "5", "6", "Error"], 1),
        ("Which loop iterates over a sequence?",
         ["for", "switch", "case", "define"], 0),
        ("Which data type stores True or False?",
         ["int", "str", "bool", "list"], 2),
        ("Which brackets create a Python list?",
         ["()", "{}", "[]", "<>"], 2),
        ("Which keyword checks another condition?",
         ["else if", "elif", "elseif", "then"], 1),
        ("What does len([10, 20, 30]) return?",
         ["2", "3", "30", "10"], 1),
        ("Which keyword imports a module?",
         ["include", "using", "import", "require"], 2)
    ],

    "SQL": [
        ("Which command retrieves data?",
         ["INSERT", "SELECT", "DELETE", "UPDATE"], 1),
        ("Which clause filters records?",
         ["ORDER BY", "GROUP BY", "WHERE", "JOIN"], 2),
        ("Which command adds a new row?",
         ["INSERT", "SELECT", "DROP", "ALTER"], 0),
        ("Which command modifies existing records?",
         ["CHANGE", "UPDATE", "MODIFY TABLE", "EDIT"], 1),
        ("Which command removes selected rows?",
         ["DELETE", "SELECT", "CREATE", "INSERT"], 0),
        ("Which clause sorts query results?",
         ["SORT", "ORDER BY", "ARRANGE", "GROUP BY"], 1),
        ("Which function counts rows?",
         ["SUM()", "TOTAL()", "COUNT()", "NUMBER()"], 2),
        ("Which keyword removes duplicate results?",
         ["UNIQUE", "DISTINCT", "SINGLE", "DIFFERENT"], 1),
        ("Which key uniquely identifies a table row?",
         ["Foreign key", "Primary key", "Duplicate key", "Sort key"], 1),
        ("Which JOIN returns matching rows from both tables?",
         ["INNER JOIN", "CROSS JOIN", "FULL JOIN", "LEFT JOIN"], 0)
    ],

    "Aptitude": [
        ("What is 20% of 100?",
         ["10", "20", "30", "40"], 1),
        ("What is 12 + 18?",
         ["20", "25", "30", "35"], 2),
        ("What is 15% of 200?",
         ["15", "20", "30", "45"], 2),
        ("What is the square of 9?",
         ["18", "72", "81", "99"], 2),
        ("Find the next number: 2, 4, 6, 8, __",
         ["9", "10", "12", "14"], 1),
        ("What is the average of 10 and 20?",
         ["10", "15", "20", "30"], 1),
        ("If one pen costs ₹5, what do 4 pens cost?",
         ["₹10", "₹15", "₹20", "₹25"], 2),
        ("What is 3/4 expressed as a percentage?",
         ["25%", "50%", "75%", "80%"], 2),
        ("A car travels 60 km in 1 hour. How far in 2 hours at the same speed?",
         ["60 km", "90 km", "100 km", "120 km"], 3),
        ("What is 144 divided by 12?",
         ["10", "11", "12", "14"], 2)
    ],

    "Communication": [
        ("Which is best in a job interview?",
         ["Interrupting", "Listening carefully",
          "Ignoring questions", "Speaking rudely"], 1),
        ("What should a professional email use?",
         ["Clear language", "Slang only",
          "No greeting", "All capital letters"], 0),
        ("What should you do if you don't understand a question?",
         ["Guess angrily", "Politely ask for clarification",
          "Ignore it", "Leave immediately"], 1),
        ("Which is an example of active listening?",
         ["Interrupting", "Checking your phone",
          "Paying attention", "Changing the topic"], 2),
        ("How should you begin a formal email?",
         ["Hey dude", "Dear Sir/Madam",
          "Yo", "What's up"], 1),
        ("What is important during a presentation?",
         ["Speaking clearly", "Speaking too fast",
          "Avoiding the audience", "Reading inaudibly"], 0),
        ("Which is professional workplace behaviour?",
         ["Blaming everyone", "Respecting others",
          "Spreading rumours", "Ignoring colleagues"], 1),
        ("How should you respond to constructive feedback?",
         ["Listen and learn", "Argue immediately",
          "Ignore everything", "Insult the speaker"], 0),
        ("Which is suitable body language in an interview?",
         ["Appropriate eye contact", "Constantly looking away",
          "Turning your back", "Rolling your eyes"], 0),
        ("What makes a good team member?",
         ["Refusing to cooperate", "Sharing ideas respectfully",
          "Taking all the credit", "Ignoring teammates"], 1)
    ]
}

# =====================================
# SKILL ASSESSMENT
# =====================================

def open_assessment():
    window = tk.Toplevel(root)
    window.title("PlaceReady - Skill Assessment")
    window.geometry("650x450")
    window.configure(bg="#f3f6fb")

    category_var = tk.StringVar(value="Coding")
    answer_var = tk.IntVar(value=-1)

    current = {"index": 0, "score": 0, "questions": []}

    tk.Label(
        window,
        text="Skill Assessment",
        font=("Arial", 20, "bold"),
        bg="#f3f6fb",
        fg="#23395d"
    ).pack(pady=15)

    tk.Label(
        window,
        text="Choose a skill:",
        font=("Arial", 11),
        bg="#f3f6fb"
    ).pack()

    category_box = ttk.Combobox(
        window,
        textvariable=category_var,
        values=list(question_bank.keys()),
        state="readonly",
        width=25
    )
    category_box.pack(pady=8)

    question_label = tk.Label(
        window,
        text="",
        font=("Arial", 13, "bold"),
        bg="#f3f6fb",
        wraplength=550
    )
    question_label.pack(pady=20)

    options_frame = tk.Frame(window, bg="#f3f6fb")
    options_frame.pack(anchor="w", padx=70)

    feedback = tk.Label(
        window,
        text="",
        bg="#f3f6fb",
        font=("Arial", 10)
    )
    feedback.pack(pady=8)

    option_buttons = []

    for i in range(4):
        button = tk.Radiobutton(
            options_frame,
            text="",
            variable=answer_var,
            value=i,
            font=("Arial", 11),
            bg="#f3f6fb",
            anchor="w"
        )
        button.pack(anchor="w", pady=3)
        option_buttons.append(button)

    def show_question():
        questions = current["questions"]
        index = current["index"]
        question, options, correct = questions[index]

        question_label.config(
            text=f"Question {index + 1} of {len(questions)}\n\n{question}"
        )

        answer_var.set(-1)
        feedback.config(text="")

        for i, option in enumerate(options):
            option_buttons[i].config(text=option)

    def start_quiz():
        current["index"] = 0
        current["score"] = 0
        current["questions"] = question_bank[category_var.get()]

        category_box.config(state="disabled")
        start_button.config(state="disabled")
        next_button.config(state="normal", text="Submit Answer")

        show_question()

    def next_question():
        if answer_var.get() == -1:
            messagebox.showwarning(
                "Select an answer",
                "Please select an answer first.",
                parent=window
            )
            return

        questions = current["questions"]
        index = current["index"]

        if answer_var.get() == questions[index][2]:
            current["score"] += 1

        if index < len(questions) - 1:
            current["index"] += 1
            show_question()
        else:
            score = current["score"]
            total = len(questions)
            category = category_var.get()

            database.save_assessment(category, score, total)

            messagebox.showinfo(
                "Assessment Complete",
                f"Skill: {category}\n"
                f"Score: {score}/{total}\n"
                "Your result has been saved!",
                parent=window
            )

            window.destroy()

    start_button = tk.Button(
        window,
        text="Start Assessment",
        command=start_quiz,
        bg="#23395d",
        fg="white",
        font=("Arial", 11, "bold"),
        padx=12,
        pady=6
    )
    start_button.pack(pady=5)

    next_button = tk.Button(
        window,
        text="Next",
        command=next_question,
        bg="#287a50",
        fg="white",
        font=("Arial", 11, "bold"),
        padx=20,
        pady=6
    )
    next_button.pack(pady=5)

    question_label.config(
        text="Choose a category and click Start Assessment."
    )
    next_button.config(state="disabled")


# =====================================
# ASSESSMENT HISTORY + CLEAR HISTORY
# =====================================

def open_history():
    history_window = tk.Toplevel(root)
    history_window.title("PlaceReady - Assessment History")
    history_window.geometry("700x400")
    history_window.configure(bg="#f3f6fb")

    tk.Label(
        history_window,
        text="Assessment History",
        font=("Arial", 20, "bold"),
        fg="#23395d",
        bg="#f3f6fb"
    ).pack(pady=15)

    columns = ("category", "score", "date")

    table = ttk.Treeview(
        history_window,
        columns=columns,
        show="headings",
        height=12
    )

    table.heading("category", text="Skill")
    table.heading("score", text="Score")
    table.heading("date", text="Date")

    table.column("category", width=180)
    table.column("score", width=120)
    table.column("date", width=300)

    table.pack(
        fill="both",
        expand=True,
        padx=20,
        pady=(5, 5)
    )

    def refresh_history():
        for item in table.get_children():
            table.delete(item)

        records = database.get_assessments()

        for category, score, total, date in records:
            table.insert(
                "",
                "end",
                values=(category, f"{score}/{total}", date)
            )

        return records

    def clear_history():
        records = database.get_assessments()

        if not records:
            messagebox.showinfo(
                "No History",
                "There is no assessment history to clear.",
                parent=history_window
            )
            return

        confirm = messagebox.askyesno(
            "Confirm Clear History",
            "Are you sure you want to clear all assessment history?\n\n"
            "This action cannot be undone.",
            parent=history_window
        )

        if confirm:
            database.clear_assessments()
            refresh_history()

            messagebox.showinfo(
                "History Cleared",
                "All assessment history has been cleared successfully.",
                parent=history_window
            )

    buttons_frame = tk.Frame(
        history_window,
        bg="#f3f6fb"
    )
    buttons_frame.pack(pady=10)

    tk.Button(
        buttons_frame,
        text="Clear History",
        command=clear_history,
        bg="#b83232",
        fg="white",
        font=("Arial", 11, "bold"),
        padx=15,
        pady=7
    ).pack(side="left", padx=5)

    tk.Button(
        buttons_frame,
        text="Close",
        command=history_window.destroy,
        bg="#23395d",
        fg="white",
        font=("Arial", 11, "bold"),
        padx=15,
        pady=7
    ).pack(side="left", padx=5)

    records = refresh_history()

    if not records:
        messagebox.showinfo(
            "No History",
            "No assessments have been saved yet.",
            parent=history_window
        )


# =====================================
# PRACTICE TASKS
# =====================================

def open_tasks():
    task_window = tk.Toplevel(root)
    task_window.title("PlaceReady - Practice Tasks")
    task_window.geometry("600x450")
    task_window.configure(bg="#f3f6fb")

    tk.Label(
        task_window,
        text="Practice Tasks",
        font=("Arial", 20, "bold"),
        fg="#23395d",
        bg="#f3f6fb"
    ).pack(pady=15)

    entry = tk.Entry(task_window, font=("Arial", 12), width=35)
    entry.pack(pady=8)

    task_list = tk.Listbox(
        task_window,
        font=("Arial", 11),
        width=55,
        height=10
    )
    task_list.pack(pady=10)

    task_ids = []

    def refresh_tasks():
        task_list.delete(0, tk.END)
        task_ids.clear()

        for task_id, task_name, completed in database.get_tasks():
            status = "✓" if completed else "○"
            task_list.insert(tk.END, f"{status} {task_name}")
            task_ids.append(task_id)

    def add_new_task():
        task_name = entry.get().strip()

        if not task_name:
            messagebox.showwarning(
                "Missing Task",
                "Please enter a task.",
                parent=task_window
            )
            return

        database.add_task(task_name)
        entry.delete(0, tk.END)
        refresh_tasks()

    def mark_completed():
        selection = task_list.curselection()

        if not selection:
            messagebox.showwarning(
                "Select Task",
                "Please select a task first.",
                parent=task_window
            )
            return

        task_id = task_ids[selection[0]]

        for saved_id, task_name, completed in database.get_tasks():
            if saved_id == task_id:
                database.update_task(task_id, not completed)
                break

        refresh_tasks()

    def delete_selected_task():
        selection = task_list.curselection()

        if not selection:
            messagebox.showwarning(
                "Select Task",
                "Please select a task to delete.",
                parent=task_window
            )
            return

        task_id = task_ids[selection[0]]

        confirm = messagebox.askyesno(
            "Confirm Delete",
            "Are you sure you want to delete this task?",
            parent=task_window
        )

        if confirm:
            database.delete_task(task_id)
            refresh_tasks()

    tk.Button(
        task_window,
        text="Add Task",
        command=add_new_task,
        bg="#23395d",
        fg="white",
        font=("Arial", 11, "bold"),
        padx=15
    ).pack(pady=5)

    tk.Button(
        task_window,
        text="Toggle Complete",
        command=mark_completed,
        bg="#287a50",
        fg="white",
        font=("Arial", 11, "bold"),
        padx=15
    ).pack(pady=5)

    tk.Button(
        task_window,
        text="Delete Selected Task",
        command=delete_selected_task,
        bg="#b83232",
        fg="white",
        font=("Arial", 11, "bold"),
        padx=15
    ).pack(pady=5)

    refresh_tasks()


# =====================================
# RECOMMENDATIONS
# =====================================

def open_recommendations():
    window = tk.Toplevel(root)
    window.title("PlaceReady - Recommendations")
    window.geometry("650x450")
    window.configure(bg="#f3f6fb")

    tk.Label(
        window,
        text="Personalized Recommendations",
        font=("Arial", 18, "bold"),
        fg="#23395d",
        bg="#f3f6fb"
    ).pack(pady=20)

    output = tk.Text(
        window,
        font=("Arial", 11),
        width=65,
        height=15,
        wrap="word"
    )
    output.pack(padx=20, pady=10, fill="both", expand=True)

    advice = {
        "Coding": "Practice Python functions, loops, lists, and problem-solving.",
        "SQL": "Revise SELECT, WHERE, JOIN, GROUP BY, and aggregate functions.",
        "Aptitude": "Practice percentages, ratios, time and work, and number series.",
        "Communication": "Improve interview answers, listening, and professional email writing."
    }

    records = database.get_assessments()

    if not records:
        output.insert(
            tk.END,
            "Complete a skill assessment to receive recommendations."
        )
    else:
        latest = {}

        for category, score, total, date in records:
            if category not in latest:
                latest[category] = (score, total)

        for category, (score, total) in latest.items():
            percentage = score / total * 100 if total else 0

            output.insert(
                tk.END,
                f"{category}: {score}/{total} ({percentage:.0f}%)\n"
            )

            if percentage < 50:
                output.insert(
                    tk.END,
                    "Priority: Focus on the fundamentals.\n"
                )
            elif percentage < 80:
                output.insert(
                    tk.END,
                    "Priority: Practise regularly to improve.\n"
                )
            else:
                output.insert(
                    tk.END,
                    "Priority: Keep practising advanced questions.\n"
                )

            output.insert(tk.END, advice[category] + "\n\n")

    output.config(state="disabled")


# =====================================
# DASHBOARD BUTTONS
# =====================================

tk.Button(
    content,
    text="Start Skill Assessment",
    command=open_assessment,
    bg="#287a50",
    fg="white",
    font=("Arial", 12, "bold"),
    padx=20,
    pady=10
).pack(pady=20)

tk.Button(
    content,
    text="View Assessment History",
    command=open_history,
    bg="#23395d",
    fg="white",
    font=("Arial", 11, "bold"),
    padx=15,
    pady=8
).pack(pady=5)

tk.Button(
    content,
    text="Practice Tasks",
    command=open_tasks,
    bg="#6b4ca5",
    fg="white",
    font=("Arial", 11, "bold"),
    padx=15,
    pady=8
).pack(pady=5)

tk.Button(
    content,
    text="View Recommendations",
    command=open_recommendations,
    bg="#c07825",
    fg="white",
    font=("Arial", 11, "bold"),
    padx=15,
    pady=8
).pack(pady=5)

# =====================================
# STATUS BAR
# =====================================

tk.Label(
    root,
    text="PlaceReady Python Edition | Ready to begin",
    font=("Arial", 10),
    fg="#4b5563",
    bg="#e5ebf4",
    anchor="w",
    padx=15,
    pady=10
).pack(fill="x", side="bottom")

# =====================================
# RUN APPLICATION
# =====================================

root.mainloop()
