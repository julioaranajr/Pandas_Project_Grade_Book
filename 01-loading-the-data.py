"""Calculate student grades by combining data from many sources.

Using Pandas, this script combines data from the:

* Roster
* Homework & Exam grades
* Quiz grades

to calculate final grades for a class.
"""

from pathlib import Path

import pandas as pd


HERE = Path(__file__).parent
DATA_FOLDER = HERE / "data"

# ----------------------
# 01 - LOADING THE DATA
# ----------------------

roster = pd.read_csv(
    DATA_FOLDER / "roster_table.csv",
    converters={"NetID": str.lower, "Email Address": str.lower},
    usecols=["Section", "Email Address", "NetID"],
    index_col="NetID",
)

hw_exam_grades = pd.read_csv(
    DATA_FOLDER / "homework_exam_grades.csv",
    converters={"SID": str.lower},
    usecols=lambda x: "Submission" not in x,
    index_col="SID",
)

quiz_grades = pd.DataFrame()
for file_path in DATA_FOLDER.glob("quiz_*_grades.csv"):
    quiz_name = " ".join(file_path.stem.title().split("_")[:2])
    quiz = pd.read_csv(
        file_path,
        converters={"Email Address": str.lower},
        index_col=["Email Address"],
        usecols=["Email Address", "Grade"],
    ).rename(columns={"Grade": quiz_name})
    quiz_grades = pd.concat([quiz_grades, quiz], axis=1)

print("\nLoading data...\n")
print("Done!")

print("\nRoster table:")
df_roster = pd.read_csv(DATA_FOLDER / "roster_table.csv")
print(df_roster, 5)

print("Homework and exam grades:")
df_hw_exam_grades = pd.read_csv(DATA_FOLDER / "homework_exam_grades.csv")
print(df_hw_exam_grades, 5)

print("Quiz grades 1:")
df1_quiz_grades = pd.read_csv(DATA_FOLDER / "quiz_1_grades.csv")
print(df1_quiz_grades, 5)

print("Quiz grades 2:")
df2_quiz_grades = pd.read_csv(DATA_FOLDER / "quiz_2_grades.csv")
print(df2_quiz_grades, 5)

print("Quiz grades 3:")
df3_quiz_grades = pd.read_csv(DATA_FOLDER / "quiz_3_grades.csv")
print(df3_quiz_grades, 5)

print("Quiz grades 4:")
df4_quiz_grades = pd.read_csv(DATA_FOLDER / "quiz_4_grades.csv")
print(df4_quiz_grades, 5)

print("Quiz grades 5:")
df5_quiz_grades = pd.read_csv(DATA_FOLDER / "quiz_5_grades.csv")
print(df5_quiz_grades, 5)
