import data
import diagram

my_data = data.create_data(1000)

print(my_data)

diagram.show_histogram(my_data)