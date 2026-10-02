numbers_1 = [1, 2, 2, 3, 4, 5, 2, 6]
numbers_2 = [7, 7, 3, 3, 7, 5, 5, 5, 7, 2]
numbers_3 = [9, 9, 8]  # Regression case: lower max than previous lists

all_lists = [numbers_1, numbers_2, numbers_3]

for current_list in all_lists:
    # Reset per list -> otherwise the previous list's winner leaks into the next result
    most_frequent_number = 0
    max_counter = 0

    for i in current_list:
        counter = 0
        for j in current_list:
            if i == j:
                counter += 1

        if counter > max_counter:
            max_counter = counter
            most_frequent_number = i

    print(f"List: {current_list}")
    print(f"Most frequent number: {most_frequent_number}")
    print(f"Frequency: {max_counter}")
    print("-" * 30)
