DAYS = 256
fish = [3, 4, 1, 1, 5, 1, 3, 1, 1, 3, 5, 1, 1, 5, 3, 2, 4, 2, 2, 2, 1, 1, 1, 1, 5, 1, 1, 1, 1, 1, 3, 1, 1, 5, 4, 1,
        1, 1, 4, 1, 1, 1, 1, 2, 3, 2, 5, 1, 5, 1, 2, 1, 1, 1, 4, 1,
        1, 1, 1, 3, 1, 1, 3, 1, 1, 1, 1, 1, 1, 2, 3, 4, 2, 1, 3, 1, 1, 2, 1, 1, 2, 1, 5, 2, 1, 1, 1, 1, 1, 1, 4, 1,
        1, 1, 1, 5, 1, 4, 1, 1, 1, 3, 3, 1, 3, 1, 3, 1, 4, 1, 1, 1,
        1, 1, 4, 5, 1, 1, 3, 2, 2, 5, 5, 4, 3, 1, 2, 1, 1, 1, 4, 1, 3, 4, 1, 1, 1, 1, 2, 1, 1, 3, 2, 1, 1, 1, 1, 1,
        4, 1, 1, 1, 4, 4, 5, 2, 1, 1, 1, 1, 1, 2, 4, 2, 1, 1, 1, 2,
        1, 1, 2, 1, 5, 1, 5, 2, 5, 5, 1, 1, 3, 1, 4, 1, 1, 1, 1, 1, 1, 1, 4, 1, 1, 4, 1, 1, 1, 1, 1, 2, 1, 2, 1, 1,
        1, 5, 1, 1, 3, 5, 1, 1, 5, 5, 3, 5, 3, 4, 1, 1, 1, 3, 1, 1,
        3, 1, 1, 1, 1, 1, 1, 5, 1, 3, 1, 5, 1, 1, 4, 1, 3, 1, 1, 1, 2, 1, 1, 1, 2, 1, 5, 1, 1, 1, 1, 4, 1, 3, 2, 3,
        4, 1, 3, 5, 3, 4, 1, 4, 4, 4, 1, 3, 2, 4, 1, 4, 1, 1, 2, 1,
        3, 1, 5, 5, 1, 5, 1, 1, 1, 5, 2, 1, 2, 3, 1, 4, 3, 3, 4, 3]


def my_solution_bad():

    for c in range(DAYS):
        print(c)
        for item in range(len(fish)):
            fish[item] -= 1
            if fish[item] < 0:
                fish.append(8)
                fish[item] = 6

    print(len(fish))


def good_one_I_learned_from_guy_on_reddit():
    school = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}
    total = len(fish)
    for fishies in fish:
        school[fishies] += 1

    for day in range(DAYS):
        placeholder = school[0]
        school[0] = school[1]
        school[1] = school[2]
        school[2] = school[3]
        school[3] = school[4]
        school[4] = school[5]
        school[5] = school[6]
        school[6] = school[7]
        school[7] = school[8]
        school[6] += placeholder
        school[8] = placeholder

        total += placeholder

    print(total)

# my_solution_bad()
good_one_I_learned_from_guy_on_reddit()
