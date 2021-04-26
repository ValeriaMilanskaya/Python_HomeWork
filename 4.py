rus_dict = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
with open('4new.txt', 'w', encoding='utf-8') as new_f:
    with open('4my.txt', 'r', encoding='utf-8') as my_f:
        new_f.write(str([line.replace(line.split()[0], rus_dict.get(line.split()[0])) for line in my_f]))



# from googletrans import Translator
# with open('4new.txt', 'w', encoding='utf-8') as new_f:
#     with open('4my.txt', 'r', encoding='utf-8') as my_f:
#         text = my_f.read()
#     t = Translator()
#     a = t.translate(text)
#     print(a)