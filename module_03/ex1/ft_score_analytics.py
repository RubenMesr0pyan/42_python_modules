import sys


def validator(score_lst: list) -> list:
    valid_score_lst: list = []
    for elem in score_lst[1:]:
        try:
            convert_to_num = int(elem)
            valid_score_lst.append(convert_to_num)
        except ValueError:
            print(f"Invalid parameter: '{elem}'")
    return valid_score_lst


def analytics(score_lst: list) -> None:
    print(f"Scores processed: {score_lst}")
    print(f"Total players: {len(score_lst)}")
    print(f"Total score: {sum(score_lst)}")
    print(f"Average score: {(sum(score_lst) / len(score_lst)):.1f}")
    print(f"High score: {max(score_lst)}")
    print(f"Low score: {min(score_lst)}")
    print(f"Score range {max(score_lst) - min(score_lst)}")


if __name__ == "__main__":
    print("=== Player Score Analytics ===")
    final_score_lst: list = validator(sys.argv)
    if len(final_score_lst) > 0:
        analytics(final_score_lst)
    else:
        print("No scores provided. Usage: python3 ",
              "ft_score_analytics.py <score1> ...")
