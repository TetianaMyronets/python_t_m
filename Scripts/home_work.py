# from multiprocessing.pool import worker
# from operator import index

# numbers = [-5, 3, -1, 7, -2, 10]
# for i in numbers:
#     if i >= 0:
#         print(i)
#
# numbers = [3, 10, 7, 8, 15, 22, 31]
# for i in numbers:
#     if i % 2 == 0:
#         print(i,'- парне число')
#     else:
#         print(i,'- непарне число')
#
# n = int(input("Введіть число від 0 до 250: "))
# m = n // 60
# f = n % 60
# print('Число', n,'- це', m, 'хвилин', f, 'секунд')
#
# text = ['Python is Awesome']
# vowel = ['a', 'e', 'i', 'o', 'u']
# x = 0
# for i in list(text[0]):
#    if i.lower() in vowel:
#        x = x + 1
# print(x)

# Home Work 2

# def is_palindrome(text):
#     reversed_text = text[::-1]
#     if text.lower() == reversed_text.lower():
#         return True
#     else:
#         return False
# print(is_palindrome(str(input("Enter text: "))))

# def repeat_text(text, times):
#     for i in range(times):
#         print(text)
#
# repeat_text("Hello!", 5)

# def repeat_text(text, times):
#     print(text * times)
#
# repeat_text("Hello! ", 5)

# def shorten_text(text, n):
#     if len(text) > n:
#         print(text[:n] + '...')
#     elif len(text) == n:
#         print(text)
#     else:
#         print("Enter other text")
#
# shorten_text("The table is broken", 20)

# def replace_word(text, old, new):
#     return text.replace(old, new)
#
# print(replace_word('I love JavaScript', 'JavaScript', 'Python'))

# def count_words(text):
#     return len(text.split())
#
# print(count_words("Welcome to the Rivne"))

# def swap_case(text):
#     new_text = ''
#     for i in text:
#         if i.isupper():
#             new_text = new_text + i.lower()
#         else:
#             new_text = new_text + i.upper()
#     return new_text
# print(swap_case("Welcome to the Rivne"))

# def swap_case(text):
#     new_text = text.swapcase()
#     return new_text
#
# print(swap_case("Welcome to the Rivne"))


# Home Work 3

# numbers = [5, -3, 12, 0, -8, 7, -1, 4]
# positive_numbers = []
# for i in numbers:
#     if i >= 0:
#         positive_numbers.append(i)
#
# print(positive_numbers)
# print(len(positive_numbers))


# entered_word = input("Enter the word: ")
# words = ['apple', 'banana', 'cherry', 'mango', 'kiwi']
# for i in words:
#     if entered_word == i:
#         print(words.index(i))
#         break
#     else:
#         continue
#         print("This word is not in the list.")

# entered_word = input("Enter the word: ")
# words = ['apple', 'banana', 'cherry', 'mango', 'kiwi']
# if entered_word in words:
#         print(words.index(entered_word))
# else:
#         print("This word is not in the list.")

# a = [1, 2, 3]
# b = [4, 5, 6]
# c = a + b
# d = []
# for i in c:
#     d.append(i * 2)
# print(d)

# phrases = ["  Hello ", "world ", " PYTHON ", " is ", " GREAT "]
# new_phrases = []
# for i in phrases:
#     new_phrases.append(i.strip().lower())
#
# print(new_phrases)

# students = [
#     ["Anna", 90],
#     ["Ben", 75],
#     ["Oleg", 88]
# ]
# max_value = 0
# max_name =''
# for i in students:
#     if i[1] > max_value:
#         max_name = i[0]
#         max_value = i[1]
# print(max_name)

# values = [3, 5, 3, 7, 9, 5, 3, 9, 10]
# unic_values = []
# for i in values:
#     if i not in unic_values:
#         unic_values.append(i)
#
# print(unic_values)

# Home Work 4

students = {
    "Anna": [90, 85, 78],
    "Ben": [76, 88, 90],
    "Oleg": [100, 90, 95]
}
student_max_avg_name = ''
student_max_avg_value = 0

for key in students.keys():
    sum = 0
    for i in students[key]:
        sum = sum + i
    avg = round((sum/len(students[key])), 1)
    print(key, avg)
    if avg > student_max_avg_value:
        student_max_avg_value = avg
        student_max_avg_name = key
print('Max avg student score: ', student_max_avg_name, student_max_avg_value)

students["Oleg"].append(85)
print("Updated Oleg's score: ", students["Oleg"])

