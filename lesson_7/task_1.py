import os.path

project_path = 'my_project'
paths = ['settings', 'mainapp', 'adminapp', 'authapp']
for i in paths:
    os.makedirs(os.path.join(os.curdir,project_path,i), exist_ok=True)
