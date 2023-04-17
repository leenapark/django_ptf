from django.shortcuts import render
import csv



# Create your views here.
def dashboard(request):

    # gangseo = []
    dataList = []
    # # 데이터에서 장소를 찾아서 행을 추출한다
    # # 장소 데이터 testData[3]
    
    # path = "./dashboard/data/Guro/202206.csv"
    # file = open(path)
    # data = csv.reader(file)
    # # print("data", data)
    # for testData in data:
    #   # print("data", testData[3])
    #   if testData[3] != "":
    #     if "장소" not in testData[3] and "총" not in testData[3]:
    #       # print("hang", testData[3].replace("\n", "/"))
    #       testData[2] = testData[2].split("\n")
    #       testData[2] = testData[2][0]
    #       testData[3] = testData[3].split("\n")
    #       testData[3] = testData[3][0]
    #       # testData[5] = testData[5].split("\n")
    #       # testData[5] = testData[5][0]
    #       # print("{%Y%m%d}".format(int(testData[2])))
    #       # print(testData)
    #       del testData[1]
    #       del testData[3]
    #       # del testData[3]
    #       del testData[5]
    #       # del testData[]
    #       gangseo.append(testData)
    #       # print(testData)
        

    # print(gangseo)


    # with open("./dashboard/data/gangseo.csv", "a", newline="") as f:               
    #   writer = csv.writer(f)
    #   writer.writerows(gangseo)
    #   print(gangseo)
    #   f.close()

    #         #   addData = addData.replace("\n", "/").split("/")
    #         #   print("line", addData)

    # # with file as testfile:
    # #     testfile.readline()
    # path("")
    # path = "./dashboard/data/Guro/202212.csv"
    # file = open(path)
    # data = csv.reader(file)
    # # print(data)
    # for testData in data:
    #   if testData[6] != "" and "장소" not in testData:
    #     testData[1] = testData[1].split("\n")
    #     testData[1] = testData[1][0]
    #     del testData[0]
    #     del testData[2]
    #     del testData[4]
    #     del testData[4]
    #     print("data", testData)
    #     testData[1] = testData[1].replace("?", " ")
    #     testData[1] = testData[1].replace("\n", " ")
    #     dataList.append(testData)
    #     # print(testData)
        

    # print(dataList)


    # with open("./dashboard/data/Guro/Guro.csv", "a", newline="") as f:               
    #   writer = csv.writer(f)
    #   writer.writerows(dataList)
    #   print(dataList)
    #   f.close()    


    path = "./dashboard/data/geumcheon/202208.csv"
    file = open(path)
    data = csv.reader(file)
    print(data)
    for testData in data:
      # print(testData)
      if "장소" not in testData and testData[1] != "":
        testData[2] = testData[2].split("\n")
        testData[2] = testData[2][0]
        testData[3] = testData[3].split("\n")
        testData[3] = testData[3][0]
        del testData[0]
        del testData[0]
        del testData[2]
        del testData[2]
        del testData[4]
      #     print("data", testData)
      #     testData[1] = testData[1].replace("?", " ")
        dataList.append(testData)
        print(testData)
          

    print(dataList)


    with open("./dashboard/data/geumcheon/geumcheon.csv", "a", newline="") as f:               
      writer = csv.writer(f)
      writer.writerows(dataList)
      print(dataList)
      f.close()    

    return render(request)