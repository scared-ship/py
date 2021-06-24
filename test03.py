
# from test01 import get_formatted_name
def sss():
    print(1111)

# get_formatted_name('dqw','ffa')

def make_pizza(size, *toppings):

    print("\nMaking a " + str(size) +
"-inch pizza with the following toppings:")
    for topping in toppings:
       print("- " + topping + "\nMaking a ")

if __name__ == "__main__":
    print("执行前先print一下")


    make_pizza(16, 'pepperoni')
    make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

