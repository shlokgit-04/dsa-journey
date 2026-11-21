from day36.group_anagrams import Solution as G
from day36.longest_substring_without_repeating import Solution as L
from day36.reverse_words import Solution as R


def test_group_anagrams():
    out = G().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    assert sorted(map(sorted, out)) == [["ate", "eat", "tea"], ["bat"], ["nat", "tan"]]


def test_group_anagrams_edges():
    assert G().groupAnagrams([""]) == [[""]]
    assert G().groupAnagrams(["a"]) == [["a"]]


def test_lcs_examples():
    l = L()
    assert l.lengthOfLongestSubstring("abcabcbb") == 3
    assert l.lengthOfLongestSubstring("bbbbb") == 1
    assert l.lengthOfLongestSubstring("pwwkew") == 3


def test_lcs_edges():
    l = L()
    assert l.lengthOfLongestSubstring("") == 0
    assert l.lengthOfLongestSubstring(" ") == 1
    assert l.lengthOfLongestSubstring("abba") == 2


def test_reverse_words():
    r = R()
    assert r.reverseWords("the sky is blue") == "blue is sky the"
    assert r.reverseWords("  hello world  ") == "world hello"


def test_reverse_words_single():
    assert R().reverseWords("a good   example") == "example good a"
    assert R().reverseWords("x") == "x"
