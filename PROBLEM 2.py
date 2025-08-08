a = int(input("Enter a no: "))
if a % 2 == 0:
    a -= 1 
count = 0
num = 1
output = []
while count < a:
    output.append(str(num))
    num += 2
    count += 1

print(",".join(output))
