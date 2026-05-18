def ft_count_harvest_iterative() -> None:
    days_str = input("Days until harvest: ")
    n = int(days_str)
    for i in range(1, n + 1):
        print(f"Day {i}")
    print("Harvest time!")
