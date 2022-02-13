from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
# Create your views here.
from .models import User, Game, Comment, Watchlist, Like, Image

def login_view(request):
    if request.method == "POST":

        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)


        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "GRY_APP/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "GRY_APP/login.html")

@login_required
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "GRY_APP/register.html", {
                "message": "Passwords must match."
            })

        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "GRY_APP/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "GRY_APP/register.html")

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "GRY_APP/register.html", {
                "message": "Passwords must match."
            })

        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "GRY_APP/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "GRY_APP/register.html")
 

def game_page(request, game_id):
    user = User.objects.get(username=request.user)
    game = Game.objects.get(id=game_id)
    gamess = Watchlist.objects.filter(user=request.user)
    likes = Like.objects.filter(liked_game=game)
    images = Image.objects.filter(game=game)
    if request.method == "POST":
        check = Watchlist.objects.filter(user=request.user, game=game)
        liked = Like.objects.filter(liker=request.user, liked_game=game)
        if request.POST.get("like") == 'Like':
            Like.objects.create(liker=request.user, liked_game=game)
            return HttpResponseRedirect(reverse('game_page', args=(game.id,)))
        if request.POST.get("unlike") == 'Unlike':
            Like.objects.filter(liker=request.user, liked_game=game).delete()
            return HttpResponseRedirect(reverse('game_page', args=(game.id,)))
        if request.POST.get("add") == 'Add':
            Watchlist.objects.create(user=request.user, game=game)
            return HttpResponseRedirect(reverse('watchlist'))
        if request.POST.get("delete") == 'Delete':
            Watchlist.objects.filter(user=request.user, game=game).delete()
            return HttpResponseRedirect(reverse('watchlist'))
        if request.POST.get("again") == 'Again':
            again = Game.objects.filter(genre=game.genre, system=game.system).order_by("?").first()
            return HttpResponseRedirect(reverse('game_page', args=(again.id,)))
        content = request.POST["comment"]
        comment = Comment(content=content)
        comment.user = user
        comment.save()
        game.comment.add(comment)
        game.save()
        return HttpResponseRedirect(reverse('game_page', args=(game.id,)))
    else:
        check = Watchlist.objects.filter(user=request.user, game=game)
        liked = Like.objects.filter(liker=request.user, liked_game=game)
        return render(request, "GRY_APP/game.html", {
            "game":game ,
            "check":check,
            "likes":likes.count(),
            "liked":liked,
            "images":images
        })

@login_required
def watchlist(request):
    gamess = Watchlist.objects.filter(user=request.user)

    return render(request, "GRY_APP/watchlist.html", {
            "gamess": gamess
        })


def index(request):
    if request.method == "POST" and request.user.is_authenticated:
        genre = request.POST["genre"]
        system = request.POST["system"]
        if genre == "action" and system == "multiplatform":
            game = Game.objects.filter(genre='Action', system='Multiplatform').order_by("?").first()
            return HttpResponseRedirect(reverse('game_page', args=(game.id,)))
        if genre == "action" and system == "playstation":
            game = Game.objects.filter(genre='Action', system='Playstation').order_by("?").first()
            return HttpResponseRedirect(reverse('game_page', args=(game.id,)))
        if genre == "action" and system == "xbox":
            game = Game.objects.filter(genre='Action', system='Xbox').order_by("?").first()
            return HttpResponseRedirect(reverse('game_page', args=(game.id,)))
        if genre == "adventure" and system == "multiplatform":
            game = Game.objects.filter(genre='Adventure', system='Multiplatform').order_by("?").first()
            return HttpResponseRedirect(reverse('game_page', args=(game.id,)))
        if genre == "adventure" and system == "xbox":
            game = Game.objects.filter(genre='Adventure', system='Xbox').order_by("?").first()
            return HttpResponseRedirect(reverse('game_page', args=(game.id,)))
        if genre == "adventure" and system == "playstation":
            game = Game.objects.filter(genre='Adventure', system='Playstation').order_by("?").first()
            return HttpResponseRedirect(reverse('game_page', args=(game.id,)))
        if genre == "fightinggames" and system == "multiplatform":
            game = Game.objects.filter(genre='Fighting Game', system='Multiplatform').order_by("?").first()
            return HttpResponseRedirect(reverse('game_page', args=(game.id,)))
        if genre == "fightinggames" and system == "xbox":
            game = Game.objects.filter(genre='Fighting Game', system='Xbox').order_by("?").first()
            return HttpResponseRedirect(reverse('game_page', args=(game.id,)))
        if genre == "fightinggames" and system == "playstation":
            game = Game.objects.filter(genre='Fighting Game', system='Playstation').order_by("?").first()
            return HttpResponseRedirect(reverse('game_page', args=(game.id,)))     
        if genre == "horror" and system == "multiplatform":
            game = Game.objects.filter(genre='Horror', system='Multiplatform').order_by("?").first()
            return HttpResponseRedirect(reverse('game_page', args=(game.id,)))      
        if genre == "horror" and system == "xbox":
            game = Game.objects.filter(genre='Horror', system='Xbox').order_by("?").first()
            return HttpResponseRedirect(reverse('game_page', args=(game.id,)))
        if genre == "horror" and system == "playstation":
            game = Game.objects.filter(genre='Horror', system='Playstation').order_by("?").first()
            return HttpResponseRedirect(reverse('game_page', args=(game.id,)))    
        if genre == "fps" and system == "multiplatform":
            game = Game.objects.filter(genre='First Person Shooter', system='Multiplatform').order_by("?").first()
            return HttpResponseRedirect(reverse('game_page', args=(game.id,)))      
        if genre == "fps" and system == "xbox":
            game = Game.objects.filter(genre='First Person Shooter', system='Xbox').order_by("?").first()
            return HttpResponseRedirect(reverse('game_page', args=(game.id,)))
        if genre == "fps" and system == "playstation":
            game = Game.objects.filter(genre='First Person Shooter', system='Playstation').order_by("?").first()
            return HttpResponseRedirect(reverse('game_page', args=(game.id,)))   
        if genre == "rpg" and system == "multiplatform":
            game = Game.objects.filter(genre='Role Playing Game', system='Multiplatform').order_by("?").first()
            return HttpResponseRedirect(reverse('game_page', args=(game.id,)))
        if genre == "rpg" and system == "xbox":
            game = Game.objects.filter(genre='Role Playing Game', system='Multiplatform').order_by("?").first()
            return HttpResponseRedirect(reverse('game_page', args=(game.id,)))
        if genre == "rpg" and system == "playstation":
            game = Game.objects.filter(genre='Role Playing Game', system='Playstation').order_by("?").first()
            return HttpResponseRedirect(reverse('game_page', args=(game.id,)))       
        if genre == "tps" and system == "multiplatform":
            game = Game.objects.filter(genre='Third Person Shooter', system='Multiplatform').order_by("?").first()
            return HttpResponseRedirect(reverse('game_page', args=(game.id,)))
        if genre == "tps" and system == "xbox":
            game = Game.objects.filter(genre='Third Person Shooter', system='Xbox').order_by("?").first()
            return HttpResponseRedirect(reverse('game_page', args=(game.id,)))     
        if genre == "tps" and system == "playstation":
            game = Game.objects.filter(genre='Third Person Shooter', system='Playstation').order_by("?").first()
            return HttpResponseRedirect(reverse('game_page', args=(game.id,)))            
    elif request.method == "GET" and request.user.is_authenticated:    
        return render(request, "GRY_APP/index.html")
    else:
        return HttpResponseRedirect(reverse("login"))
