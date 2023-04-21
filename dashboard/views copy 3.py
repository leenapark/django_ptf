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
    testList = {}


    test = DashData.objects.values()
    dbCnt = test.count()

    testCnt = DashData.objects.values("restaurant").annotate(name_count=Count('restaurant')).filter(name_count__gt=1)
    # test1 = DashData.objects.values("restaurant")
    # testSum = DashData.objects.values("restaurant").annotate(name_sum=Sum('restaurant')).filter(name_count__gt=1)
    # order = testCnt.order_by('-name_count')[:5]
    
    for name in testCnt:
        # print(name)
        # print(name['restaurant'])
        resName.append(name['restaurant'])
        # print(resName)

    cntList = len(resName)
    # print(cntList, type(cntList))
    # for ck in testCnt:
    #     print(ck)
    # testCnt = testCnt.count()

    # print(test)

    num = 0
    num2 = num
    lastList = []
    listCnt = len(lastList)
    print("res", resName)
    while True:

        psSum = 0
        prSum = 0
        # db 안에 있는 식당 이름을 식당 리스트와 비교하는 반복문        
        for i2 in range(dbCnt):

            resName2 = test[i2]['restaurant']
            resName1 = resName[num]
            if resName1 in resName2:
                # print("num", num)
                # print(resName2)
                # print(test[num])
                psSum = test[i2]['personnel'] + psSum
                # print(test[i2])
                prSum = test[i2]["price"] + prSum
                # print(resName[num])
                # print("psSum", psSum, test[i2])
                # print("prSum", prSum)
                listCnt = len(lastList)
                # print("listCnt", listCnt)
                # for ehwjs in range(cntList):
                result = prSum / psSum
                result = round(int(result), -2)

                if listCnt == 0:
                    lastList.append([resName1, result])
                    # continue
                if listCnt != 0:
                    # print("밖", num2)
                    if resName1 == lastList[num2][0]:
                        # print("num2", num2)
                        # print(lastList[0][0])
                        # print("같다")
                        lastList[num] = [resName1, result]
                        # num2 +=1
                    elif resName1 != lastList[0][0]:
                        # print("num2", num2)
                        # print(lastList[0][0])                        
                        # print("다르다")
                        lastList.append([resName1, result])
                        num2 +=1
                    
                        
                # TestData.objects.update_or_create(
                #     restaurant = resName1,

                #     defaults={
                #         "restaurant" : resName1,
                #         "psSum": psSum,
                #         "prSum": prSum
                #     }
                # )
    #             resName1 = [resName1, psSum, prSum]
    #             # result = prSum / psSum
    #             # result = round(int(result), -2)
    #             # print("result", result)
    #             # print(test[i2])
                # lastList.append([resName[num], result])
                
        num += 1
        # num2 +=1
        if num >= cntList:
            break
        

        # print("last", lastList)
        # print(lastList[0][1]/)
    i = 0
    topList = []
    prList = []
    for pr in lastList:
        prList.append(pr[1])
        
        # if top[1] > 50:
            # topList.append(top)
    print(prList)
    prList1 = prList[:]
    prList1.reverse()
        # # print(topList.reverse())

    for go in range(5):
        tmp = prList1.pop()
        # print(tmp, "Index : ",prList.index(tmp))
        for top in range(len(lastList)):
            if tmp == lastList[top][1]:
                topList.append(lastList[top])


    chartDash = {
        "dbDatas": topList
    }

    return render(request, "dashboard/chart.html", chartDash)