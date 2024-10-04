![Pandas_Project_Grade_Book](https://socialify.git.ci/julioaranajr/Pandas_Project_Grade_Book/image?description=1&font=Source%20Code%20Pro&forks=1&issues=1&language=1&name=1&owner=1&pattern=Solid&pulls=1&stargazers=1&theme=Dark)

# Pandas Project Grade Book

Gradebook With Python &amp; pandas

## Table of Contents

- **What We are going to build**
- **Project Overview**
- **01-loading-the-data**
- **02-merging-the-dataframes**
- **03-calculating-the-grades**
- **04-grouping-the-data**
- **05-plotting-summary-statistics**
- **06-final-gradebook**
- **Conclusion**

## What We are going to build

In this project, we are going to build a Gradebook using Python and pandas. We’ll use pandas and numpy to load and manipulate the data, and matplotlib to create visualizations. Also we are going to use Jupyter Notebook with iTables to display the data and the results.

iTables is a Jupyter Notebook extension that allows us to create interactive tables. We can sort, filter, and search the data in the table. This is a great way to explore the data and see the results of your calculations.

## Project Overview

One of the jobs that all teachers have in common is evaluating students. Whether you use exams, homework assignments, quizzes, or projects, you usually have to turn students’ scores into a letter grade at the end of the term. This often involves a bunch of calculations that you might do in a spreadsheet. Instead, you can consider using Python and pandas.

One problem with using a spreadsheet is that it can be hard to see when you make a mistake in a formula. Maybe you selected the wrong column and put quizzes where exams should go. Maybe you found the maximum of two incorrect values. To solve this problem, you can use Python and pandas to do all our calculations and find and fix those mistakes much faster.

In this tutorial, we’ll learn how to:

- Load and merge data from multiple sources with pandas
- Filter and group data in a pandas DataFrame
- Calculate and plot grades in a pandas DataFrame

This pandas project involves four main steps:

- Explore the data we’ll use in the project to determine which format and data we’ll need to calculate your final grades.
- Load the data into pandas DataFrames, making sure to connect the grades for the same student across all your data sources.
- Calculate the final grades and save them as CSV files.
- Plot the grade distribution and explore how the grades vary among your students.

Once you complete these steps, we’ll have a working Python script that can calculate our grades. Our grades will be in a format that you should be able to upload to your school’s student administration system.

## 01-loading-the-data

In this section, we’ll load the data we need to calculate the final grades. We’ll use pandas to load the data from CSV files and merge the data into a single DataFrame.

we need to import the `pandas library` and the `Path class` from the `pathlib module`. The Path class allows us to work with file paths in a platform-independent way.

`pd.read_csv(file)` is a function that reads a CSV file and returns a DataFrame. We’ll use this function to load the data from the CSV files.

With the `lambda function` we pass here, if the string `"Submission"` appears in the column name, then the column will be excluded.

We use `Path.glob()` to find all the quiz CSV files and load them with pandas, making sure to convert the email addresses to lowercase. We also set the index column for each quiz to the `students’ email addresses`, which `pd.concat()` uses to align data for each student.

Notice that we pass `axis=1` to `pd.concat()`. This causes pandas to concatenate columns rather than rows, adding each new quiz into a new column in the combined DataFrame.

Finally, you use `DataFrame.rename()` to change the name of the grade column from Grade to something specific to each quiz.

[01-loading-the-data](01-loading-the-data.py)

## 02-merging-the-dataframes

In this section, we’ll merge the data from the different CSV files into a single DataFrame.

We’ll merge the data together in two steps:

- Merge roster and hw_exam_grades together into a new DataFrame called final_data.
- Merge final_data and quiz_grades together.

We’ll use different columns in each DataFrame as the merge key, which is how pandas determines which rows to keep together. This process is necessary because each data source uses a different unique identifier for each student.

[02-merging-the-dataframes](02-merging-dataframes.py)

## 03-calculating-the-grades

In this section, we’ll calculate the final grades for each student. We’ll use the data we loaded in the previous section to calculate the final grades.

[03-calculating-the-grades](03-calculating-grades.py)

## 04-grouping-the-data

In this section, we’ll group the data by the final grade and count the number of students in each grade. We’ll use the pandas groupby function to group the data by the final grade and count the number of students in each grade.

[04-grouping-the-data](04-grouping-the-data.py)

## 05-plotting-summary-statistics

In this section, we’ll plot the summary statistics for the final grades. We’ll use the matplotlib library to create a bar chart that shows the number of students in each grade.

[05-plotting-summary-statistics](05-plotting-summary-statistics.py)

## 06-final-gradebook

In this section, we’ll create a final gradebook that contains the final grades for each student. We’ll save the final gradebook as a CSV file that you can upload to your school’s student administration system.

[06-final-gradebook](06-final-gradebook.py)

## Jupyter Notebook

You can run the code in a Jupyter Notebook. You can install Jupyter Notebook in your VS Code or use Google Colab.

[Gradebook With Python & pandas](grade_book.ipynb)

With iTabels you can display the data and the results in a table. Also you can sort, filter, and search the data in the table and save the results as a CSV file.

## Conclusion

In this project, we learned how to use Python and pandas to create a gradebook. We loaded the data from multiple CSV files, merged the data into a single DataFrame, calculated the final grades, and plotted the summary statistics. We also created a final gradebook that you can upload to our school’s student administration system.

I hope you enjoyed this project and learned something new.

If you have any questions or comments, please leave them in the comments below. Thanks for reading!

Happy coding!
