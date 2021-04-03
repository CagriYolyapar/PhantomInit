# url pathlerini belirlememizi saglayan kodları barındıran kütüphanemizi entegre etmeliyiz. Yoksa ilgili pathler belirlenemez
from django.urls import path

# bu projedeki sayfayı görebilmek istiyorsak bu katmana uygun url'leri burada belirlememiz gerekiyor...
from . import views
# views dosyasındaki her modülü al (. sembolünün görevi)

urlpatterns = [

    # eger bize bir istek gelirse onu yonlendirme kodları..Path argümanına bos string ifade vermeniz otomatik olarak buraya bir istek gelirse demektir.
    path('', views.UserForm, name="Index")

]
