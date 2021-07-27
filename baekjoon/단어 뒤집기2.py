strs = input()
answer = ''
li = strs.replace('>','<').split('<')

for i in range(len(li)):
    if i % 2 != 0 :
        answer += '<'+ li[i] + '>'
    else :
        non_tag_li = li[i].split(' ')
        answer += ' '.join([word[::-1] for word in non_tag_li])
    
print(answer)
