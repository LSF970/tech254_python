# Build a cli contact book that will allow users to add and delete and delete contacts. 
# Use Lists or Dictionaries.

# E.G

book = []

contact = input("Please enter a name for the contact book ")

book.append(contact)

remove_contact = input("Please enter a name of a user you would like to remove from the contact book")

book.remove(remove_contact)
print(book)