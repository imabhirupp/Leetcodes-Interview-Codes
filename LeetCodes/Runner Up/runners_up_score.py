if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

a = sorted(list(set(arr)))

if 2<= n <=10:
    print(a[-2])
        
