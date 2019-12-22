from anytree import Node

def Make_start_word(our_rules, all_keys, our_start_word, complete_start_word):
    a = 0
    new_tamplate = ""
    for i in our_start_word:
        if i in all_keys:
            i = our_rules[str(i)]
        new_tamplate += i
    complete_start_word = new_tamplate
    for i in new_tamplate:
        if i in all_keys:
            a += 1
    if a != 0:
        for i in new_tamplate:
            if i in all_keys:
                Make_start_word(our_rules, all_keys, new_tamplate, complete_start_word)
    else:
        Make_tree_of_good_words(complete_start_word)

def Make_tree_of_good_words(complete_start_word):
    print(complete_start_word)
   
can_be_neterminals, first_or_second, false_rule = False, False, False
key_list, value_list, all_keys = [], [], []
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
rule = str(input("Пожалуйста, следуйте примеру 'S --> Aa'.\n\n"))
while rule != "":
    for i in rule:
        if i != " " and i != "-" and i != ">" and first_or_second == False:
            if count_of_neterminals.count(i) == 1:
                false_rule = False
                key_list.append(i)
            elif count_of_neterminals.count(i) == 0:
                print("\nВы ввели правила, для необъявленного нетерминала грамматики!\n")
                false_rule = True
        if i == ">": 
            first_or_second = True
        if i != " " and i != "-" and i != ">" and first_or_second == True and false_rule == False:
            value_list.append(i)
        false_rule = False
    for i in range(len(key_list)):
        key += key_list[i]
    for i in range(len(value_list)):
        value += value_list[i]
    if key != '':
        all_keys.append(key)
    our_rules.update({key:value})
    first_or_second = False
    key_list, value_list = [], []
    key, value = "", ""
    rule = str(input("\nПожалуйста, следуйте примеру 'S --> Aa'.\n\n"))
our_start_word = our_rules[str(all_keys[0])]
complete_start_word = ""
print(all_keys)
Make_start_word(our_rules, all_keys, our_start_word, complete_start_word)

#Make_tree_of_good_words(our_rules, all_keys, can_be_neterminals, our_chain)