categories = [
    {
        "name": "전자제품",
        "children": [
            {
                "name": "노트북",
                "children": [
                    {"name": "맥북"},
                    {"name": "윈도우"}
                ]
            }
        ]
    },
    {
        "name": "의류",
        "children": [
            {"name": "티셔츠"},
            {"name": "바지"}
        ]
    }
]

def flatten_categories(categories):
    result = []

    for category in categories:
        # 1️⃣ 현재 노드의 name 수집
        name = category.get("name")
        if name is not None:
            result.append(name)

        # 2️⃣ 자식이 있으면 재귀적으로 처리
        children = category.get("children")
        if isinstance(children, list):
            result.extend(flatten_categories(children))


    return result


# 실행
names = flatten_categories(categories)
print(names)

