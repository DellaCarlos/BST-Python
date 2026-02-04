import matplotlib.pyplot as plt

def plot_tree(root):
    fig, ax = plt.subplots()
    ax.axis('off')

    def draw(node, x, y, dx):
        if node is None:
            return

        # desenha o nó
        ax.text(
            x, y, str(node.value),
            ha='center', va='center',
            bbox=dict(boxstyle="circle", fc="white", ec="black")
        )

        # left
        if node.left:
            ax.plot([x, x - dx], [y, y - 1], color="black")
            draw(node.left, x - dx, y - 1, dx / 2)

        # right
        if node.right:
            ax.plot([x, x + dx], [y, y - 1], color="black")
            draw(node.right, x + dx, y - 1, dx / 2)

    draw(root, 0, 0, 4)
    plt.show()