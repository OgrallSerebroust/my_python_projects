from requests import get, exceptions
from json import loads
from os import mkdir, path, rename
from datetime import datetime
from shutil import rmtree

if __name__ == '__main__':
    def check_files_is_same(new_name, new_email, new_company, new_completed_tasks, new_not_completed_tasks):
        with open("tasks/" + str(new_name) + ".txt", "r", encoding="utf-8") as old_file:
            name_mail_and_time_line = old_file.readline()
            email_from_file = name_mail_and_time_line.split()[-3::1][0]
            name_from_file = str(name_mail_and_time_line.partition(email_from_file)[0][:-1])
            company_from_file = old_file.readline().rstrip('\n')
            old_file.readline()
            i = old_file.readline()
            completed_tasks_from_file, not_completed_tasks_from_file = [], []
            while i != '\n':
                i = old_file.readline()
                if i != '\n':
                    completed_tasks_from_file.append(i[:-1])
            j = old_file.readline()
            while j != '':
                j = old_file.readline()
                if j != '':
                    not_completed_tasks_from_file.append(j[:-1])
        temp_completed_tasks_from_file = sorted(completed_tasks_from_file)
        temp_new_completed_tasks = sorted(new_completed_tasks)
        temp_not_completed_tasks_from_file = sorted(not_completed_tasks_from_file)
        temp_new_not_completed_tasks = sorted(new_not_completed_tasks)
        email_from_file = email_from_file[1:-1]
        if new_name == name_from_file and new_email == email_from_file and new_company == company_from_file and temp_new_completed_tasks == temp_completed_tasks_from_file and temp_new_not_completed_tasks == temp_not_completed_tasks_from_file:
            return True
        else:
            return False

    def creating_process(name_for_creating, email_for_creating, time_for_creating, company_for_creating, completed_tasks_for_creating, not_completed_tasks_for_creating):
        with open("tasks/" + str(name_for_creating) + ".txt", "w", encoding="utf-8") as file_about_person:
            file_about_person.write(
                name_for_creating + " <" + email_for_creating + "> " + time_for_creating + "\n" + company_for_creating + "\n\n" + "Завершённые задачи:\n")
            for i in range(len(completed_tasks_for_creating)):
                file_about_person.write(completed_tasks_for_creating[i] + "\n")
            file_about_person.write("\nОставшиеся задачи:\n")
            for j in range(len(not_completed_tasks_for_creating)):
                file_about_person.write(not_completed_tasks_for_creating[j] + "\n")

    def file_creator_function(name_for_creating, email_for_creating, time_for_creating, company_for_creating, completed_tasks_for_creating, not_completed_tasks_for_creating):
        try:
            try:
                creating_process(name_for_creating, email_for_creating, time_for_creating, company_for_creating,
                                 completed_tasks_for_creating, not_completed_tasks_for_creating)
            except IOError:
                print(
                    "Обнаружена ошибка доступа к файлам!\nСкрипт удалит директорию!\nПожалуйста, перезапустите скрипт после устранения неполадок.\n")
                rmtree("tasks/", ignore_errors=True)
                creating_process(name_for_creating, email_for_creating, time_for_creating, company_for_creating,
                                 completed_tasks_for_creating, not_completed_tasks_for_creating)
                raise SystemExit()
        except FileNotFoundError:
            try:
                mkdir("tasks/")
            except IOError:
                print(
                    "Обнаружена ошибка доступа к файлам!\nСкрипт удалит директорию!\nПожалуйста, перезапустите скрипт после устранения неполадок.\n")
                rmtree("tasks/", ignore_errors=True)
                raise SystemExit()

    def make_file_about_person(name, email, time, company, completed_tasks, not_completed_tasks):
        if path.exists("tasks/" + str(name) + ".txt"):
            if not check_files_is_same(name, email, company, completed_tasks, not_completed_tasks):
                with open("tasks/" + str(name) + ".txt", "r", encoding="utf-8") as old_file:
                    name_mail_and_time_line = old_file.readline()
                    where_was_create_old_file = name_mail_and_time_line.split()[-2::]
                rename("tasks/" + str(name) + ".txt",
                       "tasks/" + str(name) + "_" + str(where_was_create_old_file[0].split(".")[2]) + "-" + str(
                           where_was_create_old_file[0].split(".")[1]) + "-" + str(
                           where_was_create_old_file[0].split(".")[0]) + "T" + str(
                           where_was_create_old_file[1].split(":")[0]) + "-" + str(
                           where_was_create_old_file[1].split(":")[1]) + ".txt")
                file_creator_function(name, email, time, company, completed_tasks, not_completed_tasks)
        else:
            file_creator_function(name, email, time, company, completed_tasks, not_completed_tasks)

    def collecting_information_from_todos_json(user_id):
        completed_tasks, not_completed_tasks = [], []
        our_query_for_tasks_information_from_json = get("https://json.medrating.org/todos",
                                                        params={"userId": str(user_id)})
        our_data_from_query = loads(our_query_for_tasks_information_from_json.text)
        for _ in our_data_from_query:
            if _["completed"]:
                if len(_["title"]) <= 50:
                    completed_tasks.append(_["title"])
                else:
                    completed_tasks.append(_["title"][:50] + "...")
            else:
                if len(_["title"]) <= 50:
                    not_completed_tasks.append(_["title"])
                else:
                    not_completed_tasks.append(_["title"][:50] + "...")
        return completed_tasks, not_completed_tasks

    def collecting_information_from_json(our_persons):
        global users_data_without_full_info_set
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
                except :
                    #
                    make_file_about_person(name_of_person, email_of_person, time_of_writing_info,
                                           company_were_user_works, completed_tasks_of_one_user,
                                           not_completed_tasks_of_one_user)
            except KeyError:
                users_data_without_full_info_set += 1

    try:
        our_query_for_all_information_from_json = get("https://json.medrating.org/users")
        our_persons_from_query = loads(our_query_for_all_information_from_json.text)
        users_data_without_full_info_set = 0
        collecting_information_from_json(our_persons_from_query)
        print("К сожалению не все данные были обработаны!\n" + str(
            users_data_without_full_info_set) + " пользователей имеют неполные данные!")
    except exceptions.ConnectionError:
        print("Возникла проблема с подключением к сети!\nПожалуйста попробуйте попытку позже...\n")
        raise SystemExit(1)
