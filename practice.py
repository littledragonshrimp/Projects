import json

food = {
    "meat": [
        {"beef": [
            {"data": "09.24.22"},
            {"quantity": "5"}
        ]},
        {"chicken": [
            {"data": "09.23.22"},
            {"quantity": "10"}
        ]}
    ]
}

print(json.dumps(food))
