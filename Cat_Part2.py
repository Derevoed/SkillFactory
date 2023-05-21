from Cat_Part1 import Cat

cats = [
    {
        "animal": "кошка",
        "name": "Барон",
        "gender": "мальчик",
        "age": 2,
    },
    {
        "animal": "кошка",
        "name": "Сэм",
        "gender": "мальчик",
        "age": 2,
    }
]

for i in cats:
    cat_obj = Cat()
    cat_obj.init_from_dict(i)
    print(f'\nИмя: {cat_obj.name} \nПол: {cat_obj.gender} \nВозраст: {cat_obj.age}')
