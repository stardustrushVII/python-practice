def create_box(message, c_char):
    width = len(message) + 4  # spacingx10
    print(c_char + '-' * (width - 2) + c_char)
    print(f"| {message} |")
    print(c_char + '-' * (width - 2) + c_char)

# get.inputs
corner1 = input("User 1, enter your name: ")
message1 = input("User 1, enter your message: ")

corner2 = input("User 2, enter your name: ")
message2 = input("User 2, enter your message: ")

# display message code
create_box(message1, corner1)
print()  # line break stuff
create_box(message2, corner2)
