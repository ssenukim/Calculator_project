def replace(str, prev, next):
    str_ = str
    cnt = 0
    for i in str_:
        if i==prev:
            print(cnt)
            str_ = str_[:cnt] + next + str_[cnt+1:]
        cnt += 1 
    return str_ 

str = "hello i'am a ssenu"

print(replace(str, 's', '*'))