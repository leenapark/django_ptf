from django.shortcuts import render
from .models import *
from django.db.models import Sum, Count
import json
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.core.serializers.json import DjangoJSONEncoder
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
# 장소명이 같을 경우
# 인원이랑 가격을 더해서
# 인원으로 가격을 나눠서
# 평균 단가를 구한다

# 1. 장소명을 list에 넣고 list 값을 비교?
@csrf_exempt
@api_view(['POST'])
# Create your views here.
def post_api(request):
    if request.method == "POST":
        # print(request.POST.get(data))
        print("post")
        check = request.POST.get("borough")
        print(check)
        # ycResName = []
        # dbResName = []
        test = []
        # ycallCnt = DashData.objects.filter(borough="yangcheon").values("id")
        # dobondAllCnt = DashData.objects.filter(borough="dobong").values("id")
        # # print(allData[dobondAllCnt])
        # dobondAllCnt = list(dobondAllCnt[0].values())
        # numDB = int(dobondAllCnt[0])
        allData = DashData.objects.filter(borough=check).values()
        jsonCk = allData.count()
        # print("test1", test1[0]["restaurant"])
        boroughData = DashData.objects.filter(borough=check).values("restaurant").annotate(name_count=Count('restaurant')).filter(name_count__gt=1)
        # dobong = DashData.objects.filter(borough="dobong").values("restaurant").annotate(name_count=Count('restaurant')).filter(name_count__gt=1)
        # print("test2", test2)
        order = boroughData.order_by('-name_count')[:5]
        odCnt = order.count()
        borList = []
        borCnt = len(borList)

        num = 0
        numBor = 0
        numYC = 0
        numYC1 = numYC
        ycList = []
        ycCnt = len(ycList)
        while True:
            psSum = 0
            prSum = 0
            # db 안에 있는 식당 이름을 식당 리스트와 비교하는 반복문        
            for i2 in range(jsonCk):
                resName2 = allData[i2]['restaurant']
                resName1 = order[num]['restaurant']
                if resName1 in resName2:
                    psSum = allData[i2]['personnel'] + psSum
                    prSum = allData[i2]["price"] + prSum
                    borCnt = len(borList)

                    result = prSum / psSum
                    result = round(int(result), -2)
                    # print(resName1, psSum, prSum, result)
                    if borCnt == 0:
                        borList.append([resName1, result])
                    if borCnt != 0:
                        if resName1 == borList[numBor][0]:
                            borList[num] = [resName1, result]
                        elif resName1 != borList[0][0]:
                            borList.append([resName1, result])
                            numBor +=1
            num += 1
            if num >= odCnt:
                break
        
        for test in borList:
            print(test[0])
            print(test[1])

        chart_list = [
            {
                "restaurant": chartDate[0],
                "priceAvg": chartDate[1]
            }
            for chartDate in borList
        ]
        # resName = [
        #     {
        #         "restaurant": resData["restaurant"],
        #         "name_count": resData["name_count"]
        #     }
        #     for resData in test2
        # ]

        # test.append(chart_list)
        # print(test)
        # test.append(resName)
        # print(test)
        # print("chart_list", chart_list)
        # for tlqkf in chart_list:
        #     print("tlqkf", tlqkf)
        #     print(type(tlqkf))
        json_data = json.dumps(chart_list, cls=DjangoJSONEncoder, ensure_ascii=False)
        # print("json", type(json_data), json_data[1:6])
        # print("json2", json_data)
        # json_data = 

        # for name in yangcheon:
        #     # print(name)
        #     ycResName.append(name['restaurant'])
        # for name in dobong:
        #     # print(name)
        #     dbResName.append(name['restaurant'])

        # cntYcList = len(ycResName)
        # cntDbList = len(dbResName)

        # # print(resName)
        # # print(cntList)
        # # num = 0
        # numYC = 0
        # numYC1 = numYC
        # ycList = []
        # ycCnt = len(ycList)

        # if allData[0]["borough"] == check:
        #     while True:
        #         psSum = 0
        #         prSum = 0
        #         # db 안에 있는 식당 이름을 식당 리스트와 비교하는 반복문        
        #         for i2 in range(dbCnt):
        #             resName2 = allData[i2]['restaurant']
        #             resName1 = ycResName[numYC]
        #             if resName1 in resName2:
        #                 psSum = allData[i2]['personnel'] + psSum
        #                 prSum = allData[i2]["price"] + prSum
        #                 ycCnt = len(ycList)

        #                 result = prSum / psSum
        #                 result = round(int(result), -2)

        #                 if ycCnt == 0:
        #                     ycList.append([resName1, result])
        #                 if ycCnt != 0:
        #                     if resName1 == ycList[numYC1][0]:
        #                         ycList[numYC] = [resName1, result]
        #                     elif resName1 != ycList[0][0]:
        #                         ycList.append([resName1, result])
        #                         numYC1 +=1
        #         numYC += 1
        #         if numYC >= cntYcList:
        #             break
        # numDB1 = 0
        # numDB3 = numDB1
        # dobongList = []
        # dobongCnt = len(dobongList)

        # if allData[numDB]["borough"] == check:
        #         # print("도봉쓰")
        #         while True:
        #             psSum = 0
        #             prSum = 0
        #             # db 안에 있는 식당 이름을 식당 리스트와 비교하는 반복문        
        #             for i2 in range(dbCnt):
        #                 resName2 = allData[i2]['restaurant']
        #                 resName1 = dbResName[numDB1]
        #                 if resName1 in resName2:
        #                     psSum = allData[i2]['personnel'] + psSum
        #                     prSum = allData[i2]["price"] + prSum
        #                     dobongCnt = len(dobongList)

        #                     result = prSum / psSum
        #                     result = round(int(result), -2)
        #                     if dobongCnt == 0:
        #                         dobongList.append([resName1, result])
        #                     if dobongCnt != 0:
        #                         if resName1 == dobongList[numDB3][0]:
        #                             dobongList[numDB1] = [resName1, result]
        #                         elif resName1 != dobongList[0][0]:
        #                             dobongList.append([resName1, result])
        #                             numDB3 +=1
        #             numDB1 += 1
        #             if numDB1 >= cntDbList:
        #                 break
                

        # # print(ycList)
        # # print(dobongList)

        # # i = 0
        # topYcList = []
        # prYcList = []
        # for pr in ycList:
        #     prYcList.append(pr[1])
            
        # # print(prList)
        # prList1 = prYcList[:]
        # prList1.reverse()

        # for go in range(5):
        #     tmp = prList1.pop()
        #     for top in range(len(ycList)):
        #         if tmp == ycList[top][1]:
        #             topYcList.append(ycList[top])
        # topDbList = []
        # prDbList = []
        # for pr in dobongList:
        #     prDbList.append(pr[1])
            
        # # print(prList)
        # prList2 = prDbList[:]
        # prList2.reverse()

        # for go in range(5):
        #     tmp = prList2.pop()
        #     for top in range(len(dobongList)):
        #         if tmp == dobongList[top][1]:
        #             topDbList.append(dobongList[top])


        # chartDash = {
        #     "json_data": json_data,
        # }

        return HttpResponse(json_data, content_type ="application/json")

def dashboard(request):
 

    return render(request, "dashboard/chart.html")