# # 1 Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# num = input('Введите вещественное число: ')
# num = float(num)
# num = abs(num)
# summ = sum(map(int, str(num).replace('.', '')))
# print('Сумма цифр числа равна =', summ)

# # 2 Дана последовательность чисел. Получить список уникальных элементов заданной последовательности.
# enum_number = list(map(int, input("Введите последовательность: ").split()))
# enum_unique = list(filter(lambda item: enum_number.count(item) == 1, enum_number))
# print(enum_number, '->', enum_unique)

# # 3 Напишите программу, удаляющую из текста все слова, содержащие "абв".
# text_my = 'Напишите программуабв, удаляющуюабв из текста все словаабв, содержащие "абв"'
# text_my = list(filter(lambda x: 'абв' not in x, text_my.split()))
# my = " ".join(text_my)
# print(text_my)
# print(my)

# # 4 Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.
# Text = True
# while Text:
#     try:
#         n = input('Введите число N: ')
#         n = float(n)
#         n = int(n)
#         Text = False
#     except ValueError:
#         print('Вводить надо число')
# lst = []
# lst = [round((1+1/i)**i) for i in range(1,n+1)]
# print(f'Полученная сумма последовательности {lst} =', sum(lst))

# # 5 Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# lst = [2, 3, 4, 5, 6]
# proizved_lst = []
# proizved_lst = [(lst[i]*lst[-1-i]) for i in range((len(lst)+1)//2)]
# print(proizved_lst)