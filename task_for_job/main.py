from requests import get
from json import loads
from os import mkdir

if __name__ == '__main__':
    name_of_person = ""
    our_test_query = get("https://json.medrating.org/users", params={"id": "1"})
    one_test_person = loads(our_test_query.text)
    for _ in one_test_person:
        if _["name"]:
            name_of_person = _["name"]
    try:
        file_about_person = open("tasks/" + str(name_of_person) + ".txt", "w")
        file_about_person.write(name_of_person)
    except FileNotFoundError:
        mkdir("tasks")
        file_about_person = open("tasks/" + str(name_of_person) + ".txt", "w")
        file_about_person.write(name_of_person)
