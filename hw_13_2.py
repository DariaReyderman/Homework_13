# a
max_in_class: int = 30
total_in_school: int = 103
pupils: int = int(input("How many pupils will be studying this year? "))
print(f"We will have {pupils // max_in_class} full classes and one class for the rest {pupils % max_in_class} pupils.")

# b
x: int = 0
while True:
    try:
        x: int = int(input("Enter a number: "))
        tens: int = x // 10
        units: int = x % 10
        new_x: int = units * 10 + tens * 1
        if not 10 <= x <= 99:
            continue
        if tens < units:
            print(f'{x} ==> {new_x}')
            break
        else:
            print(x)
            break
    except ValueError as e:
        print("Only numbers are acceptable, try again")
        continue

# c
print([x for x in range(2, 200 + 1) if all([x % i for i in range(2, x)])])

# d
SENTINEL: str = 'x'
answers: list[str] = ['a', 'b', 'c', 'd']
count_answers: list[int] = [0, 0, 0, 0]
while True:
    answer: str = input("What is your answer? ")
    if answer == SENTINEL:
        break
    if answer == 'a':
        count_answers[0] += 1
    if answer == 'b':
        count_answers[1] += 1
    if answer == 'c':
        count_answers[2] += 1
    if answer == 'd':
        count_answers[3] += 1
    if answer != 'a' and answer != 'b' and answer != 'c' and answer != 'd':
        print("Invalid answer, try again")
        continue
print(f"Statistics of answers:\n"
      f" 'a' = {count_answers[0]},\n"
      f" 'b' = {count_answers[1]},\n"
      f" 'c' = {count_answers[2]},\n"
      f" 'd' = {count_answers[3]},\n"
      f"The most popular answer: {answers[count_answers.index(max(count_answers))]}\n"
      f"The most unpopular answer: {answers[count_answers.index(min(count_answers))]}")
