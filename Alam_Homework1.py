# Aysha Alam
# CIS 3368 - Otto
# Homework 1

# Implement a menu of options for a user to modify the contact details
# Each option is represented by a single character
# The program initially outputs the menu, and outputs the menu after a user chooses an option

def menu_output():
    print("MENU")

    print("a - Add contact")
    print("d - Delete contact")
    print("u - Update contact details")
    print("b - Output all contacts in alphabetical order")
    print("c - Output all contacts by creatation date")
    print("o - Output all contacts")
    print("q - Quit\n")

    print("Choose an option: ")

menu_output()

def user_choice():
    user_choice = input()

    if user_choice == "a":
        print("Add contact")
    elif user_choice == "d":
        print("delete contact")
    elif user_choice == "u":
        print("update contact")
    elif user_choice == "b":
        print("output all contacts in ALPHA")
    elif user_choice == "c":
        print("Output all contacts by creatation date")
    elif user_choice == "o":
        print("Output all contacts")

user_choice()

