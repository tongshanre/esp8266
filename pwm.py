import json


json_str = json.dumps({'a':1})

print(json_str)

json_obj = json.loads(json_str)
print(json_obj['a'])