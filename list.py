def execute_command(input_commad, values, original_list):
    if input_commad == "insert":
        insert_to_list(original_list, values[0], values[1])
    elif input_commad == "print":
        print(original_list)
    elif input_commad == "remove":
        delete_from_list(original_list, values[0])
    elif input_commad == "append":
        append_to_list(original_list, values[0])
    elif input_commad == "sort":
        sort_list(original_list)
    elif input_commad == "pop":
        pop_list(original_list)
    elif input_commad == "reverse":
        reverse_list(original_list)
    else:
        print("Invalid command: %s" % input_commad)


def insert_to_list(original_list, position, value):
    """Insert a value to a specific position."""
    return original_list.insert(position, value)


def delete_from_list(original_list, value):
    """Delete the first occurrence of integer."""
    return original_list.remove(value)


def append_to_list(original_list, value):
    """Append to the end of the list"""
    return original_list.append(value)


def sort_list(original_list):
    """Sort the list."""
    return original_list.sort()


def pop_list(original_list):
    """Pop from the list."""
    return original_list.pop()


def reverse_list(original_list):
    """Reverse the list."""
    return original_list.reverse()


if __name__ == "__main__":
    N = int(input())
    my_list = []
    commands = []
    for _ in range(N):
        command_dict = {}
        command, *line = input().split()
        values = list(map(int, line))
        command_dict["command"] = command
        command_dict["values"] = values
        commands.append(command_dict)

    for command in commands:
        execute_command(command["command"], command["values"], my_list)
