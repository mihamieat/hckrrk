from collections import Counter


def inventory(list_of_shoe_sizes):
    inventory = Counter(list_of_shoe_sizes)
    return inventory


if __name__ == "__main__":
    number_of_shoes = int(input())
    list_of_shoe_sizes = list(map(int, input().split()))
    number_of_customers = int(input())
    shoes_inventory = inventory(list_of_shoe_sizes)
    money = 0
    for _ in range(number_of_customers):
        shoes_size, price = list(map(int, input().split()))
        if shoes_inventory[shoes_size] != 0:
            money += price
            shoes_inventory[shoes_size] -= 1
        else:
            pass
    print(money)
