import json
person={
    "name":"何秋灿",
    "age":22,
    "hobbies":["跳舞","健身","唱歌"]
}
with open('../data/data.json', 'w', encoding='utf-8') as f:
    json.dump(person,f,ensure_ascii=False,indent=4)
with open('../data/data.json', 'r', encoding='utf-8') as f:
    loaded_person=json.load(f)
    print(loaded_person)
