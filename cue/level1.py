#!/usr/bin/env python

"""
The Cue Programming Challenge
Level 1
"""

def is_palindrome(word):
    word = str(word)
    if len(word) is 0: return False
    return word == word[::-1]


def largest_palindrome(text):
    text = str(text)

    if is_palindrome(text):
        return text

    text_length = len(text)
    word_length = text_length
    left = 1

    while word_length > 1:
        word_length = text_length - left

        for offset in xrange(text_length - word_length):
            word = text[left-offset-1:text_length-offset]

            if is_palindrome(word):
                return word

        left += 1

    return None


def test():
    assert(is_palindrome('a'))
    assert(is_palindrome('racecar'))
    assert(not is_palindrome(''))
    assert(not is_palindrome('bacon'))
    print largest_palindrome('a')

    assert(largest_palindrome('') == None)
    assert(largest_palindrome('bacon') == None)
    assert(largest_palindrome('a') == 'a')
    assert(largest_palindrome('aba') == 'aba')
    assert(largest_palindrome('abba') == 'abba')
    assert(largest_palindrome('baconracecar') == 'racecar')
    assert(largest_palindrome('baconracecarbacon') == 'racecar')


def answer():
    return largest_palindrome("FourscoreandsevenyearsagoourfaathersbroughtforthonthiscontainentanewnationconceivedinzLibertyanddedicatedtothepropositionthatallmenarecreatedequalNowweareengagedinagreahtcivilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth")


def main():
    test()
    print answer()


if __name__ == "__main__":
    import sys
    sys.exit(main())
