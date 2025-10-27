import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

''' 

코드를 뒤에서부터 한 단계씩 뜯어보면 이렇습니다.

__file__ : "이 코드를 담고 있는 파일이 뭐야?"

결과: .../Portfolio-BrotherKorea/config/settings.py (즉, settings.py 파일 자체의 경로)

Path(__file__).resolve() : "settings.py 파일의 '전체 주소'를 정확하게 알려줘." (컴퓨터의 루트부터 시작하는 전체 경로)

결과 (객체): Path('/Users/.../Portfolio-BrotherKorea/config/settings.py')

.parent (첫 번째 부모) : "settings.py 파일을 감싸고 있는 바로 위 폴더가 뭐야?"

결과 (객체): Path('/Users/.../Portfolio-BrotherKorea/config/')

.parent (두 번째 부모) : "config 폴더를 감싸고 있는 바로 위 폴더가 뭐야?"

결과 (객체): Path('/Users/.../Portfolio-BrotherKorea/')

결론: BASE_DIR라는 변수에는 manage.py가 있는 프로젝트의 최상위 폴더 경로(.../Portfolio-BrotherKorea/)가 저장됩니다.

'''

SECRET_KEY = 'django-insecure-os@iweu1zu2w#5c+w+*+8wt&o0rl1^h8sj=t+pr8409b=!6hui'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition
INSTALLED_APPS = [
    'main',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'config.wsgi.application'


# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
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
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# 1. 웹 URL에서 static 파일을 참조할 때 사용할 기본 경로
STATIC_URL = '/static/'

# 2. ⭐️ 개발 환경에서 Django가 static 파일을 찾을 추가 경로
# 1단계에서 만든 'static' 폴더를 여기에 등록
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

# 3. ⭐️ 배포(collectstatic) 시 static 파일이 수집될 경로
# 'staticfiles'라는 이름으로 루트 폴더에 생성되도록 설정
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
