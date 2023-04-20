import os
import django
import csv
import sys

sumPrice = 0

# 일반 파이썬앱(스크립트)에서 django ORM을 사용하려면 다음의 설정 필요
# django 환경설정 파일 지정
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ptf_base.settings")
# django settings 메모리 로딩 적용
django.setup()

# data를 ORM으로 uploading 하기 위해 import
from dashboard.models import DashData

CSV_PATH='./dashboard/data/yangcheon/yangcheon.csv'

with open(CSV_PATH, "r", encoding="UTF-8") as file:
  dataRows = csv.reader(file, skipinitialspace=True)
  # print(list(dataRows))

  dataRows = filter(None, list(dataRows))
  # print(dataRows)

  for dbData in dataRows:
      if dbData[2].isdigit() == True:
      #   dbData[1].replace("（주）", "").replace(" （주）", "").replace("(주)", "")
      #   if "）" not in dbData[1]:
            # dbData[1] = dbData[1].replace("-", "")
            # print(dbData)
            #     dbData[0] = int(dbData[0])
            #     print(type(dbData[0]))
            #     if dbData[3].isinstance(int, ):
          
            dbData[3] = dbData[3].replace(",", "")
            dbData[3] = int(dbData[3])

            if dbData[1] != None and dbData[1] != "":
               regDate = dbData[0]
               restaurant = dbData[1]
               personnel = dbData[2]
               price = dbData[3]
               borough = "yangcheon"

               DashData.objects.create(
                  regDate = regDate,
                  restaurant = restaurant,
                  personnel = personnel,
                  price = price,
                  borough = borough
               )
                
                # if dbData[1] == dbData[1]:
                #   sumPrice = sumPrice + dbData[3]

                # DashData.objects.update_or_create(
                #     restaurant = dbData[1],

                #     defaults={
                #       "regDate": dbData[0],
                #       "restaurant": dbData[1],
                #       "personnel": dbData[2],
                #       "price": sumPrice,
                #       "borough": "yangcheon"
                #     }
                # )
