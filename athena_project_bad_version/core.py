import subprocess

main_core = "D:/Python3_6_8/my_projects/Athena_project/Version_1.0_pre_alfa/core_blue.py"
url_temp = "D:/Python3_6_8/my_projects/Athena_project/Version_1.0_pre_alfa" \
                                             "/other_modules/core_of_internet_chat_working.py"
process_1 = subprocess.Popen(main_core, stdout=subprocess.PIPE, shell=True)
process_2 = subprocess.Popen(url_temp, stdout=subprocess.PIPE, shell=True)

text, _ = process_1.communicate()
text, _ = process_2.communicate()
while True:
    print("Hello")