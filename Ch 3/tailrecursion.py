def natural_sum(count, sum_total = 0, output = False):
    if count == 0:
        return sum_total
    else:
        if output:
            print("Current Total: {}".format(sum_total))
            return natural_sum(count-1, sum_total + count, True)
        else:
            return natural_sum(count-1, sum_total + count)

if __name__ == "__main__":
    print(natural_sum(14))
    print(natural_sum(6, 0, True))