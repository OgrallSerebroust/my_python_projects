from requests import get
from json import loads
from os import mkdir

if __name__ == '__main__':
    def make_file_about_person(name, email):
        file_about_person = open("tasks/" + str(name) + ".txt", "w")
        file_about_person.write(name + " <" + email + ">")

    def collecting_information_from_json(our_persons):
        for _ in our_persons:
            try:
                name_of_person = _["name"]
                email_of_person = _["email"]
                try:
                    make_file_about_person(name_of_person, email_of_person)
                except FileNotFoundError:
                    mkdir("tasks")
                    make_file_about_person(name_of_person, email_of_person)
            except KeyError:
                print("")

    our_query_for_all_information_from_json = get("https://json.medrating.org/users")
    our_persons_from_query = loads(our_query_for_all_information_from_json.text)
    collecting_information_from_json(our_persons_from_query)
