def line(deli_line):
    if not deli_line:
        print("The line is currently empty.")
    else:
        line_str = "The line is currently:"
        for i, person in enumerate(deli_line, start=1):
            line_str += f" {i}. {person}"
        print(line_str)

def take_a_number(deli_line, name):
    deli_line.append(name)
    print(f"Welcome, {name}. You are number {len(deli_line)} in line.")

def now_serving(deli_line):
    if not deli_line:
        print("There is nobody waiting to be served!")
    else:
        serving_person = deli_line.pop(0)
        print(f"Currently serving {serving_person}.")

# deli_line = []
# take_a_number(deli_line, "Ada")
# line(deli_line)
# now_serving(deli_line)
# line(deli_line)
