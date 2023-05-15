import matplotlib.pyplot as plt

x = [10, 15,20,21,22,23,25,30,40,50,100]
y1 = [0.3272, 0.3964, 0.3568, 0.3542, 0.3811, 0.3592, 0.3859, 0.4059, 0.4811, 0.4941, 0.7976]
y2 = [0.8855, 0.8626, 0.8881, 0.8844, 0.8863, 0.8891, 0.8878, 0.8846, 0.8875, 0.8916, 0.8858]

plt.plot(x, y1, label='Функция потерь')

plt.plot(x, y2, label='Точность')

# naming the x axis
plt.xlabel('Эпохи')
# naming the y axis
plt.ylabel('')
  
# giving a title to my graph
#plt.title('My first graph!')
  
# function to show the plot
plt.legend()
plt.show()