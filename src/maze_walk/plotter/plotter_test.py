import matplotlib.pyplot as plt

WIDTH = 5

fig, ax = plt.subplots(figsize=(5, 4))


ax.set_aspect("equal")
ax.axis("on")
ax.set_xticks([])
ax.imshow([[0, 0, 0],
           [0, 1, 0],
           [1, 1, 1]])

plt.show()
