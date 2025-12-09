# problem 1
import numpy as nmpy
import torch
import matplotlib.pyplot as plt
import pandas as pd
from flask import Flask
array = nmpy.arrange(1, 20)
print("mean:", nmpy.mean(array))
print("standard deviation:", nmpy.std(array))
print("median:", nmpy.median(array))


#-----------------------------------------------------

# problem 2

data = {
    "Name": ["Nada", "Nadine", "Eyad", "Ahmed"],
    "Age": [18 , 20 , 19 , 23],
    "Score": [20, 30, 85, 90]
}
df = pd.DataFrame(data)
result=df[df["score"] > 80]
print(result)

#--------------------------------------------------

# problem 3

x = [1,2,3,4,5]
y = [1,4,9,16,25]
plt.plot(x, y)
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.title("equivalent square numbers")
plt.show()

#-------------------------------------------------

# problem 4

app = Flask(__name__)
@app.route('/hello')
def hello():
    return "Hello, Advanced Python!"
if __name__ == "__main__":
    app.run()

#--------------------------------------------
# Problem 5:
t1 = torch.tensor([1,2,3])
t2 = torch.tensor([4,5,6])
dot = torch.dot(t1, t2)
mul = t1 * t2
print("dot product:", dot)
print("per element multiplication:", mul)

