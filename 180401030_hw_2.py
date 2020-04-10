import sys

frek = []
ay = {}

def hist(dosya):
    for i in dosya:
        frek.append(int(i.split(";")[3].split("-")[1]))

    for item in frek:
        if(item in ay.keys()):
            ay[item] = ay[item] + 1
        else:
            ay[item] = 1
    return ay




def sortValues(ay):
    sortedhist = sorted(ay.items(), key = lambda t:t[1])
    return sortedhist




def medyan():
    ayMedyan = sortValues(ay)
    n = len(ayMedyan)
    if n % 2 == 1:
        middle = int(n / 2)
        return ayMedyan[middle][1]


    else:
        middle_1 = ayMedyan[int(n / 2)][1]
        middle_2 = ayMedyan[int(n / 2) - 1][1]
        medyan = (middle_1 + middle_2) / 2
        return medyan





def average():
    ayAverage = list(ay.values())
    sum = 0
    counter = 0
    for i in range(len(ay)):
        sum = sum + ayAverage[i]
        counter += 1
    return sum / counter



def output(average, medyan):
    fnew = open(sys.argv[2], "w+")
    fnew.write("Medyan = ")
    fnew.write(str(medyan))
    fnew.write("\n")
    fnew.write("Ortalama = ")
    fnew.write(str(average))
    fnew.close()



with open(sys.argv[1]) as dosya: 
    histogram = hist(dosya)
    output(average(), medyan())
    print("histogram = ", histogram)
    print("sorted histogram = ", sortValues(ay))
