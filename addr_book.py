from collections import UserDict
import re

class AddressBook(UserDict):

    def add_record(self, record):
        key = record.name.value
        value = record
        self.data[key] = value
        
    def get_record(self, name):
        return f"{self.data[name].phones}"
    
    
class Field:
    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, new_value):
        self._value = new_value

    def __repr__(self):
        return f"{self._value}"

class Name(Field):
    pass


class Phone(Field):
    def __init__(self, value):
        self.value = value

    @Field.value.setter
    def value(self, new_value):
        result = re.findall(r"^(?=\+\d{3}\(\d{2}\)\d{3}-\d{1,2}-\d{2,3}).{17}$", new_value)
        if not result:
            raise ValueError
        self._value = new_value
   

class Birthday(Field):
    pass


class Record:
    def __init__(self, name:Name, phone:Phone, birthday:Birthday = None):
        self.name = name
        self.phones = list()
        self.phones.append(phone)
        self.birthday = birthday
    
    def add_phone(self, new_phone):
        self.phones.append(new_phone)
    
    def edit_phone(self, old_phone, new_phone):
        for phone in self.phones:
            if phone.value == old_phone:
                phone.value = new_phone
                return True
        return False
    
    def del_phone(self, phone):
        for item in self.phones:
            if item.value == phone:
                self.phones.remove(item)
                return True
        return False
    
    def add_birthday(self, birthday):
        self.birthday = birthday

    # def days_to_birthday(self, birthday):

    
    def __repr__(self):
        return f"Name: {self.name.value}, Phones: {self.phones}, Birthday: {self.birthday}"