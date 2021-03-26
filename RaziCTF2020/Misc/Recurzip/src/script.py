import os
import io
import base64
from zipfile import ZipFile

def extract(path_to_zip_file, name):
    print("unzip -P " + str(base64.b64decode(name).decode()) + " " + path_to_zip_file);
    zf = ZipFile(path_to_zip_file + ".zip" , 'r')
    os.system('unzip -P ' + str(base64.b64decode(name).decode()) + " " + path_to_zip_file)
    for f in zf.namelist():
        dirname = os.path.splitext(f)[0]
        print(dirname)
        
    for i in zf.namelist():
        extract(dirname, dirname)

extract("eWh1dXF5YnZrYw==","eWh1dXF5YnZrYw==")