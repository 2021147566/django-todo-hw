from django.shortcuts import render, redirect
from .models import UserModel
from django.http import HttpResponse

# Create your views here.
# user/views.py


def sign_up_view(request):
    if request.method == 'GET':  # GET 메서드로 요청이 들어 올 경우
        return render(request, 'user/signup.html')
    elif request.method == 'POST':  # POST 메서드로 요청이 들어 올 경우
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        password2 = request.POST.get('password2', None)
        email = request.POST.get('email', None)

        if password != password2:
            return render(request, 'user/signup.html')
        else:
            exist_user = UserModel.objects.filter(username=username)
            if exist_user:
                return render(request, 'user/signup.html')
            else:
                new_user = UserModel()
                new_user.username = username
                new_user.password = password
                new_user.email = email
                new_user.save()
                return redirect('/sign-in')
# user/views.py

# user/views.py


def sign_in_view(request):
    if request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)

        try:
            me = UserModel.objects.get(username=username)
        except UserModel.DoesNotExist:
            return render(request, 'user/signin.html')


        if me.password == password:  # 저장된 사용자의 패스워드와 입력받은 패스워드 비교
            request.session['user'] = me.username  # 세션에 사용자 이름 저장
            return HttpResponse("로그인 성공!")
        else:  # 로그인이 실패하면 다시 로그인 페이지를 보여주기
            return redirect('/sign-in')

    elif request.method == 'GET':
        return render(request, 'user/signin.html')
