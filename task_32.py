import pickle

phone_book = [
              {"name": "Petr", "surname": "Petrov", "age": 50, "phone_number":"+380501234567"},
              {"name": "Ivan", "surname": "Ivanov", "age": 15, "phone_number":"+380507654321"},
              {"name": "Djon", "surname": "Rambo", "age": 42, "phone_number":"+380503453473"},
              {"name": "Jon", "surname": "McLein", "age": 35, "phone_number":"+380505551578"},
              {"name": "Petr", "surname": "Trov", "age": 23, "phone_number":"+380501202561"}
             ]

def print_entry(number, entry):
    print ("--[ %s ]--------------------------" % number)
    print ("| Surname: %20s |" % entry["surname"])
    print ("| Name:    %20s |" % entry["name"])
    print ("| Age:     %20s |" % entry["age"])
    print("| Number:  %20s |" % entry["phone_number"])
    print ()


def print_phonebook():
    print ()
    print ()
    print ("#########  Phone book  ##########")
    print ()

    number = 1
    for entry in phone_book:
        print_entry(number, entry)
        number += 1

def print_phonebook_by_age():
    phone_book_age = sorted(phone_book, key=lambda x: x["age"])
    print()
    print()
    print("#########  Phone book sorted by age ##########")
    print()

    number = 1
    for entry in phone_book_age:
        print_entry(number, entry)
        number += 1


def add_entry_phonebook(surname, name, age):
    entry = {}
    entry["surname"] = surname
    entry["name"] = name
    entry["age"] = age
    phone_book.append(entry)



def printError(message):
    print ("ERROR: %s" % message)

def printInfo(message):
    print ("INFO: %s" % message)

def find_entry_name_phonebook(name):
    idx = 1
    found = False
    for entry in phone_book:
        if entry["name"] == name:
            print_entry(idx, entry)
            idx += 1
            found = True
    if not found:
        printError("Not found!!")


def find_entry_age_phonebook(age):
    idx = 1
    found = False
    for entry in phone_book:
        if entry["age"] == age:
            print_entry(idx, entry)
            idx += 1
            found = True
    if not found:
        printError("Not found!!")

def delete_entry_name_phonebook(name):
    found = False
    idx_name = []
    for i in range(len(phone_book) - 1, -1, -1):
        if name == phone_book[i]["name"]:
            idx_name.append(i)
            found = True
    if not found:
        printError("Abonent not found!!!")
    for i in idx_name:
        phone_book.pop(i)
    #print(phone_book)


def count_all_entries_in_phonebook():
    print ("Total number of entries: ", len(phone_book))

def print_avr_age():
    avr_age = sum([x["age"]  for x in phone_book ]) / (len(phone_book))
    print(" Averange age of all abonent is %.2f " % avr_age)

def increase_age(number_of_years):
    for x in phone_book :
        x["age"] += number_of_years
        print(" Age all abonent increast on %d years" % number_of_years)
    pass

def save_to_file():
    pickle.dump(phone_book, open("phone_book.save", "wb"))
    printInfo("Phonebook is saved into 'phone_book.save'")


def load_from_file():
    global phone_book
    phone_book = pickle.load(open("phone_book.save", "rb"))
    printInfo("Phonebook is loaded from 'phone_book.save'")


def edit_phonebook(number):

    if 0 <= number <= len(phone_book):
        print("Select one of actions below for edit entry # %d :" , number)
        print("     1 - Edit surname ")
        print("     2 - Edit name ")
        print("     3 - Edit age ")
        print("     4 - Edit phone nuber")
        print("     5 - Edit all data entry # %d" , number)
        print("     6 - Delete entry # %d", number)
        print("-----------------------------")
        print("     0 - Exit")

        user_input = input("Enter you choice: ")
        if user_input is int:
            choice_2 = int(user_input)

            if choice_2 == 1:
                phone_book[number - 1]["surname"] = input(" - new surname  ")
            elif choice_2 == 2:
                phone_book[number - 1]["name"] = input(" - new name  ")
            elif choice_2 == 3:
                phone_book[number - 1]["age"] = int(input(" - new age  "))
            elif choice_2 == 4:
                phone_book[number - 1]["phone_number"] = input(" - new phone_number  ")
            elif choice_2 == 5:
                phone_book[number - 1]["surname"] = input(" - new surname  ")
                phone_book[number - 1]["name"] = input(" - new name  ")
                phone_book[number - 1]["age"] = int(input(" - new age  "))
                phone_book[number - 1]["phone_number"] = input(" - new phone_number  ")
            elif choice_2 == 6:
                phone_book.pop(number)
            elif choice == 0:
                print("Bye!")
            else:
                printInfo("Wrong choice...")
        else:
            printInfo("Something went wrong. Try again...")

    else :
        printInfo("Something went wrong. Try again...")

def main():
    while True:
        user_input = ""
        try:
            print ()
            print ()
            print ()
            print ("~ Welcome to phonebook ~")
            print ("Select one of actions below:")
            print ("     1 - Print phonebook entries")
            print ("     2 - Print phonebook entries (by age)")
            print ("     3 - Add new entry")
            print ("     4 - Find entry by name")
            print ("     5 - Find entry by age")
            print ("     6 - Delete entry by name")
            print ("     7 - The number of entries in the phonebook")
            print ("     8 - Avr. age of all persons")
            print ("     9 - Increase age by num. of years")
            print ("-----------------------------")
            print("     e - Edit entry by number")
            print("     s - Save to file")
            print ("     l - Load from file")
            print ("     0 - Exit")

            user_input = input("Enter you choice: ")
            choice = int(user_input)

            if choice == 1:
                print_phonebook()
            elif choice == 2:
                print_phonebook_by_age()
            elif choice == 3:
                surname = str(input("    Enter surname: "))
                name = str(input("    Enter name: "))
                age = int(input("    Enter age: "))
                add_entry_phonebook(surname, name, age)
            elif choice == 4:
                name = str(input("    Enter name: "))
                find_entry_name_phonebook(name)
            elif choice == 5:
                age = int(input("    Enter age: "))
                find_entry_age_phonebook(age)
            elif choice == 6:
                name = str(input("    Enter name: "))
                delete_entry_name_phonebook(name)
            elif choice == 7:
                count_all_entries_in_phonebook()
            elif choice == 8:
                print_avr_age()
            elif choice == 9:
                nmbrs_of_years = int(input("    Enter number of years to add to current ages: "))
                increase_age(nmbrs_of_years)
            elif choice == 0:
                print ("Bye!")
                break
            else:
                print ("Enter action within range [0..9]")

        except ValueError:
            if str(user_input) == 's':
                save_to_file()
            elif str(user_input) == 'l':
                load_from_file()
            elif str(user_input) == 'e':
                nmbrs_of_edit = int(input("    Enter number of edit: "))
                edit_phonebook(nmbrs_of_edit)
            else:
                printError("Something went wrong. Try again...")


if __name__ == '__main__':
    main()