import os

file_1 = "home.html"
file_2 = "catalog.html"
file_3 = "contacts.html"
file_4 = "category_1.html"

current_dir = os.path.dirname(os.path.abspath(__file__))
rel_file_path = os.path.join(current_dir, f"{file_1}")
Path_html = os.path.abspath(rel_file_path)

print(Path_html)