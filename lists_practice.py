toy = input("Enter your favorite toy: ")
weather = input("Enter your favorite weather: ")
language = input("Enter your favorite language: ")
car = input("Enter your favorite car: ")
club = input("Enter your favorite club: ")


the_list = []
the_list.append(toy)
the_list.append(weather)
the_list.append(language)
the_list.append(car)
the_list.append(club)

for i, favoritething in enumerate(the_list, 1):
    print(f"{i}. {favoritething}")
    