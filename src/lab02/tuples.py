def format_record(rec):
    if not isinstance(rec, tuple):
        return ("TypeError")
    if len(rec) != 3:
        return ("ValueError")
    
    fio, group, gpa = rec
    
    if not isinstance(fio, str):
        return ("TypeError")
    if not isinstance(group, str):
        return ("TypeError")
    if isinstance(gpa, bool) or not isinstance(gpa, (int, float)):
        return ("TypeError")
    parts = fio.split()
    if len(parts) == 0:
        return ("ValueError")
    if len(parts) not in (2, 3):
        return ("ValueError")
    group = group.strip()
    if group == "":
        return ("ValueError")
    if gpa < 0.0 or gpa > 5.0:
        return ("ValueError")
    surname = parts[0].title()
    initials = ""
    for name in parts[1:]:
        initials += name[0].upper() + "."

    return f"{surname} {initials}, гр. {group}, GPA {gpa:.2f}"

test=[("Иванов Иван Иванович", "BIVT-25", 4.6),("Петров Пётр", "IKBO-12", 5.0),("Петров Пётр Петрович", "IKBO-12", 5.0),("  сидорова  анна   сергеевна ", "ABB-01", 3.999),("Анна     ", "ABB-01", 3.999)]
print("\n")
for i in test:
    print(i,' --> ',format_record(i),end="\n\n")