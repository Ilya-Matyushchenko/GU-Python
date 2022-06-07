import os
import shutil

folder = 'my_project'

for root, dirs, files in os.walk('my_project'):
    for i in dirs:
        if i == "templates":
            shutil.copytree(os.path.join(root, i),
                            os.path.join(folder, 'templates'),
                            dirs_exist_ok=True)
