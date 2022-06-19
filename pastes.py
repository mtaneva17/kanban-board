# Отидете в WAP.py!!!!



# from enum import unique
# import string

# import random

# FILE_EXT = ".pbn"


# def create(request):
#     text = POST['content']

#     S = 10

#     unique_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k = S))  

#     file_name = unique_name + FILE_EXT

#     with open(file_name, "w") as f:
#         f.write(text)

#     return ("/view/" + unique_name)

# def view(request, id):
#     file_name = id + FILE_EXT

#     with open(file_name, "r") as f:
#         text = f.read()

#     return (request, 'view.html', {'text': text})