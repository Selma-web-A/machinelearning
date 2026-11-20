import matplotlib.pyplot as plt

def show_histogram(data):
    plt.hist(data, bins=50)
    plt.xlabel("frukt")
    plt.ylabel("Frequency")
    plt.title("Histogram")
    plt.show()