def days_to_units(num_of_days,conversion_unit):
    if conversion_unit == "hours":
        return f"{num_of_days} days are {num_of_days * 24} {conversion_unit}"
    elif conversion_unit == "minutes":
        return f"{num_of_days} days are {num_of_days * 24 * 60} {conversion_unit}"
    else:
        return "unsupported unit"


def validate_and_execute(days_and_unit_dictionary):
    try:
        user_input_number = int(days_and_unit_dictionary["days"])
        if user_input_number > 0:

            calculated_value = days_to_units(user_input_number,days_and_unit_dictionary["unit"])
            print(calculated_value)
        elif user_input_number == 0:
            print("You entered 0 , please enter a valid number")
        else:
            print("you entered  a negative number, no conversion for you!")
    except ValueError:
        print("Your input is not a valid number,Don't ruin my program")


user_input_message = "Hey user, enter number of days and coversion units\n"