from anytree import Node, RenderTree

def Making_S_words(all_keys_and_values):
    list_with_current_words = []
    for i in all_keys_and_values:
        if i[0] == "S":
            list_with_current_words.append(i[1])
    Making_tree_with_S_roots(list_with_current_words)
    for i in range(len(list_with_current_words)):
        Making_of_other_words(all_keys_and_values, list_with_current_words[i])
    
def Making_tree_with_S_roots(list_with_current_words):
    main_node = Node("S")
    for i in range(len(list_with_current_words)):
        i = Node(str(list_with_current_words[i]), parent = main_node)
    #for pre, fill, node in RenderTree(main_node):
        #print("%s%s" % (pre, node.name))

def Making_of_other_words(all_keys_and_values, current_word):
    list_with_current_other_words = []
    for i in current_word:
        for j in all_keys_and_values:
            print(j)
            for k in j[0]:
                if k == i:
                    i = k
                    list_with_current_other_words.append(current_word)
                    #print(list_with_current_other_words)
    
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
        Make_start_word(our_rules, all_keys, new_tamplate, complete_start_word)
    else:
        Make_tree_of_good_words(our_rules, all_keys, new_tamplate, complete_start_word)

def Make_other_words(our_rules, all_keys, new_tamplate, complete_start_word):
    a = 0
    for i in new_tamplate:
        if i in all_keys:
            a += 1
    if a != 0:
        Make_start_word(our_rules, all_keys, new_tamplate, complete_start_word)

def Make_tree_of_good_words(our_rules, all_keys, new_tamplate, complete_start_word):
    main_node = Node(complete_start_word)
    Make_other_words(our_rules, all_keys, new_tamplate, complete_start_word)
    second_node = Node("test_node", parent = main_node)
    #for pre, fill, node in RenderTree(main_node):
        #print("%s%s" % (pre, node.name))
if __name__ == '__main__':   
    first_or_second, false_rule = False, False
    key_list, value_list, all_keys, key_value_list, all_keys_and_values = [], [], [], [], []
    our_rules = {}
    key, value = "", ""
    print("Дорогой пользователь, пожалуйста, задайте грамматику G...")
    count_of_neterminals = list(input("Для этого задайте нетерминалы грамматики(ОБЯЗАТЕЛЕН К ЗАДАНИЮ S!): "))
    for i in range(int(len(count_of_neterminals) / 2)):
        count_of_neterminals.remove(" ")
    count_of_terminals = list(input("Кроме этого, не забудьте задать терминалы грамматики: "))
    for i in range(int(len(count_of_terminals) / 2)):
        count_of_terminals.remove(" ")
    print("Исходя из введённых вами данных, вот список нетерминалов, которые могут быть использованны для задания правил:", end = " ")
    for i in range(len(count_of_neterminals)):
        print(count_of_neterminals[i], end = " ")
    print("\nТеперь можно задать правила грамматики(Чтобы прекратить введите пустую строку)\n")
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
            key_value_list.append(key)
            key_value_list.append(value)
        our_rules.update({key:value})
        first_or_second = False
        key_list, value_list = [], []
        key, value = "", ""
        rule = str(input("\nПожалуйста, следуйте примеру 'S --> Aa'.\n\n"))
        all_keys_and_values.append(key_value_list)
        key_value_list = []
    our_start_word = our_rules[str(all_keys[0])]
    complete_start_word = ""
    Making_S_words(all_keys_and_values)
    Make_start_word(our_rules, all_keys, our_start_word, complete_start_word)

#Make_tree_of_good_words(our_rules, all_keys, can_be_neterminals, our_chain)