from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def Index(request):
    return HttpResponse("<table width='1500' height='500' style='background-color:green;font-size:80px' border='1'> <thead> <tr><td> İsim</td><td>  SoyIsim</td> <td> Sehir </td> </tr> </thead> <tbody> <tr> <td> Şeyma </td> <td>Yazan </td> <td> İstanbul </td>  </tr> <tr> <td>Mehmet </td> <td> Ceviz </td><td> KahramanMaraş </td></tr><tr><td> Mehmet </td> <td> Taşar</td> <td>GaziAntep</td> </tr></tbody> </table>")


def UserForm(request):
    return HttpResponse("<form> <div>  <input width='150' type='text' placeholder='Lutfen isminizi giriniz' /> </div> <div> <input type='text' width='150' placeholder='Lutfen soyadınızı giriniz' /> </div> <button> Kaydol </button></form>")

# Fonksiyonumuzu düzgün yazmamıza ragmen su anda bunu cagıramayız


# Alt tarafta onclick olarak yazdıgımız taraf JavaScript koduyken  geride kalanlar HTML kodudur...

def ButtonIndex(request):
    return HttpResponse("<button style='background-color:red' onclick=\"alert('Hello World!!!')\"> Tıkla!!! </button>")


# todo:img resim entegrasyonu

def ImageIndex(request):
    return HttpResponse("<img src='uzayGemisi.png'> </img>")
