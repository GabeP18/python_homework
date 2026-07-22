#Task 2: Read a CSV File
import csv
import traceback

def read_employees():
    employees_dict = {}
    rows = []

    try:
        with open("../csv/employees.csv", "r") as employee_file:
            employee_reader = csv.reader(employee_file)
            first_row = True

            for row in employee_reader:
                if first_row:
                    employees_dict["fields"] = row
                    first_row = False
                else:
                    rows.append(row)
            employees_dict["rows"] = rows

    except Exception as e:
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = list()

        for trace in trace_back:
            stack_trace.append(
                f"File : {trace[0]} , Line : {trace[1]}, "
                f"Func.Name : {trace[2]}, Message : {trace[3]}"
            )
        print(f"Exception type: {type(e).__name__}")
        message = str(e)
        if message:
            print(f"Exception message: {message}")
        print(f"Stack trace: {stack_trace}")

    return employees_dict

employees = read_employees()
print(employees)

#Task 3: Find the Column Index
def column_index(column_name):
    return employees["fields"].index(column_name)

employee_id_column = column_index("employee_id")

#Task 4: Find the Employee First Name
def first_name(row_number):
    first_name_column = column_index("first_name")
    return employees["rows"][row_number][first_name_column]

#Task 5: Find the Employee: a Function in a Function
def employee_find(employee_id):

    def employee_match(row):
        return int(row[employee_id_column]) == employee_id
    matches = list(filter(employee_match, employees["rows"]))

    return matches

#Task 6: Find the Employee with a Lambda
def employee_find_2(employee_id):
    matches = list(
        filter(
            lambda row: int(row[employee_id_column]) == employee_id,
            employees["rows"]
        )
    )
    return matches

#Task 7: Sort the Rows by last_name Using a Lambda
def sort_by_last_name():
    last_name_column = column_index("last_name")

    employees["rows"].sort(
        key=lambda row: row[last_name_column]
    )
    return employees["rows"]

sort_by_last_name()
print(employees)

#Task 8: Create a dict for an Employee
def employee_dict(row):
    employee = {}

    for index in range(len(employees["fields"])):
        field_name = employees["fields"][index]

        if field_name != "employee_id":
            employee[field_name] = row[index]

    return employee
print(employee_dict(employees["rows"][0]))

#Task 9: A dict of dicts, for All Employees
def all_employees_dict():
    all_employees = {}

    for row in employees["rows"]:
        employee_id = row[employee_id_column]
        all_employees[employee_id] = employee_dict(row)

    return all_employees

all_employees = all_employees_dict()
print(all_employees)

#Task 10: Use the os Module
import os

def get_this_value():
    return os.getenv("THISVALUE")

#Task 11: Creating Your Own Module
import custom_module

def set_that_secret(new_secret):
    custom_module.set_secret(new_secret)

set_that_secret("surprise!")
print(custom_module.secret)

#Task 12: Read minutes1.csv and minutes2.csv
def read_minutes():
    minutes1 = {}
    minutes2 = {}

    minutes1_rows = []
    minutes2_rows = []

    try:
        with open("../csv/minutes1.csv", "r") as minutes1_file:
            minutes1_reader = csv.reader(minutes1_file)
            first_row = True

            for row in minutes1_reader:
                if first_row:
                    minutes1["fields"] = row
                    first_row = False
                else:
                    minutes1_rows.append(tuple(row))
            minutes1["rows"] = minutes1_rows

        with open("../csv/minutes2.csv", "r") as minutes2_file:
            minutes2_reader = csv.reader(minutes2_file)
            first_row = True

            for row in minutes2_reader:
                if first_row:
                    minutes2["fields"] = row
                    first_row = False
                else:
                    minutes2_rows.append(tuple(row))
            minutes2["rows"] = minutes2_rows

    except Exception as e:
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = list()

        for trace in trace_back:
            stack_trace.append(
                f"File : {trace[0]} , Line : {trace[1]}, "
                f"Func.Name : {trace[2]}, Message : {trace[3]}"
            )
        print(f"Exception type: {type(e).__name__}")

        message = str(e)

        if message:
            print(f"Exception message: {message}")

        print(f"Stack trace: {stack_trace}")

    return minutes1, minutes2

minutes1, minutes2 = read_minutes()

print(minutes1)
print(minutes2)

#Task 13: Create minutes_set
def create_minutes_set():
    minutes1_set = set(minutes1["rows"])
    minutes2_set = set(minutes2["rows"])

    combined_set = minutes1_set.union(minutes2_set)

    return combined_set

minutes_set = create_minutes_set()
print(minutes_set)

#Task 14: Convert to datetime
from datetime import datetime

def create_minutes_list():
    minutes_rows = list(minutes_set)

    minutes_datetime_list = list(
        map(
            lambda row: (
                row[0],
                datetime.strptime(row[1], "%B %d, %Y")
            ),
            minutes_rows
        )
    )
    return minutes_datetime_list

minutes_list = create_minutes_list()
print(minutes_list)

#Task 15: Write Out Sorted List
def write_sorted_list():
    minutes_list.sort(key=lambda row: row[1])

    converted_minutes = list(
        map(
            lambda row: (
                row[0],
                datetime.strftime(row[1], "%B %d, %Y")
            ),
            minutes_list
        )
    )
    try:
        with open("./minutes.csv", "w", newline="") as minutes_file:
            minutes_writer = csv.writer(minutes_file)
            minutes_writer.writerow(minutes1["fields"])
            minutes_writer.writerows(converted_minutes)

    except Exception as e:
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = list()

        for trace in trace_back:
            stack_trace.append(
                f"File : {trace[0]} , Line : {trace[1]}, "
                f"Func.Name : {trace[2]}, Message : {trace[3]}"
            )
        print(f"Exception type: {type(e).__name__}")

        message = str(e)

        if message:
            print(f"Exception message: {message}")
            
        print(f"Stack trace: {stack_trace}")
    return converted_minutes

sorted_minutes = write_sorted_list()
print(sorted_minutes)