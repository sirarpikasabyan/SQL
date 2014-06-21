import matplotlib.pyplot as plt


def main():
    x = range(6)
    y = [xi**2 for xi in x]
    plt.plot(x,y)
    plt.show()

if __name__ == '__main__':
    main()

