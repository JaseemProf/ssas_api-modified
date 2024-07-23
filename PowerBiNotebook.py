
import sys
import os
import requests

print (sys.argv[1])
print (sys.argv[2])


home_dir = os.path.expanduser('~')

# Construct the path to the Documents directory
folderpath = os.path.join(home_dir, 'Documents') + "\\Power Bi Connections"

if not os.path.exists(folderpath):
    # Create the folder if it doesn't exist
    os.makedirs(folderpath)
    print(f"Folder '{folderpath}' created.")
else:
    print(f"Folder '{folderpath}' already exists.")

filepath = folderpath +  '\\Power BI Desktop Localhost ' + sys.argv[1].strip('localhost:') + '.ipynb'


nb_template_url = 'https://raw.githubusercontent.com/JaseemProf/ssas_api-modified/main/new_notebook.json'
notebook_core = requests.get(nb_template_url).text.replace('<<PowerBIServer>>',sys.argv[1]).replace('<<PowerBIDatabase>>',sys.argv[2])

py_url = 'https://raw.githubusercontent.com/JaseemProf/ssas_api-modified/main/ssas_api.py'
py_file = requests.get(py_url)
api_file = open(folderpath + '\ssas_api.py', 'wb')
api_file.write(py_file.content)
api_file.close()

if os.path.exists(filepath):
    print(filepath + ' already exists. Not overwriting.')

try:
    if not os.path.exists(filepath):
        print('Creating ' + filepath)
        file = open(filepath,'w+')
        file.write(notebook_core)
        file.close()

    print('Opening Jupyter')

    os.system('"code "' + filepath + '""')

except Exception as e:
    print(e)
    print('Unable to create Jupyter notebook file')
