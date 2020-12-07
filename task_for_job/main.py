from requests import get
from json import loads
from os import mkdir
from datetime import datetime

if __name__ == '__main__':
    def make_file_about_person(name, email, time, company, completed_tasks, not_completed_tasks):
        file_about_person = open("tasks/" + str(name) + ".txt", "w", encoding="utf-8")
        file_about_person.write(name + " <" + email + "> " + time + "\n" + company + "\n\n" + "Завершённые задачи:\n")
        for i in range(len(completed_tasks)):
            file_about_person.write(completed_tasks[i] + "\n")
        file_about_person.write("\nОставшиеся задачи:\n")
        for j in range(len(not_completed_tasks)):
            file_about_person.write(not_completed_tasks[j] + "\n")
        file_about_person.close()

    def collecting_information_from_todos_json(user_id):
        completed_tasks, not_completed_tasks = [], []
        our_query_for_tasks_information_from_json = get("https://json.medrating.org/todos",
                                                        params={"userId": str(user_id)})
        our_data_from_query = loads(our_query_for_tasks_information_from_json.text)
        for _ in our_data_from_query:
            if _["completed"]:
                completed_tasks.append(_["title"])
            else:
                not_completed_tasks.append(_["title"])
        return completed_tasks, not_completed_tasks

    def collecting_information_from_json(our_persons):
        for _ in our_persons:
            try:
                user_id = _["id"]
                name_of_person = _["name"]
                email_of_person = _["email"]
                now = datetime.now()
                time_of_writing_info = now.strftime("%d.%m.%Y %H:%M")
                company_were_user_works = _["company"]["name"]
                completed_tasks_of_one_user, not_completed_tasks_of_one_user = collecting_information_from_todos_json(
                    user_id)
                try:
                    make_file_about_person(name_of_person, email_of_person, time_of_writing_info,
                                           company_were_user_works, completed_tasks_of_one_user,
                                           not_completed_tasks_of_one_user)
                except FileNotFoundError:
                    mkdir("tasks")
                    make_file_about_person(name_of_person, email_of_person, time_of_writing_info,
                                           company_were_user_works, completed_tasks_of_one_user,
                                           not_completed_tasks_of_one_user)
            except KeyError:
                print("")

    our_query_for_all_information_from_json = get("https://json.medrating.org/users")
    our_persons_from_query = loads(our_query_for_all_information_from_json.text)
    collecting_information_from_json(our_persons_from_query)
