def calc_arif_p(num, n):
    step = num
    result = []
    for i in range(n):
        result.append(num)
        num += step
    return result

if __name__ == "__main__":
    sequence = calc_arif_p(2, 10)
    for item in sequence:
        print(item)