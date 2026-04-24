def handle_hello(args, contacts):
    return "How can I help you?"


def add_contact(args, contacts):
    if len(args) != 2:
        return "Usage: add <name> <phone>"

    name, phone = args
    contacts[name] = phone
    return "Contact added."


COMMANDS = {
    "hello": handle_hello,
    "add": add_contact,
} 