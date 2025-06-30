from decorators import input_error

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contacts(args, contacts):
    name, phone = args
    contacts[name] = phone
    return("Contact added")

@input_error
def show_phone(args, contacts):
    name = args[0]
    if name in contacts:
        return (contacts[name])
    else:
        return("There is no contuct with such name!")

@input_error
def change_contact(args, contacts):
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return("Contact was changed")
    else:
        return("There is no contuct with such name!")


@input_error
def all_contacts(contacts):
    for name, number in contacts.items():
        print(name, number)
  
def main():
    contacts = {}
    print("Welcome to assistant bot")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)
        
        if command in ["close" , "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contacts(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            all_contacts(contacts)
        else:
            print("Invalid command")
            
if __name__ == "__main__":
    main()
