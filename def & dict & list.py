# 傳入數據返回字典
def test(n,a):
   d = {'name':n,'age':a}
   return d

print(test('siki',18))

# 函數內操作列表
l = ['micheal','libai','dufu','kongzi']
def test(l):
   del(l[1])

# test(l) # 🐾函數內可以修改傳進去的列表
test(l[:]) # 複製列表再傳入, 以避免被函數內修改
print(l)