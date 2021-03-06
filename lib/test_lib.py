
UPPER = 7


def emulated_switch(comp):
    return {
        1: lambda: 'hit 1',
        2: lambda: 'hit 2',
        3: lambda: 'hit 3',
        4: lambda: 'hit 4',
    }.get(comp, lambda: None)()


def test_emulated_switch(upper=UPPER):
    for i in range(1, upper):
        print(emulated_switch(i))
