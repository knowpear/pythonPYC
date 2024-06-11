# 全部導入
# import test
# test.test1()

# 部分導入
from test import test1,test2

# 導入並改方法名
from test import test3 as t
t()

# 導入並改模塊名
import test as te
te.test1()