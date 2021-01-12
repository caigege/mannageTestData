"""
Django settings for mannageTestData project.

Generated by 'django-admin startproject' using Django 3.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""
import pymysql
from pathlib import Path
import os
#配置静态资源
STATIC_URL='/static'
ROOT_PATH = 'F:\\mannageTestData'
STATICFILES_DIRS = (os.path.join(ROOT_PATH,'static'),)

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
pymysql.version_info = (1, 4, 13, "final", 0)
pymysql.install_as_MySQLdb()

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'i3(d&5q)4#t2w30e2rz994$t6gho%6!*sef(=4z&e#6dk319ag'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'login',
    'model.apps.ModelConfig',
    'L1_Task_create',
    'company',
    'employee',
    'business'


]
MIDDLEWARE_CLASSES = (
   'django.contrib.sessions.middleware.SessionMiddleware',
   'django.middleware.common.CommonMiddleware',
   'django.middleware.csrf.CsrfViewMiddleware',
   'django.contrib.auth.middleware.AuthenticationMiddleware',
   'django.contrib.messages.middleware.MessageMiddleware',
   'django.middleware.clickjacking.XFrameOptionsMiddleware',
)



MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mannageTestData.urls'
os.path.join(BASE_DIR, 'templates')
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],

        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'mannageTestData.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': BASE_DIR / 'db.sqlite3',
        'ENGINE': 'django.db.backends.mysql',  # 数据库引擎
        'NAME': 'manager', #数据库名称
        'USER':'root', # 连接数据库的用户名称
        'PASSWORD':'123',  # 用户密码
        'HOST':'localhost', # 访问的数据库的主机的ip地址
        'PORT':'3306'# 默认mysql访问端口
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False
SILENCED_SYSTEM_CHECKS = ['fields.E300', 'fields.E307']


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
#---------------------步骤---------------------
'''
1.创建Django 项目
1.1 启动 python manage.py runserver
2.创造页面套餐包 python manage.py startapp xxxxx
3.Setting 配置
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'xxxxx'
]
4.view 
4.1.页面请求
def index(request):
    return HttpResponse("Hello, world!")

5.配置urls
from  xxxxx import views
   urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.index2),
] 
6.记得配置设置文件中的 TIME_ZONE 为自己所在地的时区，中国地区为 Asia/Shanghai。

7.model 数据库创建
 class Book(models.Model):
    name = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    pub_house = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    
    python manage.py sqlmigrate xxxxx 0001
  命令 1.  python manage.py makemigrations xxxxx   
       2.  python manage.py sqlmigrate model 0001
       3.  python manage.py migrate /
           python    manage.py   makemigrations
           
        A.   　直接在命令行执行命令 ： python    manage.py   makemigrations    或     python    manage.py   makemigrations   app_name

　　　　注.　　可以指定你的项目中的app的名字；也可以不指定，直接映射该项目中全部的app中的表模型

8.python manage.py shell

'''



#----------------------命名--------------------------
#
# python manage.py startapp login  创建页面


