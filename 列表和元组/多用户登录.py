map = {"aaa":"123456","bbb":"888888","ccc":"333333"}
username = input()
password = input()

def login(username, password):
    if map.get(username) == None:
        print("Wrong User")
        return

    if map.get(username) != password:
        print("Fail")
    else:
        print("Success")
    return

login(username, password)
    