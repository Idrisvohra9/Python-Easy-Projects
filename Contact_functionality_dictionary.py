contacts={
    "Ambulance" : 108,
    "Police station" : 100,
    "Fire station" : 101
}
contacts=sorted(contacts.items()) #Sorting the keys(Contact names) by alphabetical order. This will convert it to a list.
contacts=dict(contacts) # Converting it back to dictionary.
s=0
contacts.update(contacts.items())
c=list(contacts.keys()) 
while (True):
    print("Contacts:\n")
    for name,num in contacts.items():
        gets=c[s][0]
        print(gets, name,"   ",num,"|")
        s+=1
    print("*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*\n")
    n=int(input("What do you like to do?\n 1. Add a contact\n 2. Delete a contact\n 3. Search for a contact\n 0. Exit\n"))
    if n==0:
        print("You exited.")
        exit()
    if n==1:
        key = input("Enter the name of the contact: ")
        number=int(input("Enter the number: "))
        contacts.update({key:number})
    if n==2:
        profile= input("Which contact: ")
        contacts.pop(profile)
    if n==3:
        profile= input("Search by name: ")
        contacts.get(profile)
        print(" Name:",profile,"\n Number: ",contacts[profile])
        print("More options: ")
        mo=(input(" 'c'- Call\n 'e'- Edit contact\n 'd'- Delete\n"))
        mo.lower()
        if mo=='c':
            print("Calling..")
            call=int(input("0 to end call "))
            if call==0:
                exit()
        if mo=='e':
            contacts.pop(profile)
            name = input("Edit name: ")
            number=int(input("Edit number: "))
            contacts.update({name : number})
            print("\nContact information saved.")
        if mo=='d':
            contacts.pop(profile)
            print("\nContact Deleted.")