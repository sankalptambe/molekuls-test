import typing

# returns True on finding a triplet, else False
def main(numbers: typing.List[int], target_sum: int):

    for i in range(0, len(numbers) - 1):

        # checking target_sum - numbers[i] - numbers[j] is in set
        s = set()

        tmp_sum = target_sum - numbers[i]

        for j in range(i + 1, len(numbers)):
            if (tmp_sum - numbers[j]) in s:
                return True
            s.add(numbers[j])

    return False

if __name__ == "__main__":

    assert (main([5, 4, 10, 7, 1, 9], 13) is True), "Triplet exists"
    assert (main([4, 2, 5, 9, 11, 23], 9) is False), "Triple does not exist"
