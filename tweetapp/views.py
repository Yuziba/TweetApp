from django.shortcuts import render,redirect
from . import models
from django.urls import reverse
from . import forms



# Create your views here.
def listtweet(request):
    all_tweets = models.Tweet.objects.all()
    tweet_dict = {"tweets": all_tweets}
    return render(request, 'tweetapp/listtweet.html', context=tweet_dict)

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



