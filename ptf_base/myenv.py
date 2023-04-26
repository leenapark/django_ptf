SECRET_KEY = 'django-insecure-7x^8$j3ns^cdk#8q&m=jbr-@hcsc_@n_a9g&5la1008*4b#tpp'

DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'ptf_dashboard_db',
        'USER': 'admin',
        'PASSWORD' : 'django20230414',
        'HOST' : 'django-pjt-db.ceogn7iklwh9.ap-northeast-2.rds.amazonaws.com',
        'PORT' : '3306',
        'OPTIONS':{
            'init_command' : "SET sql_mode='STRICT_TRANS_TABLES'"
        }
    }
}