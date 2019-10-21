def single_number(nums):
    hash_table = {}

    for i in nums:
        try:
            hash_table.pop(i)
        except:
            hash_table[i] = 1

    return hash_table.popitem()[0]


def single_number_on_steroids(nums):
    a = 0

    for i in nums:
        a ^= i

    return a


if __name__ == "__main__":
    nums = [2, 3, 2, 4, 3, 4, 0, 8, 2, 7, 0, 8, 7, 1, 2]
    single_umber(nums)
    single_umber2(nums)
