def finite_automata(pattern, text):
    pattern_length = len(pattern)
    text_length = len(text)
    transition_function = compute_transition_function(pattern, pattern_length)
    result = []

    current_state = 0
    for letter_position in range(text_length):
        current_state = transition_function[current_state][ord(text[letter_position])]
        if current_state == pattern_length:
            result.append(letter_position - pattern_length + 1)

    return result


def compute_transition_function(pattern, pattern_length):
    transition_function = [[0 for _ in range(256)] for _ in range(pattern_length + 1)]

    for state in range(pattern_length + 1):
        for character in range(256):
            next_state = get_next_state(pattern, pattern_length, state, character)
            transition_function[state][character] = next_state

    return transition_function


def get_next_state(pattern, pattern_length, current_state, character):
    if current_state < pattern_length and character == ord(pattern[current_state]):
        return current_state + 1

    for next_state in range(current_state, 0, -1):
        if ord(pattern[next_state - 1]) == character:
            i = 0
            while i < next_state - 1:
                if pattern[i] != pattern[current_state - next_state + 1 + i]:
                    break
                i += 1
            if i == next_state - 1:
                return next_state
    return 0
