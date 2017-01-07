lines = [line.rstrip('\n') for line in open('/home/sudarshan/CS229/Assignments/spam_data/out.txt')]
array = list()
for line in lines:
    z = line.split()
    z = [float(x) for x in z]
##    print z
    array.append((z[0], z[1]))

obj = sorted(array, key=lambda x:x[0], reverse=True)

for i in range(0, 5):
    print obj[i]
    
