def merge_strings_alternatively(one: str, two: str) -> str:
    result = ""
    count = 0
    while count < len(one) or count < len(two):
        if count < len(one):
            result += one[count]
        if count < len(two):
            result += two[count]
        count += 1

    return result
