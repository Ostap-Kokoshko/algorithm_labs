def own_hamster_hunger_sort(hamster_array, hamster_count):
    for i in range(1, hamster_count):
        hamster_check = hamster_array[i]
        j = i - 1
        while j >= 0 and hamster_array[j][0] > hamster_check[0]:
            hamster_array[j + 1] = hamster_array[j]
            j -= 1
        hamster_array[j + 1] = hamster_check
    return hamster_array


def hamster_greed_sort(hamster_array, hamster_count):
    for i in range(1, hamster_count):
        hamster_check = hamster_array[i]
        j = i - 1
        while j >= 0 and hamster_array[j][1] > hamster_check[1]:
            hamster_array[j + 1] = hamster_array[j]
            j -= 1
        hamster_array[j + 1] = hamster_check
    return hamster_array


def compute_corm(sorted_list, max_idx):
    corm = 0
    for i in range(max_idx):
        corm += sorted_list[i][0]
        corm += sorted_list[i][1] * (max_idx - 1)
    return corm


def binary_search(hamster_list, S, left, right):
    while left <= right:
        mid = (left + right) // 2
        corm = compute_corm(hamster_list, mid)
        if corm <= S:
            left = mid + 1
        else:
            right = mid - 1
    return right


def max_hamsters_bst(S, C, hamster_list):
    hungry_list = own_hamster_hunger_sort(hamster_list, C)
    greedy_list = hamster_greed_sort(hamster_list, C)

    max_hungry_idx = binary_search(hungry_list, S, 0, len(hamster_list))
    max_greedy_idx = binary_search(greedy_list, S, 0, len(hamster_list))

    if max_greedy_idx > max_hungry_idx:
        return max_greedy_idx
    return max_hungry_idx

# S - пакети, які я маю на день для хом'ячків
# С - загальна кількість хом'ячків у продажу
# H - денна норма для хом'ячка, перше число у підмасиві
# G - жадібність хом'ячка, скіко він з'їдає корму за кожного наступного хом'ячка (є другим у підмасиві)
