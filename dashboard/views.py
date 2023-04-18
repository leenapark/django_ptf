from django.shortcuts import render
import csv



# Create your views here.
def dashboard(request):
    dataList = []
    path = "./dashboard/data/dobong/202212.csv"
    file = open(path)
    data = csv.reader(file)
    print(data)

    for dbData in data:
        # print(dbData)
        if dbData[6] != "" and "장소" not in dbData[6]:
            del dbData[0]
            del dbData[0]
            del dbData[0]
            dbData[0] = dbData[0].split("(")
            dbData[0] = dbData[0][0].rstrip(".")
            dbData[0] = dbData[0].replace(".", "-")
            dbData[0] = "2022-" + dbData[0]
            del dbData[1]
            del dbData[4]
            del dbData[4]
            dbData[1], dbData[2] = dbData[2], dbData[1]
            dataList.append(dbData)

    print(dataList)
    with open("./dashboard/data/dobong/dobong.csv", "a", newline="") as f:               
      writer = csv.writer(f)
      writer.writerows(dataList)
      print(dataList)
      f.close() 
    return render(request)