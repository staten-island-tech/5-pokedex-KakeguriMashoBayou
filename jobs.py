wards = {
    "Cardiology":  ["Alice", "Bob", "Carol"],
    "Neurology":   ["Diana", "Eve"],
    "Orthopedics": ["Frank", "Grace", "Hank"],
    "Oncology":    ["Ivy", "Bob"]
}

staff={}
for dept, docs in wards.items():
    for doc in docs:
        if docs not in staff:
            staff[doc] = dept
print(staff)