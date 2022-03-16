from django.views import View
from django.shortcuts import render
from . import forms


class LoginView(View):
    # 페이지에 접근했을 때
    def get(self, request):
        form = forms.LoginForm(
            initial={
                "email": "itn@las.com",
            }
        )
        return render(
            request,
            "users/login.html",
            {
                "form": form,
            },
        )

    # Login 요청했을 때
    # clean - dict형태로 정리해 줌 - clean_email 등의 함수의 return 값으로
    def post(self, request):
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
        return render(
            request,
            "users/login.html",
            {
                "form": form,
            },
        )
