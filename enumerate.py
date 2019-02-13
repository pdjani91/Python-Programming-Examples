# how we can do this without  enumerate function
# names = ['PARTH','ANKUR','KARAN']
# pos = 0
# for name in names:
#     print(f"{pos}--->{name}")
#     pos += 1
# Output:
# 0--->PARTH
# 1--->ANKUR
# 2--->KARAN
# ===========================================================
#With Enumerate Function
names = ['PARTH','ANKUR','KARAN']
# for pos,name in enumerate(names):
#     print(f"{pos}--->{name}")
# ===========================================================
def find_pos(l,target):
    for pos,name in enumerate(l):
        if name == target:
            return pos
        return -1
print(find_pos(names,'PARTH'))