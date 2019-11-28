import Matrix as mx
import numpy as np
import copy


# a=np.array([
#             [mx.swn(1,"l2c_12"),mx.swn(1,"l_2s_12")],
#             [mx.swn(-1,"l_1c_1+l2c_12"),mx.swn(-1,"l_1s_1+l_2s_12")]   
#       ])
# #sk=mx.skew_s(a)
# b=np.array([
#             [mx.swn(1,"")],
#             [mx.swn(0,"")]     
#       ])
# print(a.shape)
# print(b.shape)

# mx.show_swn(mx.cmul(a,b))

# sk=mx.skew_s(np.array([
#     [mx.swn(1,"l2x2")],
#     [mx.swn(0,"")],
#     [mx.swn(0,"")]
# ]    
# ))
# mx.show_swn(sk)
# b=np.array([
#     [mx.swn(1,"fx")],
#     [mx.swn(1,"fy")],
#     [mx.swn(0,"")]
# ])

sk=mx.skew_s(np.array([
    [mx.swn(1,"x")],
    [mx.swn(0,"")],
    [mx.swn(0,"")]
]    
))
mx.show_swn(sk)
print("bbbbbbbb")
b=np.array([
    [mx.swn(1,"a")],
    [mx.swn(1,"b")],
    [mx.swn(0,"")]
])
mx.show_swn(mx.cmul(sk,b))
