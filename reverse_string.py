"""Reverse string
"""
# Method 1: convert to list, and used reverse method
a_str = "abcdef"
a_list = list(a_str)
a_list.reverse()
# also can used sort method, but sorting only based on english word to priority not based on string priority
# a_list.sort(reverse=True)
a_result = "".join(a_list)

# Method 2: iterate string and revert reference
b_str = "abcdef"
b_result = ""
for v in b_str:
    b_result = v + b_result


# Method 3: revert string
c_str = "abcdef"
c_result = c_str[::-1]


# Method 4: recursion
def recursion(a):
    if len(a) <= 1:
        return a
    result = a[-1] + foo(a[:-1])
    print(result)
    return result


if __name__ == "__main__":
    recursion("abdef")
