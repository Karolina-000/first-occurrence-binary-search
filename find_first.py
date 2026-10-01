from sorted_numbers import numbers


def find_first(target):
    left, right = 0, len(numbers)

    while left < right:
        mid = (left + right) // 2

        if numbers[mid] < target:
            left = mid + 1
        else:
            right = mid

    if left < len(numbers) and numbers[left] == target:
        return left
    return -1


target = int(input("შეიყვანე რიცხვი: "))
index = find_first(target)

if index == -1:
    print(f"რიცხვი {target} სიაში არ არის")
else:
    print(f"რიცხვი {target} პირველად გვხვდება ინდექსზე: {index}")