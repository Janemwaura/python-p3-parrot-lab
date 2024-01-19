def parrot(message="Squawk!"):
    print(message)
    return message


custom_message = "Parrot says:"
result = parrot(custom_message)
print("Returned message:", result)


default_result = parrot()
print("Returned default message:", default_result)

parrot()
