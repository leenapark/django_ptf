from django.shortcuts import render
from .models import DashData
from django.db.models import Sum
from django.db.models import Count

# 장소명이 같을 경우
# 인원이랑 가격을 더해서
# 인원으로 가격을 나눠서
# 평균 단가를 구한다

# 1. 장소명을 list에 넣고 list 값을 비교?

# Create your views here.
def dashboard(request):
    resName = [] # 비교 기준 장소명 : 장소
    # testList = {}


    test = DashData.objects.values()
    dbCnt = test.count()
    # print("db", test)

    testCnt = DashData.objects.values("restaurant").annotate(name_count=Count('restaurant')).filter(name_count__gt=1)
    test1 = DashData.objects.values("restaurant")
    
    # 중복 값 거른 식당 이름
    for name in testCnt:
        print(name)
        # print(name['restaurant'])
        resName.append(name['restaurant'])
        # print(resName[0])

    cntList = len(resName)
    # print(cntList, type(cntList))
    # for ck in testCnt:
    #     print(ck)
    # testCnt = testCnt.count()

    # print(test)

    num = 0
    
    lastList = []

    while True:
        psSum = 0
        prSum = 0
        for i2 in range(dbCnt):
            print(type(num))
            resName2 = test[i2]['restaurant']
            print(resName[0])
            if resName[num] in resName2:
                print("num", num)
                # print(resName2)
                # print(test[num])
                psSum = test[i2]['personnel'] + psSum
                print(test[i2])
                print("psSum", psSum)
                prSum = test[i2]["price"] + prSum
                print("prSum", prSum)
                result = prSum / psSum
                result = round(int(result), -2)
                print("result", result)
                # list가 빈 리스트가 아닐때
                # if lastList != "":
                #     # 리스트 안에 장소가 없으면 추가
                #     if resName[num] != lastList[num][0]:
                #         lastList.append([resName[num], result])
                #     # 리스트 안에 장소가 있으면 result 값 update
                #     elif resName[num] == lastList[num][0]:
                #         lastList[num][1] = result
                # else:
                #     lastList.append([resName[num], result])
        num += 1
        if num >= cntList:
            break
        
        print(lastList)

    chartDash = {
        "dbDatas": lastList
    }

    return render(request, "dashboard/chart.html", chartDash)