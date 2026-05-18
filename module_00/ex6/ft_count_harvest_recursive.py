def ft_count_harvest_recursive() -> None:
    n = int(input("Days until harvest: "))

    def helper(current: int) -> None:
        if current > n:
            return
        print(f"Day {current}")
        helper(current + 1)

    helper(1)
    print("Harvest time!")
