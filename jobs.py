wards = {
    "Cardiology":  ["Alice", "Bob", "Carol"],
    "Neurology":   ["Diana", "Eve"],
    "Orthopedics": ["Frank", "Grace", "Hank"],
    "Oncology":    ["Ivy", "Bob"]
}

staff={}

for dept, docs in wards.items():
    print(dept,docs)
    for doc in docs:
        if docs not in staff:
            staff[doc] = dept
        else:
            staff[doc].append(dept)
print(staff)