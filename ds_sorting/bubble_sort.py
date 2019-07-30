class BubbleSort:

    def sortElements(self, data):
        n = len(data)
        for value in range(0, n-1):
            for x in range(0, n-1):
                if data[value] < data[x]:
                    temp = data[x]
                    data[x] = data[value]
                    data[value] = temp
        print(data)

