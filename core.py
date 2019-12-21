from anytree import Node

def Make_tree_of_good_words(our_rules, all_keys, can_be_neterminals , our_chain):
    new_our_chain = ""
    can_be_neterminals = True
    for i in our_chain: 
        if i in all_keys:
            i = our_rules[str(i)]
            can_be_neterminals = False
            print(i)
        new_our_chain += i
    print(new_our_chain)
    if can_be_neterminals == False:
        Make_tree_of_good_words(our_rules, all_keys, can_be_neterminals, new_our_chain)
first_or_second, can_be_neterminals = False, False
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
            key_list.append(i)
        if i == ">":
            first_or_second = True
        if i != " " and i != "-" and i != ">" and first_or_second == True:
            value_list.append(i)
    for i in range(len(key_list)):
        key += key_list[i]
    for i in range(len(value_list)):
        value += value_list[i]
    all_keys.append(key)
    our_rules.update({key:value})
    first_or_second = False
    key_list, value_list = [], []
    key, value = "", ""
    rule = str(input("\nПожалуйста, следуйте примеру 'S --> Aa'.\n\n"))
our_chain = our_rules[str(all_keys[0])]
Make_tree_of_good_words(our_rules, all_keys, can_be_neterminals, our_chain)