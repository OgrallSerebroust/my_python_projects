first_or_second = False
key_list, value_list = [], []
our_rules = {}
key, value = "", ""
print("Дорогой пользователь, пожалуйста, задайте грамматику G...\n")
count_of_neterminals = list(input("Для этого задайте нетерминалы грамматики(ОБЯЗАТЕЛЕН К ЗАДАНИЮ S!): "))
for i in range(int(len(count_of_neterminals) / 2)):
    count_of_neterminals.remove(" ")
count_of_terminals = list(input("Кроме этого, не забудьте задать терминалы грамматики: "))
for i in range(int(len(count_of_terminals) / 2)):
    count_of_terminals.remove(" ")
print(count_of_neterminals, count_of_terminals)
print("Теперь можно задать правила грамматики(Чтобы прекратить введите пустую строку)\n")
rule = str(input("Пожалуйста, следуйте примеру 'S --> Aa'.\n"))
while rule != "":
    for i in rule:
        if i != " " and i != "-" and i != ">" and first_or_second == False:
            key_list.append(i)
        if i == ">":
            first_or_second = True
        if i != " " and i != "-" and i != ">" and first_or_second == True:
            value_list.append(i)
    print(key_list, value_list)
    for i in range(len(key_list)):
        key += key_list[i]
    for i in range(len(value_list)):
        value += value_list[i]
    print(key, value)
    our_rules.update({key:value})
    print(our_rules)
    first_or_second = False
    key_list, value_list = [], []
    key, value = "", ""
    rule = str(input("Пожалуйста, следуйте примеру 'S --> Aa'.\n"))