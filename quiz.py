#Q9
'''
#영행렬(1*5)
#영행렬(3*3)
#일행렬(1*5)
import numpy as np

a=np.zeros(5, dtype=int) #뒤에 dtype 생략 가능
print(a)
a=np.zeros((3,3),dtype=int)
print(a)
a=np.ones(5,dtype=float) #flaot로 넣어서 실수형. 1. 1. 1. 1. 1.
print(a)
'''

#Q10
'''
"""
5를 9번
5번 9
단위행렬 3짜
"""
import numpy as np

a=np.tile(5,9)
print(a)
a=np.full(5,9)
print(a)
a=np.eye(3,dtype=int)
print(a)
'''

#Q11
'''
"""
0이상 20미만까지 차이가 1인 등차수열
위의 배열을 4행5열의 행렬로 cnffur
"""
import numpy as np

a=np.arange(20)
print(a)
a=np.reshape(a, (4,5))
print(a)
print(a.reshape(2,10))
print(a)
#np.reshape(a, (x,y) == a.reshape(x,y)
'''

#Q12
'''
"""
1,'A'를 list로 받고 데이터형 확인
위의 리스트를 numpy.array에 넣고 다시 확인
"""
import numpy as np

a=[1,'A']
print(type(a[0]))   #list라서
print(type(a[1]))   #다를 수 있음
a=np.array(a)
print(type(a[0]))   #numpy로 가서
print(type(a[1]))   #같아짐
'''

#Q13
'''
"""
(1)
[[1,2,3], [4,5,6]] 을 DataFrame으로 하나
[[7,8,9],[10,11,12]] 를 또 하나 해서
행으로 하나 합치고 열로 하나 합치기
"""
import pandas as pd

df1=pd.DataFrame({
    'a':[1,2,3],
    'b':[4,5,6]
})
df2=pd.DataFrame({
    'a':[7,8,9],
    'b':[10,11,12]
})
cc=pd.concat([df1,df2], axis=0) #axis=0 은 열로 합침(컬럼 같아야 함)
print(cc)
cc=pd.concat([df1,df2], axis=1) #axis=0 은 행으로 합침(컬럼 달라도 문제 X)
print(cc)
'''
'''
"""
(2)
똑같은 상황에서 컬럼 이름이 달라진다면?
df2 칼럼을 'c', 'd'로
"""
import pandas as pd

df1=pd.DataFrame({
    'a':[1,2,3],
    'b':[4,5,6]
})
df2=pd.DataFrame({
    'c':[7,8,9],
    'd':[10,11,12]
})
cc=pd.concat([df1,df2], axis=0)
print(cc)
cc=pd.concat([df1,df2], axis=1) 
print(cc)
'''

#14
"""
df1은 ['A' 1], ['B' 2], ['C' 3]을 컬럼 x1 x2에 넣고
df2는 컬럼x1에 'B','C','D', x3에 2,3,4 넣음
"""
import pandas as pd

df1 = pd.DataFrame([
    ['A',1],
    ['B',2],
    ['C',3]],
    columns =['x1','x2'] #columns 생략 불가능
)
df2 = pd.DataFrame({
    'x1':['B','C','D'],
    'x3':[2,3,4]
})
print(df1, '\n')
print(df2, '\n')
print(pd.concat([df1,df2], axis=0), '\n')
print(pd.concat([df1,df2], axis=1), '\n')