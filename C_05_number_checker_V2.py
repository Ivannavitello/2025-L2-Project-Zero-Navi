def int_check(question, low, high):
    """Checks users enter an integer between two values"""

    error = f"oops - please enter an integer between {low} and {high}."

    while True:
        response = input(question).lower()

        # check for the ext code
        if response == "xxx":
            return response

        try:
            # Change the response to an integer and check that it's more than zero
            response = int(response)

            if low <=response <= high:
                return response
            else:
                print(error)

        except ValueError:
            print(error)


# main routine ges here

# loop for testing purposes....
while True:

    print()
    my_num = int_check("Choose a number: ", 1 , 10)
    print(f"You chose {my_num}")

