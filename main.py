import data
import diagram

buu = 50

my_data = data.create_data(buu)

print(my_data)


my_datalista = data.datalista ()
print(my_datalista)

number = (1, 10)
my_fruktlista = data.fruktlista (number)
print(my_fruktlista)
diagram.show_histogram(my_fruktlista)