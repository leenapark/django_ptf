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

import os
import django

# 1. 장소명을 list에 넣고 list 값을 비교?
@csrf_exempt
@api_view(['POST', 'GET'])
# Create your views here.
def post_api(request):

    if request.method == "POST":
        check = request.POST.get("borough")
        allData = TopData.objects.filter(borough=check).values()

        for i in allData:
            print(check, i)
            print(i["restaurant"])
            print(i)
        
        chart_list = [
            {
                "restaurant": chartDate["restaurant"],
                "priceAvg": chartDate["result"]
            }
            for chartDate in allData
        ]
        print(chart_list)

        json_data = json.dumps(chart_list, cls=DjangoJSONEncoder, ensure_ascii=False)

        return HttpResponse(json_data, content_type ="application/json")

def dashboard(request):


    # 일반 파이썬앱(스크립트)에서 django ORM을 사용하려면 다음의 설정 필요
    # django 환경설정 파일 지정
    # os.environ.setdefault("DJANGO_SETTINGS_MODULE", "doit_django_prj.settings")
    # # django settings 메모리 로딩 적용
    # django.setup()

    # from .models import TopData

    # dobongAll = DashData.objects.filter(borough="dobong").values()
    # dobongCnt = dobongAll.count()
    # dongdaemunAll = DashData.objects.filter(borough="dongdaemun").values()
    # dongdaemunCnt = dongdaemunAll.count()
    # dongjakAll = DashData.objects.filter(borough="dongjak").values()
    # dongjakCnt = dongjakAll.count()
    # eunpyeongAll = DashData.objects.filter(borough="eunpyeong").values()
    # eunpyeongCnt = eunpyeongAll.count()
    # gangdongAll = DashData.objects.filter(borough="gangdong").values()
    # gangdongCnt = gangdongAll.count()
    # gangnamAll = DashData.objects.filter(borough="gangnam").values()
    # gangnamCnt = gangnamAll.count()
    # gangseoAll = DashData.objects.filter(borough="gangseo").values()
    # gangseoCnt = gangseoAll.count()
    # geumcheonAll = DashData.objects.filter(borough="geumcheon").values()
    # geumcheonCnt = geumcheonAll.count()
    # guroAll = DashData.objects.filter(borough="guro").values()
    # guroCnt = guroAll.count()
    # gwanakAll = DashData.objects.filter(borough="gwanak").values()
    # gwanakCnt = gwanakAll.count()
    # gwangjinAll = DashData.objects.filter(borough="gwangjin").values()
    # gwangjinCnt = gwangjinAll.count()
    # jongroAll = DashData.objects.filter(borough="jongro").values()
    # jongroCnt = jongroAll.count()
    # jungAll = DashData.objects.filter(borough="jung").values()
    # jungCnt = jungAll.count()
    # jungnangAll = DashData.objects.filter(borough="jungnang").values()
    # jungnangCnt = jungnangAll.count()
    # mapoAll = DashData.objects.filter(borough="mapo").values()
    # mapoCnt = mapoAll.count()
    # nowonAll = DashData.objects.filter(borough="nowon").values()
    # nowonCnt = nowonAll.count()
    # seochoAll = DashData.objects.filter(borough="seocho").values()
    # seochoCnt = seochoAll.count()
    # seongbukAll = DashData.objects.filter(borough="seongbuk").values()
    # seongbukCnt = seongbukAll.count()
    # seongdongAll = DashData.objects.filter(borough="seongdong").values()
    # seongdongCnt = seongdongAll.count()
    # songpaAll = DashData.objects.filter(borough="songpa").values()
    # songpaCnt = songpaAll.count()
    # yangcheonAll = DashData.objects.filter(borough="yangcheon").values()
    # yangcheonCnt = yangcheonAll.count()
    # yeongdeungpoAll = DashData.objects.filter(borough="yeongdeungpo").values()
    # yeongdeungpoCnt = yeongdeungpoAll.count()
    # yongsanAll = DashData.objects.filter(borough="yongsan").values()
    # yongsanCnt = yongsanAll.count()


    # dbborData = dobongAll.values("restaurant").annotate(name_count=Count("restaurant")).filter(name_count__gt=1)
    # order = dbborData.order_by('-name_count')[:5]
    # print(order)
    # odCnt = order.count()
    # # borList = []
    # # borCnt = len(borList)
    # num = 0
    # # numBor = num
    # while True:
    #     # print(boroughData)
    #     psSum = 0
    #     prSum = 0
    #     # db 안에 있는 식당 이름을 식당 리스트와 비교하는 반복문        
    #     for i2 in range(dobongCnt):
    #         resName2 = dobongAll[i2]['restaurant']
    #         resName1 = order[num]['restaurant']
    #         if resName1 in resName2:
    #             psSum = dobongAll[i2]['personnel'] + psSum
    #             prSum = dobongAll[i2]["price"] + prSum
    #             # borCnt = len(borList)

    #             result = prSum / psSum
    #             result = round(int(result), -2)

    #             TopData.objects.update_or_create(
    #                 borough = dobongAll[i2]["borough"],
    #                 restaurant = resName1,

    #                 defaults={
    #                     "restaurant":resName1,
    #                     "result": result,
    #                     "borough": dobongAll[i2]["borough"]
    #                 }
    #             )
    #             # if borCnt == 0:
    #             #     borList.append([resName1, result, dobongAll[i2]["borough"]])
    #             # if borCnt != 0:
    #             #     if resName1 == borList[numBor][0]:
    #             #         borList[num] = [resName1, result, dobongAll[i2]["borough"]]
    #             #     elif resName1 != borList[0][0]:
    #             #         borList.append([resName1, result, dobongAll[i2]["borough"]])
    #             #         numBor +=1
    #     num += 1
    #     if num >= odCnt:
    #         break


        

    return render(request, "dashboard/chart.html")

