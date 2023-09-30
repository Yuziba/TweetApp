from django.shortcuts import render,redirect
from . import models
from django.urls import reverse, reverse_lazy
from . import forms
from django.contrib.auth.decorators import login_required #--kullanici giris yapti mi bakar
from django.contrib.auth.forms import UserCreationForm      #-- Kullanici olusturma (sing up)
from django.views.generic import CreateView                 #-- Kullanici olusturma (sing up)

# Create your views here.
def listtweet(request):
    all_tweets = models.Tweet.objects.all()
    tweet_dict = {"tweets": all_tweets}
    return render(request, 'tweetapp/listtweet.html', context=tweet_dict)

@login_required(login_url="/login") #giris yapmayan addtweet kismini goremeyecek
def addtweet(request):
    # birinci veri alma yontemi
    """print(request.POST)  """   # formda gonderilen bilgiyi almak icin (terminalde gosterir)

    # ikinci veri alma cesidi
    """
    if request.POST:
        #print(request.POST["nickname"])    #terminalde yazdirdik
        #print(request.POST["message"])
    """

    # ucuncu yol
    if request.POST:
        nickname = request.POST["nickname"]
        message = request.POST["message"]
        #yol_1 DATABASE'e kaydetme
        """
        tweet = models.Tweet(nickname, message)
        tweet.save()
        """

        #yol_2 DATABASE'e kaydetme
        models.Tweet.objects.create(nickname=nickname, message=message)
        return redirect(reverse('tweetapp:listtweet'))  #database'e kayit yapildiktan sonra listeme ekranina yonlendirme yaptik
        #ama ust kisma alttaki import islemlerini yazdik
        #from django.shortcuts import render,redirect
        #from django.urls import reverse
    else:
        return render(request, 'tweetapp/addtweet.html')
    
def addtweetbyform(request):
    if request.method == "POST":
        #print (request.POST)
        """nickname = request.POST["nickname_input"]
        message = request.POST["message_input"]
        models.Tweet.objects.create(nickname=nickname, message=message)"""

        #baska bir yol
        form = forms.AddTweetForm(request.POST)
        if form.is_valid():
            nickname = form.cleaned_data["nickname_input"]
            message = form.cleaned_data["message_input"]
            models.Tweet.objects.create(nickname=nickname, message=message)
        return redirect(reverse('tweetapp:listtweet'))
    else:
        form = forms.AddTweetForm() #formumu olusturduk
        return render (request,'tweetapp/addtweetbyform.html', context={"form":form}) #contect ile ustte olustutrlan formu dict formatinda ilettik



def addtweetbymodelform(request):
    if request.method == "POST":
        form = forms.AddTweetModelForm(request.POST)
        if form.is_valid():
            nickname = form.cleaned_data["nickname"]
            message = form.cleaned_data["message"]
            models.Tweet.objects.create(nickname=nickname, message=message)
            return redirect(reverse('tweetapp:listtweet'))
        else:
            print("Error in model form")
            return render (request,'tweetapp/addtweetbymodelform.html', context={"form":form}) 
    else:
        form = forms.AddTweetModelForm() #formumu olusturduk
        return render (request,'tweetapp/addtweetbymodelform.html', context={"form":form}) 





class SignUpView(CreateView):   #-- Yukarida import ettigimiz createview den inherit eder
    form_class = UserCreationForm   # bu satiri tam olarak bu sekilde yazmamiz gerek. tanimli cunku. usercreatinonfrom dan import ederiz
    # success_url = reverse("login")  bununlada yapsak olurdu ama uygulama her baslatildiginda bu reverse calisacak ve 
    # sistemi yoracak. lazy ile sadece bu kayit ekrani acilirsa calisacak
    success_url = reverse_lazy("login")  # UserCreationForm'dan basarili olursa hangi url ye gidecegini belirtmek icin
    template_name = "registration/signup.html"  # hangi template ye bagli olacak 


