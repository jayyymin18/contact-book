import json

def main():
	with open("contacts.json") as f:
			contacts = json.load(f)
	while True:
		print("Enter 1 to add new contacts")
		print("Enter 2 to print existing contacts")
		print("Enter 3 to delete existing contacts")
		print("Enter 4 to find a contact")
		print("Enter 0 to exit")
		#Select what to do
		n = int(input("Choose from the above options	: "))
		print("")
		if n==1:
			add_contacts(contacts)
		elif n==2:
			print_contacts(contacts)
		elif n==3:
			delete_contacts(contacts)
		elif n==4:
			find_contacts(contacts)
		elif n==0:
			return
		else:
			print("Choose correct option")
		print("")

def add_contacts(contacts):
	while True:
		name = input("Enter name: ")
		if name=="":
			break
		if name not in contacts:
			number = input("Enter mobile number: ")
		else:
			print("Already in contacts. Want to update?")
			ans=input("Enter Y to continue or N to rewrite: ")
			if ans=='N':
				print("")
				add_contacts(contacts)
			else:
				number = input("Enter mobile number: ")
		if number=="":
			break
		contacts[name]=number
		with open("contacts.json", "w") as f:
			json.dump(contacts, f)
		print("")
	print("")

def print_contacts(contacts):
	for ele in contacts:
		print(str(ele),str("-->"),str(contacts[ele]))
	print("")

def delete_contacts(contacts):
	while True:
		name = input("Enter name of contact: ")
		if name=="":
			break
		if name not in contacts:
			print("Enter vaild name.")
			delete_contacts(contacts)
		else:
			del contacts[name]
			print(str(name)+str(" got deleted."))
		with open("contacts.json", "w") as f:
			json.dump(contacts, f)
		print("")

def find_contacts(contacts):
	while True:
		name = input("Enter name of contact: ")
		if name=="":
			break
		if name not in contacts:
			print("Name not present")
			delete_contacts(contacts)
		else:
			print(str(name),str("-->"),str(contacts[name]))
		print("")


if __name__ == '__main__':
	main()