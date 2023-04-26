# 동명이인 찾기
def find_same_name(a):
    same_name = set()
    n = len(a)
    for i in range(0, n-1):
        for j in range(i+1, n):
            if a[i] == a[j]:
                same_name.add(a[i])
    return same_name
    """
    i=0, j=1, a[0] == a[1]
         j=2, a[0] == a[2]  
         j=3, a[0] == a[3]
    i=1, j=2, a[1] == a[2]  
         j=3, a[1] == a[3] '을지문덕'
    i=2, j=3, a[2] == a[3]
         
    """ 
name = ['이순신', '을지문덕', '강감찬', '을지문덕']
print(find_same_name(name))
