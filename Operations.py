from Sample import Sample

obj = Sample("Alice")
print(obj.greet())

result_add = obj.Add(5, 3)
print(f"Addition Result: {result_add}")

result_sub = obj.Sub(10, 4)
print(f"Subtraction Result: {result_sub}")

result_mul = obj.Mul(6, 7)
print(f"Multiplication Result: {result_mul}")