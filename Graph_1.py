import matplotlib.pyplot as plt

x = [2, 4, 6, 8, 10]
y = [1, 2, 3, 5, 6]

if len(x) != len(y):
    print("Number of values in x and y do not match")
else:
    plt.scatter(x, y)
    plt.plot(x, y)
    plt.grid()
    plt.xlabel("x-axis")
    plt.ylabel("y-axis")
    plt.title("Graph to Plot Points")
    plt.axvline(x=0, color="red")
    plt.axhline(y=0, color="red")
    plt.show()
