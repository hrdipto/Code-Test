strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

group_word = []
group_word.append([strs[0]])

if len(strs) == 0:
    print("Words are missing")
    
else:
    for item in strs[1:]:
        flag = 1
        for row in group_word:

            if sorted(list(row[0])) == sorted(list(item)):
                flag = 0
                row.append(item)
                break
        if flag:
            group_word.append([item])
    

print(group_word)




