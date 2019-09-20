class Contact:
    counter = 1
    def __init__(self, name, lastname, phone, email, address):
        self._id = Contact.counter # TODO auto increment
        Contact.counter += 1
        self.name = name
        self.lastname = lastname
        self.phone = phone
        self.email = email
        self.address = address

    def __str__(self):
        return "name: {}\nlastname: {}\nphone: {}\nemail: {}\naddress: {}"\
            .format(self.name, self.lastname, self.phone, self.email, self.address)

c = Contact("A", "B", 132, "email", "address")
print(c)