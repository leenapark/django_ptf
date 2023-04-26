from django.shortcuts import render
from .models import *
import json
from django.http import HttpResponse
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

        # for i in allData:
        #     print(check, i)
        #     print(i["restaurant"])
        #     print(i)
        
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

    return render(request, "dashboard/chart.html")

