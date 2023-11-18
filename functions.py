def get_todos(filepath='todos.txt'):
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_org, filepath='todos.txt'):
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_org)


if __name__ == "__main__":
    print("Hello")
    print(get_todos())