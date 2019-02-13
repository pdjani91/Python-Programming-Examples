def word_counter(s):
    count = {}
    for char in s:
        count[char] = s.count(s)
    return count

print (word_counter('harshit'))