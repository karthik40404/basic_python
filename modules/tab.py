def table(data):
    if data:
        print("{:<10}{:<10}{:<10}{:<10}".format("ID", "Name", "Age", "Place"))
        print('_' * 40)
        for i in data:
            print("{:<10}{:<10}{:<10}{:<10}".format(i['id'], i['name'], i['age'], i['place']))
        print("")
    else:
        print("No records found")

