
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name

        # example list of members
        self._members = [
            {
                "id": self._generateId(),
                "first_name": "Lara",
                "last_name": self.last_name,
                "age": 25,
                "lucky_numbers": [74, 12, 54]
            }, 
            {
                "id": self._generateId(),
                "first_name": "Juan",
                "last_name": self.last_name,
                "age": 34,
                "lucky_numbers": [101, 25, 47]
            }, 
            {
                "id": self._generateId(),
                "first_name": "Ron",
                "last_name": self.last_name,
                "age": 40,
                "lucky_numbers": [33, 3, 13]
            }
        ]

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        # fill this method and update the return
        aditional_info = {
            "id": member.get("id", self._generateId()),
            "last_name": self.last_name
        }
        member.update(aditional_info)
        self._members.append(member)
        return member
    

    def delete_member(self, id):
        # fill this method and update the return
        self._members = [member for member in self._members if member["id"] != id]
        return self._members

    def get_member(self, id):
        # fill this method and update the return
        member = None

        for x in self._members:
            if x["id"] == id:
                member = x

        return member

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
