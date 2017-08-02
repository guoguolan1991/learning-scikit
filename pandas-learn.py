import json
import pandas as pd


def read_line(path):
    file_object = open(path)
    for line in file_object:
        try:
            r = json.loads(line)
            yield r
        except:
            file_object.close()


a = list(read_line('comments.txt'))
df = pd.DataFrame(a)
color = df[u'productColor'].value_counts()
print color