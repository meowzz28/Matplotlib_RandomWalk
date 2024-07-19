import matplotlib.pyplot as plt
plt.style.use('Solarize_Light2')
x = range(1,1001)
y = [i**2 for i in x]
fig, ax = plt.subplots()
ax.scatter(x, y, c=y, cmap=plt.cm.Blues, s=10)
ax.set_title("Square Numbers", fontsize = 24)
ax.set_xlabel("Value", fontsize = 14)
ax.set_ylabel("Square_value", fontsize = 14)
ax.tick_params(labelsize = 14)
ax.axis([0,1100,0,1_100_000])

plt.show()