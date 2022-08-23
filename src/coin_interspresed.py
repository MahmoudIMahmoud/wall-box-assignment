def count_changes(coin_list):
    count = 0
    for i in range(0, len(coin_list)):
        if (i % 2) == 0:  # Even
            if coin_list[i] == 1:
                count = count + 1
        else:  # Odd
            if coin_list[i] == 0:
                count = count + 1
    return count


# if __name__ == "__main__":
#     print(count_changes([0, 1, 1, 0, 0, 1]))
#     print(count_changes([0]))
#     print(count_changes([0, 0]))
