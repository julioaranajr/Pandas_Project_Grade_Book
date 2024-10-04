"""Generate random data for the project."""

from dataclasses import asdict
from dataclasses import dataclass
from dataclasses import field
from pathlib import Path
from random import choice
from random import seed as py_rand_seed
from typing import Optional

from dateutil import parser
from dateutil import rrule

from faker import Faker

import numpy

import pandas as pd


fake = Faker()

seed = 11111
fake.seed_instance(seed)
py_rand_seed(seed)
rg = numpy.random.default_rng(seed)

HERE = Path(__file__).parent


def get_section():
    """Return a random section number."""
    return rg.integers(1, 3, endpoint=True)


def get_psid():
    """Return a random 7-digit PSID."""
    return rg.integers(1000000, 9999999, endpoint=True)


def get_middle_name():
    """Return a random middle name or None."""
    return choice([None, fake.first_name()])


@dataclass
class Student:
    """The attributes of this class describe a student at Univ."""

    first_name: str = field(default_factory=fake.first_name)
    last_name: str = field(default_factory=fake.last_name)
    psid: int = field(default_factory=get_psid)
    section: int = field(default_factory=get_section)
    middle_name: Optional[str] = field(default_factory=get_middle_name)
    modifier: Optional[str] = None
    netid: Optional[str] = None
    email: Optional[str] = None
    full_name: str = field(init=False)

    def __post_init__(self):
        """Create attributes that depend on other attributes."""
        m = self.middle_name[0].lower() if self.middle_name is not None else "x"
        if self.netid is None:
            self.netid = f"{self.first_name[0].lower()}{m}{self.last_name[0].lower()}"
            self.netid += "".join(map(str, rg.integers(10, size=5)))
        if self.email is None:
            self.email = (
                f"{self.first_name.lower()}.{self.last_name.lower()}@dci-student.edu"
            )

        assert (
            len(str(self.psid)) == 7
        ), f"PSID not 7 digits for {self.first_name} {self.last_name}"

        self.full_name = f"{self.last_name}"
        if self.modifier is not None:
            self.full_name += f" {self.modifier}, "
        else:
            self.full_name += ", "
        self.full_name += self.first_name
        if self.middle_name is not None:
            self.full_name += f" {self.middle_name}"


# These 4 students are used as examples in the tutorial, so they're
# manually generated.

students = [
    Student(
        "Woody",
        "Barrera",
        1234567,
        modifier="Jr.",
        email="woody.barrera_jr@dci-student.edu",
        netid="wxb12345",
        section=1,
        middle_name=None,
    ),
    Student(
        "Malaika",
        "Lambert",
        2345678,
        middle_name=None,
        netid="mxl12345",
        section=2,
    ),
    Student(
        "Traci",
        "Joyce",
        3456789,
        middle_name=None,
        netid="txj12345",
        section=1,
    ),
    Student(
        "John",
        "Flower",
        4567890,
        middle_name="Gregg",
        email="john.g.2.flower@dci-student.edu",
        netid="jgf12345",
        section=3,
    ),
]

n_students = 150
n_fake_students = n_students - len(students)
students.extend(Student() for _ in range(n_fake_students))

n_homeworks = 10
n_exams = 3
n_quizzes = 5
quiz_max_scores = rg.integers(10, 20, size=n_quizzes)
quiz_min_scores = quiz_max_scores * 0.4
hw_max_scores = rg.integers(5, 10, size=n_homeworks, endpoint=True) * 10
hw_min_scores = hw_max_scores * 0.6
homework_sub_time = list(
    rrule.rrule(
        rrule.WEEKLY,
        count=n_homeworks,
        dtstart=parser.parse("2024-07-29 09:56:02 -0700"),
    )
)
exam_sub_time = list(
    rrule.rrule(
        rrule.MONTHLY,
        count=n_exams,
        dtstart=parser.parse("2024-09-08 10:30:05 -0700"),
    )
)

df = pd.concat(
    [
        pd.DataFrame([asdict(x) for x in students]),
        pd.DataFrame(
            rg.integers(
                hw_min_scores,
                hw_max_scores,
                endpoint=True,
                size=(len(students), n_homeworks),
            ),
            columns=[f"Homework {n}" for n in range(1, n_homeworks + 1)],
        ),
        pd.DataFrame(
            numpy.repeat(hw_max_scores.reshape(1, -1), len(students), axis=0),
            columns=[f"Homework {n} Max Points" for n in range(1, n_homeworks + 1)],
        ),
        pd.DataFrame(
            [homework_sub_time] * len(students),
            columns=[
                f"Homework {n} Submission Time" for n in range(1, n_homeworks + 1)
            ],
        ),
        pd.DataFrame(
            rg.integers(60, 100, endpoint=True, size=(len(students), n_exams)),
            columns=[f"Exam {n}" for n in range(1, n_exams + 1)],
        ),
        pd.DataFrame(
            numpy.ones((len(students), n_exams), dtype=numpy.int64) * 100,
            columns=[f"Exam {n} Max Points" for n in range(1, n_exams + 1)],
        ),
        pd.DataFrame(
            [exam_sub_time] * len(students),
            columns=[f"Exam {n} Submission Time" for n in range(1, n_exams + 1)],
        ),
        pd.DataFrame(
            rg.integers(
                quiz_min_scores,
                quiz_max_scores,
                endpoint=True,
                size=(len(students), n_quizzes),
            ),
            columns=[f"Quiz {n} Grade" for n in range(1, n_quizzes + 1)],
        ),
    ],
    axis=1,
)

roster = (
    df[["psid", "full_name", "netid", "email", "section"]]
    .rename(
        columns={
            "psid": "ID",
            "full_name": "Name",
            "netid": "NetID",
            "email": "Email Address",
            "section": "Section",
        }
    )
    .set_index("ID")
)
roster["Email Address"] = roster["Email Address"].str.upper()
roster["NetID"] = roster["NetID"].str.upper()
roster.to_csv(HERE / "roster_table.csv")

hw_exam_grades = df.filter(
    regex="^first_name$|^last_name$|^netid$|^Homework.*|^Exam.*"
).rename(
    columns={
        "netid": "SID",
        "first_name": "First Name",
        "last_name": "Last Name",
    }
)
hw_exam_cols = ["First Name", "Last Name", "SID"]
for n in range(1, n_homeworks + 1):
    hw_exam_cols.append(f"Homework {n}")
    hw_exam_cols.extend(f"Homework {n} {s}" for s in ["Max Points", "Submission Time"])
for n in range(1, n_exams + 1):
    hw_exam_cols.append(f"Exam {n}")
    hw_exam_cols.extend(f"Exam {n} {s}" for s in ["Max Points", "Submission Time"])

hw_exam_grades = hw_exam_grades[hw_exam_cols]
hw_exam_grades = hw_exam_grades.sort_values(by="First Name")

# Munge some of the data to show different things in the article
hw_exam_grades.loc[hw_exam_grades["SID"] == "jgf12345", "First Name"] = "Gregg"
hw_exam_grades.loc[hw_exam_grades["SID"] == "txj12345", "Homework 1"] = numpy.nan

hw_exam_grades.to_csv(HERE / "homework_exam_grades.csv", index=False)

for col in range(1, n_quizzes + 1):
    df[["last_name", "first_name", "email", f"Quiz {col} Grade"]].rename(
        columns={
            "first_name": "First Name",
            "last_name": "Last Name",
            "email": "Email Address",
            "Quiz 1 Grade": "Grade",
            "Quiz 2 Grade": "Grade",
            "Quiz 3 Grade": "Grade",
            "Quiz 4 Grade": "Grade",
            "Quiz 5 Grade": "Grade",
        }
    ).sample(frac=1, random_state=col).to_csv(
        HERE / f"quiz_{col}_grades.csv", index=False
    )

print(dict(zip((f"Quiz {n}" for n in range(1, n_quizzes + 1)), quiz_max_scores)))
