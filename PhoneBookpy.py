book = {"Murugan":"1234567890", "Ramesh":"9873453467", "John":"9745086340", "Buvanesh":"8015967418", "Senthil":"86083408732", "Janani":"9548656655", "Surya":"9876565657"}
name = input("Enter person name:")
if name in book:
	print ("Phone number is " + str(book[name]))
else :
	print ("Doesn't exist")
