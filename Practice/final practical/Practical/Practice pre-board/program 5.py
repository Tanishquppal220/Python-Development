employees={'Pooja' : 70000, 'Nidhi' :40000, 'Bittu':80000, 'Anu': 16000, 'Anand':90000, 'Vanita': 34000}
stack = []


def push_to_stack(employees):
    for name, salary in employees.items():
        if salary > 50000:
            stack.append(name)


def pop_from_stack():
    while stack:
        print(stack.pop())


push_to_stack(employees)
pop_from_stack()
