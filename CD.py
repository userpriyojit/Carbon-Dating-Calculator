# Import Module
import tkinter as tk
from tkinter.ttk import *
import numpy as np
import matplotlib.pyplot as plt

# p=float(input())
p1=-1
k1=-1
r1=-1
t1=-1

# p=float(num1.get())
# k= np.log(2)/5730
# r=p/100
# t=-(np.log(r)/k)


# --- functions ---

def generate():
    try:
        global p
        p=float(num1.get())
        if ((p>= 0) and (p<= 100)):
          k= np.log(2)/5730
          r=p/100
          t=-(np.log(r)/k)
          result=np.round(t)
          global p1, k1, r1, t1
          p1 = p
          k1 = k
          r1 = r
          t1 = t
        else:
          print("Sorry, input should be between 0 - 100")
          result = 'Error!Try again!'
          num3.set(result)
          return()
        
        #if ((p1>= 0) and (p<= 100)):
#        p1 = p
#        k1 = k
#        r1 = r
#        t1 = t
        print("Within generate ", p1, k1, r1, t1)

    except Exception as ex:
        print(ex)
        result = 'error'
    num3.set(result)

# graph
def f(x):
  return((-np.log(x/100)/k1))

def graphPlot():
    x=[]
    for i in range(0,101):
      x.append(f(i))

    print("Within graphPlot ", p1, k1, r1, t1)

    if (p1 != -1 and p>=0 and p<=100 and k1 != -1 and r1 != -1 and t1 != -1):
        y=np.linspace(0,100,101)
        plt.plot(x,y,'r--')
        plt.grid()
        plt.xlabel("Time(years)")
        plt.ylabel("Amount of c-14 remaining(%)")
        plt.annotate('This is the decay state of the sample',xytext=(t1+3000,p1+15),xy=(t1,p1),arrowprops={'facecolor':'black'})
        plt.title("Decay of C-14")
        plt.show()
        print("The age of your sample is : \n", np.round(t1),"years")



# --- main ---

# create root window
root = tk.Tk()

# root window title and dimension
root.title(" Carbon-Dating-Calculator")
# Set geometry(widthxheight)
root.geometry('600x300')
root.option_add('*Font', 'Arial,sans-serif')
root.configure(bg='#222')

# # Add a frame to set the size of the window
# innerFrame = tk.Frame(root, bg="red")
# innerFrame.pack(ipadx=15, ipady=15, fill="both", expand=True)




# adding a label to the root window

label1 = tk.Label(root, text="Enter the percentage of C-14 remaining in your sample", bg="#222", foreground="red").grid(row = 0, column = 0, pady = 2)

tk.Label(root, text="The age of your sample is :", bg="#222", foreground="white").grid(row = 2, column = 0, pady = 10, sticky = 'W')
tk.Label(root, text="years", bg="#222", foreground="white").grid(row = 2, column = 3, pady = 10, sticky = 'W')

num1 = tk.StringVar()
num3 = tk.StringVar()
tk.Entry(root, textvariable=num1).grid(row = 1, column = 0, pady = 10, sticky = 'W')
tk.Entry(root, textvariable=num3,state='disabled').grid(row = 2, column = 0, pady = 10, sticky = 'E')

#button
button = tk.Button(root, text="Calculate", command=generate,activebackground='green',activeforeground='white',bg='yellow')
button.grid(row = 3, column = 0, pady = 10, sticky = 'W')

button = tk.Button(root, text="Press to visualize the Graph", command=graphPlot,activebackground='green',activeforeground='white',bg='#ff9f00')
button.grid(row = 4, column = 0, pady = 10, sticky = 'W')

root.mainloop()
