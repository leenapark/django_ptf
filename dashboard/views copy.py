
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
    resName = []
    testList = {}
    # resultNum = DashData.objects.aggregate(Sum("price"))["price__sum"]
    # print(resultNum)

    test = DashData.objects.values()
    dbCnt = test.count()
    # print(test.count())
    testCnt = DashData.objects.values("restaurant").annotate(name_count=Count('restaurant')).filter(name_count__gt=1)
    test1 = DashData.objects.values("restaurant")
    for ck in testCnt:
        print(ck)
    testCnt = testCnt.count()

    # print("type: ", type(test))
    # print("ch: ", test[0])
    # print(test.count())
    print(test)
    
    # for name in test1:
        # print(name)
        # print(name['restaurant'])
        # resName.append(name['restaurant'])
        # print(resName[0])
    # for i2 in range(testCnt):
    #     resName1 = test1[0]['restaurant']
    #     for i in range(dbCnt):
    #         # print(len(test1[i]['restaurant']))
    #         # print(test1)
    #         # test1[i]['restaurant']
    #         # resName1 = test1[0]['restaurant']
    #         resName2 = test[i]['restaurant']
        
    #         if resName1 in resName2:
    #             print(test[i])
    #             # pass


    # for i in range(dbCnt):
    #     # print(len(test1[i]['restaurant']))
    #     # print(test1)
    #     # test1[i]['restaurant']
    #     for i2 in range(testCnt):
    #         resName1 = test1[0]['restaurant']
    #         resName2 = test[i]['restaurant']
    #         if resName1 in resName2:
    #             print(resName2)


    num = 0
    result = 0
    stopCnt = 0
    # for i in range(testCnt):
        # print(len(test1[i]['restaurant']))
        # print(test1)
        # test1[i]['restaurant']
    while True:
        for i2 in range(dbCnt):
            resName1 = test1[num]['restaurant']
            resName2 = test[i2]['restaurant']
            if resName1 in resName2:
                print("num", num)
                # print(resName2)
                # print(test[num])
                result = test[i2]['personnel'] + result
                print(test[i2])
                # print(result)
        num += 1
        if num >= testCnt:
            break



    

    # for i2 in range(dbCnt):
    #     testList.append(test[i2])
    # print(testList[0])

    # print(resName[5])
    # for i in range(test1.count()):
    #     for i2 in range(dbCnt):
    # #         print(i2)
    #         if resName[i] == test[i2]['restaurant']:
    #             testList = {test}
    #             print(testList)

                # pass
        # if resName[0] == test[i]["restaurant"]:
        #     print("여기")
        #     print(test[0]['personnel'])
        #     # print(test)
        #     # print(resName)
        #     continue




    # cntTest = len(resName)
    # print(cntTest)


    # while True:
    #     cnt = 0
    #     if resName[0] == test[cnt]["restaurant"]:
    #         print("여기")
    #         print(test[0]['personnel'])
    #         # print(test)
    #         # print(resName)
    #         cnt +=1
    #     elif cnt > cntTest:
    #         break


    # chartDash = {
    #     "dbDatas": dbDatas
    # }

    return render(request, "dashboard/chart.html",)