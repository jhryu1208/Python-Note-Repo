"""
StringIO is for text. You use it when you have text in memory that you want to treat as coming from or going to a file.
BytesIO is for bytes. It's used in similar contexts as StringIO, except with bytes instead of text.
"""

from io import BytesIO, StringIO
import requests
import csv
import pandas as pd


request_url = requests.get("https://gist.githubusercontent.com/adamawolf/3048717/raw/a956ed1552091c32ce9f9f39e2210cc6359b9b26/Apple_mobile_device_types.txt")
contents = request_url.content

"""
방법1: encoding
"""
str_contents = str(contents, 'utf-8')
ls_contents = str_contents.split('\n')
x = [ ls_content.split(' : ') for ls_content in ls_contents if ls_content != '']
df = pd.DataFrame(x)
df.reset_index(inplace=True)
df.columns = ['id', 'device_id', 'device_name']
df.to_csv('./iphone1.csv', index=False)

"""
방법2 : StringIO
"""
str_contents = str(contents, 'utf-8')
stream_file = StringIO(str_contents)

with open('iphone2.csv', 'w', newline='\n') as f:
    writer = csv.writer(f, delimiter=',', quotechar='"')
    writer.writerow(['id', 'device_id', 'device_name'])
    id = 0
    for row in stream_file:
        if row != '\n':
            ls = row.replace('\n', '').split(' : ')
            ls.insert(0, id)
            id += 1
            writer.writerow(ls)
        else:
            continue

"""
방법3 : StringIO (2)
"""
str_contents = str(contents, 'utf-8')
print("Convert: ", type(contents), '=>', type(str_contents))
stream = StringIO(str_contents) # work with string data
print(type(stream))
df = pd.read_csv(stream, sep=' : ', engine='python', header=None)
df.reset_index(inplace=True)
df.columns = ['id', 'device_id', 'device_name']
df.to_csv('iphone3.csv', index=False)

"""
방법4 : StringIO (3) 
"""
str_contents = str(contents, 'utf-8')
body = StringIO(str_contents)
rows = [row.replace('\n', '').split(' : ') for row in body if row != '\n']
rows = [[id]+row for id, row in enumerate(rows)]

with open('iphone4.csv', 'w', newline='\n') as f:
    writer = csv.writer(f, delimiter=',', quotechar='"')
    writer.writerow(['id', 'device_id', 'device_name']) # header
    writer.writerows(rows)
    #result = target_body.getvalue()  S3에서 put_objects(temp파일 남기지 않고 추가하는 케이스) 이용시 유용


"""
방법5 : BytesIO (StringIO 방법도 포함임)
"""

bytes = BytesIO(contents) # work with byte data
df = pd.read_csv(bytes, sep=' : ', engine='python', header=None)
df.reset_index(inplace=True)
df.columns = ['id', 'device_id', 'device_name']
df.to_csv('iphone5.csv', index=False)


