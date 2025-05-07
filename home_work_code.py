queries = [
    'смотреть сериалы онлайн',
    'новости спорта',
    'афиша кино',
    'курс доллара',
    'сериалы этим летом',
    'курс по питону',
    'сериалы про спорт',
]

# обозначаем 2 Int переменные для подсчета кол-ва строк с 2-мя и 3-мя словами
three_words_count = 0
two_words_count = 0

# пишем цикл, перебирающий строки, считающий кол-во слов, записывающий "+1" в переменные, в зависимости от кол-ва слов
for string in queries:
  #print(string.strip())
  i = string.strip().count(' ')
  #print(i)

  if i == 2:
    three_words_count += 1
  else:
    two_words_count += 1

#print(three_words_count)
#print(two_words_count)

print(f"Поисковых запросов, содержащих 2 слов(а): {two_words_count/(three_words_count + two_words_count):.2%}")
print(f"Поисковых запросов, содержащих 3 слов(а): {three_words_count/(three_words_count + two_words_count):.2%}")
