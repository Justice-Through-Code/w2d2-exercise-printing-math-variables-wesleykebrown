
def convert_100_to_celsius():
    celsius_100 = ((100 - 32) * 5/9)
    print(celsius_100)
    print("float")
    # This is a float as there are decimal values calculated in the formula.

convert_100_to_celsius()

def convert_0_to_celsius():
    celsius_0 = ((0 - 32) * 5/9)
    print(celsius_0)

convert_0_to_celsius()

def convert_34_2_to_celsius():
    print((34.2 - 32) * 5/9)
    # Do this one all in one print statement without saving any variables
    
convert_34_2_to_celsius()


# Now, can you convert back?


def convert_5_to_fahrenheit():
    fahrenheit_5 = ((5 * 9/5) + 32)
    print(fahrenheit_5)

convert_5_to_fahrenheit()

def hotter_temp():
    #Converted 85.1 fahrenheit to celsius
    #celsius_85_1 = ((85.1 - 32) * 5/9)
    #Created list of temperatures
    #list_of_temperatures = [30.2, celsius_85_1]
    #Printed a statement showing the max temperature in the list
    #print(max(list_of_temperatures))
    #What is hotter, a temperature of 30.2 degrees celsius, or a temperature of 85.1 degrees fahrenheit?
    print("30.2 degrees celsius")

hotter_temp()
