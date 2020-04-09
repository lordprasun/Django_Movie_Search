
class Solution:
    def reverseString(self, s):
        def helper(left, right):
            if left < right:
                s[left], s[right] = s[right], s[left]
                helper(left + 1, right - 1)

        helper(0, len(s) - 1)


def reverse(string):
    if len(string) == 0:
        return string
    else:
        return reverse(string[1:]) + string[0]

def main(options):
    if options == 1:
        a = str(input("Enter the string to be reversed: "))
        print(reverse(a))    


if __name__ =='__main__':
    main(1)
    