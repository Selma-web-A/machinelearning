import matplotlib.pyplot as plt

def show_histogram(data):
    plt.hist(data, bins=10)
    plt.xlabel("Number")
    plt.ylabel("Frequency")
    plt.title("Histogram")
    plt.show()