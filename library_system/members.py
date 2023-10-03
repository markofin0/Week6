library_members = []


def register_member(name):
    if find_member(name) is True:
        print(f'{name} is already a member!')
    else:
        library_members.append(name)
        print(f'{name} is now a member!')


def find_member(name):
    if name in library_members:
        return True
    else:
        return False
