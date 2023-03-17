# python3


def build_heap(data):
    swaps = []
    n = len(data)
    for i in range(n//2, -1,-1):
        down(i, data,swaps)
    return swaps

def down(i, data,swaps):
    n = len(data)
    min_in = i 
    left_ch = 2*i + 1
    if left_ch < n and data[left_ch] < data[min_in]:
        min_in = left_ch
    right_ch = 2*i + 2
    if right_ch < n and data[right_ch] < data[min_in]:
        min_in = right_ch
    if i != min_in:
        swaps.append((i, min_in))
        data[i], data[min_in] = data[min_in], data[i]
        down(min_in, data, swaps)

def main():
    input_type = input()
    if 'I' in input_type:
        n = int(input())
        data = list(map(int, input().split()))
        assert len(data) == n
        swaps = build_heap(data)
        print(len(swaps))
        for i, j in swaps:
            print(i, j)
    
    elif 'F' in input_type:
        
        filename = input()
        with open("tests/" + filename, 'r') as f:
            n = int(f.readline())
            data = list(map(int, f.readline().split()))
            assert len(data) == n
            swaps = build_heap(data)

            print(len(swaps))
            for i, j in swaps:
                print(i, j)
    else:
        print("Error")
        exit()


if __name__ == "__main__":
    main()
