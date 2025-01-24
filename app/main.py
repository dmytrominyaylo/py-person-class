class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    people_list = []
    for person_dict in people:
        person = Person(person_dict["name"], person_dict["age"])
        people_list.append(person)
    for person_dict in people:
        person = Person.people[person_dict["name"]]
        if "wife" in person_dict and person_dict["wife"]:
            partner = Person.people.get(person_dict["wife"])
            if partner:
                person.wife = partner
        if "husband" in person_dict and person_dict["husband"]:
            partner = Person.people.get(person_dict["husband"])
            if partner:
                person.husband = partner
    return people_list
