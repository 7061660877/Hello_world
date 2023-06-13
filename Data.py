'''import matplotlib.pyplot as plt
x=['Math','English','Hindi']
y=[56,70,90]
plt.plot(x,y)
plt.xlabel('subject')
plt.ylabel('marks')
plt.title('marks Graph')
plt.show()
'''
'''from matplotlib import pyplot as plt    
    
x = [1,2,3]    
y = [10,11,12]    
    
plt.plot(x,y)    
    
plt.title("Line graph")    
plt.ylabel('Y axis')    
plt.xlabel('X axis')    
plt.show()    '''
'''from matplotlib import pyplot as plt    
from matplotlib import style    
    
style.use('ggplot')    
x = [10, 12, 13]    
y = [8, 16, 6]    
x2 = [8, 15, 11]    
y2 = [6, 15, 7]    
plt.plot(x, y, 'b', label='line one', linewidth=5)    
plt.plot(x2, y2, 'r', label='line two', linewidth=5)    
plt.title('Epic Info')    
fig = plt.figure()    
plt.ylabel('Y axis')    
plt.xlabel('X axis')    
  
plt.show()  '''
'''from matplotlib import pyplot as plt    
Names = ['Anant Raj','Raju','Manish','Rohit']    
Marks = [90,87,45,67]    
plt.bar(Names,Marks,color = 'blue')    
plt.title('Result')    
plt.xlabel('Names')    
plt.ylabel('Marks')    
plt.show()''' 
'''from matplotlib import pyplot as plt    
    
# Pie chart, where the slices will be ordered and plotted counter-clockwise:    
Aus_Players = 'Anant Raj', 'Raju', 'Rohan', 'Amit'    
Runs = [92, 78, 58, 44]    
explode = (0.1, 0, 0, 0)  # it "explode" the 1st slice     
    
fig1, ax1 = plt.subplots()    
ax1.pie(Runs, explode=explode, labels=Aus_Players, autopct='%1.1f%%',    
        shadow=True, startangle=90)    
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.    
    
plt.show()'''  
'''from matplotlib import pyplot as plt    
from matplotlib import pyplot as plt    
percentage = [97,54,45,10, 20, 10, 30,97,50,71,40,49,40,74,95,80,65,82,70,65,55,70,75,60,52,44,43,42,45]    
number_of_student = [0,10,20,30,40,50,60,70,80,90,100]    
plt.hist(percentage, number_of_student, histtype='bar', rwidth=0.8)    
plt.xlabel('percentage')    
plt.ylabel('Number of people')    
plt.title('Histogram')    
plt.show()    '''   
'''from matplotlib import pyplot as plt    
# Importing Numpy Library    
import numpy as np    
plt.style.use('fivethirtyeight')    
    
mu = 50    
sigma = 7    
x = np.random.normal(mu, sigma, size=200)    
fig, ax = plt.subplots()    
    
ax.hist(x, 20)    
ax.set_title('Historgram')    
ax.set_xlabel('bin range')    
ax.set_ylabel('frequency')    
    
fig.tight_layout()    
plt.show() '''
'''from matplotlib import pyplot as plt    
from matplotlib import style    
style.use('ggplot')    
    
x = [4,8,12]    
y = [19,11,7]    
    
x2 = [7,10,12]    
y2 = [8,18,24]    
    
plt.scatter(x, y)    
    
plt.scatter(x2, y2, color='g')    
    
plt.title('Epic Info')    
plt.ylabel('Y axis')    
plt.xlabel('X axis')    
    
plt.show()       '''
'''import matplotlib.pyplot as plt    
a = [2, 2.5, 3, 3.5, 4.5, 4.7, 5.0]  
b = [7.5, 8, 8.5, 9, 9.5, 10, 10.5]    
    
a1 = [9, 8.5, 9, 9.5, 10, 10.5, 12]    
b1 = [3, 3.5, 4.7, 4, 4.5, 5, 5.2]    
plt.scatter(a, b, label='high income low saving', color='b')    
plt.scatter(a1, b1, label='low income high savings', color='g')    
plt.xlabel('saving*100')    
plt.ylabel('income*1000')    
plt.title('Scatter Plot')    
plt.legend()    
plt.show()    '''
'''import matplotlib.pyplot as plt
x=['English','Hindi','Math','Science','History']
y=[90,78,99,89,67]
plt.bar(x,y,)
plt.xlabel('Subjects')
plt.ylabel('Marks')
plt.show()'''
'''from tkinter import  messagebox
from tkinter import *
top = Tk()
#window dimension
top.geometry("300x180")
top['bg']="#51E1DC"
#defining function
def add():
    f=firstNum.get()
    s=secondNum.get()
    messagebox.showinfo("Sum",(f+s))
#declaring variables
firstNum=IntVar()
secondNum=IntVar()
#create labels
Label(top, text="First Number",width="13").place(x=50,y=50)
Label(top, text="Second Number",width="13").place(x=50,y=90)
#create text boxes
Entry(top,textvariable=firstNum).place(x=150,y=50)
Entry(top,textvariable=secondNum).place(x=150,y=90)
#create button
Button(top,text="Add",width="5",bg="orange",command=add).place(x=100,y=120)
top.mainloop()'''
'''import pandas as pd
var1 = pd.DataFrame({"A":[1,2,3,4],"B":[11,12,13,14]})
var2 = pd.DataFrame({"A":[1,2,3,5],"C":[21,22,23,24]})
print(pd.merge(var1,var2,how="outer",indicator=True))'''
'''d1=pd.DataFrame({"A":[1,2,3,4],"B":[11,12,13,14]})
d2=pd.DataFrame({"A":[1,2,3,5],"C":[21,22,23,24]})
pd.concat([d1,d2],axis=1,keys=["d1","d2"])
print(pd.concat([d1,d2],axis=1,keys=["d1","d2"]))'''
'''import turtle
turtle.pencolor("red")
turtle.pensize(5)
turtle.shape("turtle")
turtle.color("yellow","green")
for i in range(0,360,1):
    turtle.forward(1)
    turtle.right(1)
turtle.bgcolor("black")
turtle.done()  '''

# sun making using turtle
'''from turtle import*
import turtle 
color('orange','yellow')
turtle.bgcolor("black")
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos())<1:
        break
end_fill()
done()'''
# Making Design with multiple color pentagone shape with 3 d
'''import  turtle
import  time
def myFun():
    colors=["red","blue","green","yellow","orange","brown"]
    t=turtle
    t.pensize(5)
    t.bgcolor('black')
    t.speed(1000)
    for x in range(360):
        t.pencolor(colors[x%len(colors)])
        t.pensize(x/50)
        t.forward(x)
        t.left(59)
myFun()
time.sleep(5)'''
# Makin Circle using turtle with Multiple circle 
import turtle 
import colorsys
t = turtle.Turtle()
s = turtle.Screen().bgcolor('black')
t.speed(0)
n = 70
h = 0
for i in range(360):
    c = colorsys.hsv_to_rgb(h,1,0.8)
    h+=1/n
    t.color(c)
    t.left(1)
    t.fd(1)
    for j in range(2):
        t.left(2)
    t.circle(100)

