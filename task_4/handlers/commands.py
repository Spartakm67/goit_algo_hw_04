def handle_hello(args, contacts):
    return "How can I help you?"


def validate_two_args(args, command_name: str):
    if len(args) != 2:
        return f"Please enter name and phone separated by a space"
    return None


def add_contact(args, contacts):
    error = validate_two_args(args, "add")
    if error:
        return error

    name, phone = args

    if name in contacts:
        return "This contact already exists."
    
    if phone in contacts.values():
        return "This phone number already exists."
    
    contacts[name] = phone
    return "Contact added."


def change_contact(args, contacts):
    error = validate_two_args(args, "change")
    if error:
        return error

    name, phone = args

    if name not in contacts:
        return "This contact does not exist."
    
    if phone in contacts.values() and contacts[name] != phone:
        return "This phone number already exists."

    contacts[name] = phone
    return "Contact updated."


def show_phone(args, contacts):
    if len(args) != 1:
        return "Please enter just name"

    name = args[0]

    if name not in contacts:
        return "This contact does not exist."

    return contacts[name]


def show_all(args, contacts):
    if not contacts:
        return "No contacts found."

    result = []

    for name, phone in contacts.items():
        result.append(f"{name}: {phone}")

    return "\n".join(result)


def delete_contact(args, contacts):
    if len(args) != 1:
        return "Please enter just name"

    name = args[0]

    if name not in contacts:
        return "This contact does not exist."

    del contacts[name] 
    return "Contact deleted."

COMMANDS = {
    "hello": handle_hello,
    "add": add_contact,
    "change": change_contact,
    "phone": show_phone,
    "all": show_all,
    "delete": delete_contact,
} 