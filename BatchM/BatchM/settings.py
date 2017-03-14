"""
Django settings for BatchM project.

Generated by 'django-admin startproject' using Django 1.10.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'v0tses5dvxmo)&0%)0r%p3%9*+a2pf$^5nwvo9-9t#90@7fl68'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'Batch',
]

MIDDLEWARE = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'BatchM.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
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

WSGI_APPLICATION = 'BatchM.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# 定义一个缓存,用来存放键值对
CACHES = {
    'default':{
        'BACKEND':'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'unique-snowflake',
        'TIMEOUT': 3600,
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Shanghai'


USE_I18N = True

USE_L10N = True

USE_TZ = False


AUTH_USER_MODEL = 'Batch.MyUser'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR,'statics'),
)


# these infos were define by myself

#定义发送邮件到服务器
sender_host='localhost'

# 定义工单邮件收件人
recipients='team_cloud_service@syberos.com'
#recipients='liaojiafa@syberos.com'

# 工单邮件中URL的host，通过apache或者nginx来下载附件。
#HOST='192.168.93.133'
HOST='172.16.22.104'
# 工单邮件中附件下载URL端口
APACHE_PORT=8080
# 工单附件上传的目录
accessory_dir = "upload/order_accessory"
# 管理docker容器时到并发进程数
pools=20
# docker api 的版本号，设置auto的话，能够自适应版本，版本选择可参考：https://docs.docker.com/engine/reference/api/docker_remote_api/
DockerVersion='auto'

# 设置salt-api的主机IP
SaltApiOfHost='172.16.22.129'
#SaltApiOfHost='192.168.141.129'
# 设置登录salt-api的用户名
SaltApiUsername='saltapi'
# 设置登录salt-api的密码
SaltApiPasswd='123456'
# 设置登录salt-api的认证方式
SaltApiAuthMethod='pam'
# 设置saltstack的组配置文件路径
SaltGroupConfigFile="/etc/salt/master.d/group.conf"
# 设置启动novnc的命令位置
novnc_cmd_path='/root/devops/noVNC/utils/launch.sh'
# 设置NOVNC监听的起始端口
novnc_begin_port = 6080
novnc_end_port = 6100

# 设置 启动NOvnc脚本输出内容存放的目录
novnc_outputcontent_path = '/tmp/NoVnc'