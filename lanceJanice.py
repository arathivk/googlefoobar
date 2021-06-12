

alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
             'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
s = 'wrw blf hvv ozhg mrtsg'h vkrhlwv?'
solution = ""
for element in s:
    try:
        index = alphabets.index(element)
        charAt = 25 - index
        solution = solution + alphabets[charAt]
    except ValueError:
        # print("List does not contain value")
        decipher = element
        solution = solution + decipher
        continue

print(solution)
