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
        check = request.POST.get("borough")
        allData = DashData.objects.filter(borough=check).values()
        jsonCk = allData.count()
        boroughData = DashData.objects.filter(borough=check).values("restaurant").annotate(name_count=Count('restaurant')).filter(name_count__gt=1)
        order = boroughData.order_by('-name_count')[:5]
        odCnt = order.count()
        borList = []
        borCnt = len(borList)
        num = 0
        numBor = num
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
        chart_list = [
            {
                "restaurant": chartDate[0],
                "priceAvg": chartDate[1]
            }
            for chartDate in borList
        ]

        json_data = json.dumps(chart_list, cls=DjangoJSONEncoder, ensure_ascii=False)

        return HttpResponse(json_data, content_type ="application/json")

def dashboard(request):
 
    return render(request, "dashboard/chart.html")

