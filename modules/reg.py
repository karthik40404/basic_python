def register(data):
    id = int(input("Enter your ID: "))
    name = input("Enter your Name: ")
    age = int(input("Enter your age: "))
    place = input("Enter your place: ")
    data.append({'id': id, 'name': name, 'age': age, 'place': place})
    print("Added")

    