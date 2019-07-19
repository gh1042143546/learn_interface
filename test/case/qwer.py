# -*- coding:utf-8 -*-
# Author:Gehao
from deptest import depend_on

@depend_on('test_b',with_return=True)
def test_a(name):
    print("abc"+name)

def test_b():
    #print("dfg")
    name ="def"
    return name


test_a()