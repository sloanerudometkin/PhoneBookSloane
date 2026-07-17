from typing import Dict, List, Optional


class PhoneBook:
    """
    Created by leon on 1/23/18.
    Made WAY better by kristofer 6/16/20
    Python version for beginner coders
    """

    def __init__(self, phonebook_dict: Optional[Dict[str, List[str]]] = None):
        if phonebook_dict is None:
            self.phonebook = {} #create brand new dictionary if none
        else:
            self.phonebook = phonebook_dict #if passing in existing list, pass it to the phonebook_dict field
        """
        Constructor for PhoneBook
        :param phonebook_dict: Optional dictionary to initialize the phonebook with
        """

    def add(self, name: str, phone_number: str) -> None:
        if name in self.phonebook: #is name already in the dictionary?
            self.phonebook[name].append(phone_number) #if it does we need to add the new phone number
        else: #if it doesnt we have to create a new list
            self.phonebook[name] = [phone_number]
        """
        Add a phone number for a contact
        :param name: Contact name
        :param phone_number: Phone number to add
        """

    def add_all(self, name: str, *phone_numbers: str) -> None: #looked up arbitrary argument unpacking: bundle into a tuple
        """
        Add multiple phone numbers for a contact
        :param name: Contact name
        :param phone_numbers: Variable number of phone numbers to add
        """
        if name not in self.phonebook:
            self.phonebook[name] = []
        
        for phone_number in phone_numbers:
            self.phonebook[name].append(phone_number) #phone numbers comes in as a tuple but we need to change it to a list to match our formatting for the phonebook

    def remove(self, name: str) -> None: #first have to see if the name is in the dictionary so we can remove it
        """
        Remove a contact from the phonebook
        :param name: Contact name to remove
        """
        if name in self.phonebook:
            del self.phonebook[name]

    def has_entry(self, name: str, phone_number: str = None) -> bool:
        """
        Check if a contact exists, optionally with a specific phone number
        :param name: Contact name to check
        :param phone_number: Optional phone number to check
        :return: True if contact exists (with phone number if specified), False otherwise
        """
        if name not in self.phonebook: #has to return true or false for the test_remove. 
            return False
        if phone_number is None: #then just check for the name key in the dictionary and see if it is associated with the phone number
            return True
        for number in self.phonebook[name]:
            if number == phone_number:
                return True
            return False
        
    def lookup(self, name: str) -> List[str]:
        """
        Look up all phone numbers for a contact
        :param name: Contact name to look up
        :return: List of phone numbers for the contact
        """
        if name in self.phonebook:
            return self.phonebook[name]
        return [] #called in the add all test to see the numbers linked to that name. [name] to access the dictionary or return empty list

    def reverse_lookup(self, phone_number: str) -> str:
        """
        Find the contact name for a given phone number
        :param phone_number: Phone number to look up
        :return: Contact name associated with the phone number
        """
        for name in self.phonebook:
            numbers = self.phonebook[name]
            for number in numbers:
                if number == phone_number:
                    return name
        return None

    def get_all_contact_names(self) -> List[str]:
        """
        Get all contact names in the phonebook
        :return: List of all contact names
        """
        names: List[str] = []
        for name in self.phonebook:
            names.append(name)
        return names

    def get_map(self) -> Dict[str, List[str]]: #return self phonebook to the test: it expects a dictionary
        """
        Get the underlying dictionary representation of the phonebook
        :return: Dictionary mapping names to lists of phone numbers
        """
        return self.phonebook