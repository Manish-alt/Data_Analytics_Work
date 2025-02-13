import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [10,20,30,40,50]

# plt.bar(x, y) # for bar graph
# plt.plot(x,y, marker='o') # for line plot
# plt.scatter(x,y)   #for scatter plot
# plt.hist(y, bins=5) # for histogram
# plt.pie(y, labels=x) #for pie chart
plt.boxplot(y)  #for box plot
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Basic Bar Plot')
plt.show()