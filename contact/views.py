from django.shortcuts import render


""" ESTÁ FUNÇÃO ESTÁ RENDERINADO O INDEX.HMTL """
def index(request):
     return render(
          request,
          'contact/index.html'
     )