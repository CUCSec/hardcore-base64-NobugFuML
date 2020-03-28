def trans_code(message,*Indexes):
    temp=""
    transcode=''
    for char in message:
        decnumber=ord(char)
        binnumber='{:08b}'.format(decnumber)
        temp+=binnumber
    k=0
    while(len(temp)%3!=0):
        temp+='00'
        k+=1
    i=6
    for char in temp:
        trans=temp[i-6:i]
        i+=6
        transcode+=indexes[int(trans,2)]
        if i>len(temp):
            break
    if k!=0:
        for char in range(k):
            transcode+='='
    return transcode

def de_code(message):
    temp=''
    decode=''
    k=0
    for char in message:
        if char=='=':
            k+=1
            break
        ind=indexes.find(char)
        ind='{:06b}'.format(ind)
        temp+=ind        
    for x in range(k):
        temp=temp[:-2]
    i=8
    for char in temp:
        trans=temp[i-8:i]
        i+=8
        decnumber=int(trans,2)
        decode+=chr(decnumber)
        if i>len(temp):
            break
    return decode

indexes='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
a=input('加密or解码？:')
if a=='解码':
    message=input('请输入要解码的内容:')
    print(de_code(message))
elif a=="加密" :
    message=input('请输入要加密的内容:')
    print(trans_code(message))
    
else:
    print("请重新输入")
    
