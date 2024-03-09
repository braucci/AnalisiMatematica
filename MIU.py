def apply_rule_1(string):
    if string.endswith('I'):
        return string + 'U'
    return None


def apply_rule_2(string):
    if string.startswith('M'):
        return 'M' + string[1:] * 2
    return None


def apply_rule_3(string):
    return string.replace('III', 'U', 1) if 'III' in string else None


def apply_rule_4(string):
    return string.replace('UU', '', 1) if 'UU' in string else None


def apply_rules(string):
    results = []
    for rule in (apply_rule_1, apply_rule_2, apply_rule_3, apply_rule_4):
        result = rule(string)
        if result:
            results.append(result)
    return results

# Aggiunta di una riga vuota aggiuntiva qui
def miu_system(initial_string, steps):
    current_strings = [initial_string]
    for _ in range(steps):
        next_strings = []
        for string in current_strings:
            next_strings.extend(apply_rules(string))
        current_strings = next_strings
        print(f"Step {_ + 1}: {current_strings}")

initial_string = "MI"
steps = 5  # Numero di iterazioni del sistema
miu_system(initial_string, steps)
