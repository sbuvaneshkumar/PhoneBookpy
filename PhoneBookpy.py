book = {"Murugan":"1234567890", "Ramesh":"9873453467", "John":"9745086340", "Buvanesh":"8015967418", "Senthil":"86083408732", "Janani":"9548656655", "Surya":"9876565657"}
name = input("Enter person name:")
if name == "Murugan":
        print("Murugan number is:" +  book["Murugan"])
elif name == "Ramesh":
    print("Ramesh number is:" +  book["Ramesh"])
elif name == "John":
    print("John number is:" +   book["John"])
elif name == "Buvanesh":
    print("Buvanesh number is:" +  book["Buanesh"])
elif name == "Senthil":
    print("Senthil number is:" +  book["Senthil"])
elif name == "Janani":
    print("Janani number is:" +  book["Janani"])
elif name == "Surya":
    print("Surya number is:" + book["Surya"])
else:
    print("Name is not found in your Phone Book")

