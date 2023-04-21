from django.shortcuts import render
from .models import DashData
from django.db.models import Sum, Count


# 장소명이 같을 경우
# 인원이랑 가격을 더해서
# 인원으로 가격을 나눠서
# 평균 단가를 구한다

# 1. 장소명을 list에 넣고 list 값을 비교?

# Create your views here.
def dashboard(request):
    resName = []

    allData = DashData.objects.values()
    dbCnt = allData.count()

    yangcheon = DashData.objects.filter(borough="yangcheon").values("restaurant").annotate(name_count=Count('restaurant')).filter(name_count__gt=1)
    dobong = DashData.objects.filter(borough="dobong").values("restaurant").annotate(name_count=Count('restaurant')).filter(name_count__gt=1)
    

    for name in yangcheon:
        print(name)
        resName.append(name['restaurant'])
    for name in dobong:
        print(name)
        resName.append(name['restaurant'])

    cntList = len(resName)

    # print(resName)
    # print(cntList)
    num = 0
    numYC = 0
    numDB = 0
    numYC1 = num
    numDB1 = num
    ycList = []
    dobongList = []
    ycCnt = len(ycList)
    dobongCnt = len(dobongList)
    # print("res", resName)
    while True:
        psSum = 0
        prSum = 0
        # db 안에 있는 식당 이름을 식당 리스트와 비교하는 반복문        
        for i2 in range(dbCnt):
            resName2 = allData[i2]['restaurant']
            resName1 = resName[num]
            # print("도움: ", allData[i2]["borough"])
            if allData[i2]["borough"] == "yangcheon":
                print("양천")
                if resName1 in resName2:
                    print(resName1)
                    psSum = allData[i2]['personnel'] + psSum
                    prSum = allData[i2]["price"] + prSum
                    # ycCnt = len(ycCnt)
                    result = prSum / psSum
                    result = round(int(result), -2)
                    if ycCnt == 0:
                        ycList.append([resName1, result])
                    if ycCnt != 0:
                        if resName1 == ycList[numYC1][0]:
                            ycList[numYC] = [resName1, result]
                        elif resName1 != ycList[0][0]:
                            ycList.append([resName1, result])
                            numYC1 +=1
                            numDB+=1
            elif allData[i2]["borough"] == "dobong":
                print("도봉")
                if resName1 in resName2:
                    print(resName1)
                    psSum = allData[i2]['personnel'] + psSum
                    prSum = allData[i2]["price"] + prSum
                    dobongCnt = len(dobongList)
                    result = prSum / psSum
                    result = round(int(result), -2)
                    if dobongCnt == 0:
                        dobongList.append([resName1, result])
                    if dobongCnt != 0:
                        if resName1 == dobongList[numDB1][0]:
                            dobongList[numDB] = [resName1, result]
                        elif resName1 != dobongList[0][0]:
                            dobongList.append([resName1, result])
                            numDB1 +=1
                            numYC+=1
        num += 1
        # numDB+=1
        # numYC+=1

        if num >= cntList:
            break

    print(ycList)
    print(dobongList)
    # topList = []
    # prList = []
    # for pr in lastList:
    #     prList.append(pr[1])

    # prList1 = prList[:]
    # prList1.reverse()

    # for go in range(5):
    #     tmp = prList1.pop()

    #     for top in range(len(lastList)):
    #         if tmp == lastList[top][1]:
    #             topList.append(lastList[top])

    # chartDash = {
    #     "dbDatas": topList
    # }

    return render(request, "dashboard/chart.html")