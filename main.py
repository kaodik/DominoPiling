inp1 = input()
def print_hi(inp1):
    M = inp1.split(" ")[0]
    N = inp1.split(" ")[1]
    damino = 0
    count = 0
    spaces = int(M) * int(N)
    for x in range(spaces):
        count +=1
        if count % 2 == 0:
            count =0
            damino +=1;
    print(damino)
if __name__ == '__main__':
    print_hi(inp1)
