# Theory
# syntax: lambda arguments: expression
# your_function_name = lambda inputs : output
    # arguments：一个或多个参数，它们之间用逗号隔开，不需要括号包围（除非有默认参数或*args/**kwargs）。
    # expression：一个计算表达式，其结果作为 lambda 函数的返回值。注意，lambda 函数只能有一行表达式，不能包含复杂的语句或赋值操作。
# inline functions defined at the same place we use it.
# So we don't need to declare a function somewhere and revisit the code just for a single time use.
    # result = your_function_name(actual parameters)
    # 就是函數的簡寫, 也是需要傳參的
# 📚[6. Expressions — Python 3.12.3 documentation](https://docs.python.org/3/reference/expressions.html#lambda)

# eg
sum = lambda x,y : x + y
c = sum(1,2)
print(c)
# 📚[Lambda functions - Learn Python - Free Interactive Python Tutorial](https://www.learnpython.org/en/Lambda_functions)