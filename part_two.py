
#Define a main function and introduce the user to the contact book
#The function is executed as a statement. 

def main():
    print("Greetings! \nPlease make use of my contact book by completing the following steps: \na) Add three new contacts using the following format: Name : Number \nb) Make sure your contacts have been arranged in alphebetical order.\nc) Delete a contact.\nd) Search for an existing contact.")

    #Create two variables made up of an array of strings.
    #The first variable represents the name of an indiviudal and the second is their contact number. 
    
    Name = ['Victoria', 'Andrew']
    print(Name)
    Number = ['0849993016', '0849879074']
    print(Number)

    #Create a third variable, which is made of an empty array. 

    contacts = []
    print(contacts)
    
    #Create a loop which will continue to run until it reaches the length of array. 
    #Make use of the append method to add a new contact to the end of the list.

    for i in range(len(Name)):
      contacts.append(Name[i] + ' : ' + Number[i])
      #concatenation of the two different arrays. 

    #Introduce a while loop to run until the statement is false, where the number of contacts has reached maximum number of 5.
    
    while len(contacts) < 5:
      details = input('Please enter a name and number of an individual to create a new contact.\n')
       # name : number
      contacts.append(details)
      print(contacts)
      
    #The sort method is used to arrange all your exisitng contacts into alphabetical order.
      
    contacts.sort()
    print(contacts)
    
    #A input is used to inform the user that they can delete a contact by inputting their name. 
    
    name_to_delete = input('Which contact do you want to delete? ')
    
    #Delete a contact based on what it starts with.
    
    index_to_delete = 0
    for c in range(len(contacts)):
      contact_name = contacts[c]
      if contact_name.startswith(name_to_delete):
        index_to_delete = c
    
    #The pop method is used to delete a contact in a specific index position.
    print('Index to delete: ' + str(index_to_delete))
    contacts.pop(index_to_delete)
    print(contacts)
    
    #Search for a contact based on what their name starts with.
    
    name_search = input('Search contact: ')
    for search in range(len(contacts)):
      contact_name = contacts[search]
      if contact_name.startswith(name_search):
        print(contact_name)
         

if __name__ == "__main__":
    main()
    
#Close main function.
    

  
  
  
  
  

  

  











