import json

with open("source.json", encoding='utf8') as f:
    data = json.load(f)
f.close()

depts = {}

for pers in data:
    dept = pers['dept']
    if pers['dept'] not in depts:
        depts.update({dept:{'count': 0,'avg_hours': [], 'people': []}})
    depts[dept]['count'] += 1
    if pers.get('hours') is not None:
        depts[dept]['avg_hours'] += [pers.get('hours')]
        depts[dept]['people'] += [{'name': pers['name'], 'hours': pers['hours'], 'phone': pers['phone']}]
    else:
        depts[dept]['people'] += [{'name': pers['name'], 'phone': pers['phone']}]

for i in depts.values():
    i['avg_hours'] = round(sum(i['avg_hours']) / len(i['avg_hours']))

with open('outfile.json','w', encoding='utf8') as outfile:
    json.dump(depts,outfile,ensure_ascii=False, sort_keys=True, indent=4)
outfile.close()