print("Дорогой пользователь, пожалуйста, задайте грамматику G...\n")
count_of_neterminals = list(input("Для этого задайте нетерминалы грамматики(ОБЯЗАТЕЛЕН К ЗАДАНИЮ S!): "))
for i in range(int(len(count_of_neterminals) / 2)):
    count_of_neterminals.remove(" ")
count_of_terminals = list(input("Кроме этого, не забудьте задать терминалы грамматики: "))
for i in range(int(len(count_of_terminals) / 2)):
    count_of_terminals.remove(" ")
print(count_of_neterminals, count_of_terminals)
print("Теперь можно задать правила грамматики...\nПожалуйста, следуйте примеру 'S --> Aa'.")
