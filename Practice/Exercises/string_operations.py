a = "Buchhaltung"
b = "Python ist toll!"

print(a[5])  # a
print(b[-1])  # !
print(a[:4])  # Buch
print(b[11:16])  # toll!
# Buchhaltung, noth indexes are wider than the actual bounds, so everything will be printed
print(a[-100:100])
print(b.index('o'))  # 4
print("Maximilian".index('x'))  # 2
print("123456789". index('5'))  # 4
print(b.replace("ist", "ist super"))  # Python ist super toll!
print(".....".replace('.', '*'))  # *****
