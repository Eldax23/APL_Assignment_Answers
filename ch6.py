import pandas as pd
import csv
import json

# 1
with open("students.csv", mode="r") as file:
    reader = csv.DictReader(file)    
    for row in reader:
        if int(row["Grade"]) > 80:
            print(row["Name"])


#----------------------------------------------------------

# 2

data = {
    "course": "Python",
    "duration": "3 months",
    "students": ["Ali", "Sara"]
}
with open("course.json", "w") as file:
    json.dump(data, file, indent=4)
with open("course.json", "r") as file:
    loaded_data = json.load(file)



print(loaded_data["students"])

# -------------------------------------------------
# 3


data = {
    "ID": [1, 2, 3],
    "Name": ["Ali", "Mona", "Omar"],
    "Salary": [5000, 6200, 4800]
}

df = pd.DataFrame(data)
df.to_excel("employees.xlsx", index=False)
loaded_df = pd.read_excel("employees.xlsx")
print(loaded_df[["Name", "Salary"]])

# -----------------------------------------------------
# 4

def csv_to_json(csv_file, json_file):
    data = {"people": []}
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            row["Age"] = int(row["Age"])
            data["people"].append(row)
    with open(json_file, 'w') as file:
        json.dump(data, file)
