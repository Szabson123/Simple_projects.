import random


def user_input():
    return list(input("Podaj liczbę: "))


def shuffle():
    a = list(range(10))
    random.shuffle(a)
    return [str(i) for i in a[:3]]


def rules(shuffle_val):
    user_input_val = user_input()
    if len(user_input_val) != 3:
        return "Musisz podać 3 cyfrową liczbę!!"

    if user_input_val == shuffle_val:
        return "Wygrałeś!"

    matches = sum([shuffle_val[i] == user_input_val[i] for i in range(len(shuffle_val))])
    if matches > 0:
        return "Match!"

    if any(x in user_input_val for x in shuffle_val):
        return "Close!!"

    return "Nothing"


def main():
    shuffle_val = shuffle()
    while True:
        result = rules(shuffle_val)
        print(result)
        if result == "Wygrałeś!":
            break


if __name__ == '__main__':
    main()