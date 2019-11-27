import Matrix as mx
import numpy as np
import copy


a=np.array([
            [mx.swn(0,"x")],
            [mx.swn(0,"y")],
            [mx.swn(1,"dth")]     
      ])
sk=mx.skew_s(a)
mx.show_swn(sk)
b=np.array([
            [mx.swn(1,"l1")],
            [mx.swn(0,"")],
            [mx.swn(0,"")]     
      ])

mx.show_swn(mx.cmul(sk,b))


