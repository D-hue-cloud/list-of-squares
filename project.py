start=int(input("Enter start of range: "))
end=int(input("Enter end of range: "))

squares= [x**2 for x in range(start, end+1)]
print(squares)