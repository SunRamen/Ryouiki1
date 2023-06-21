import zipfile

sum = 0

with zipfile.ZipFile('sample.zip','r') as zip_data:
    for name in zip_data.namelist():
        if "kitamura" in name:
            if int(name.split('_')[1]) % 2 != 0:
                with zip_data.open(name, 'r') as file:
                    txt = file.read()
                    num = int(txt.strip())
                    sum += num

print("奇数ファイルの合計",sum)
