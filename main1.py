# b, i
import my_func

for _ in range(5):
    my_func.print_stars()

# ii
from my_func import print_stars

print_stars()

# c
if __name__ == "__main__":
    print("You see this message because I'm the 'main'", __name__)
# d
help(print_stars)
