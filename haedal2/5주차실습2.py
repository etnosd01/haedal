with open("new1.txt", 'w') as f:
    for i in range(10):
        i+=1
        data = "피카츄는 푹 쉬었다! 체력이 %d가 되었다." % i
        f.write(data)
        f.write("\n")