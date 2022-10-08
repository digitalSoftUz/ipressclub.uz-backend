from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

def Loginpage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.filter(username=username)
        if user.count() > 0:
            usr = authenticate(username=username, password=password)
            if usr is not None:
                login(request, usr)
                return redirect('home')
            else:
                messages.error(request, 'Login yoki parol xato!')
                return redirect('login')
            return redirect('login')
        else:
            messages.error(request, 'Bunday foydalanuvchi mavjud emas!')
            return redirect('login')
    return render(request, 'pages-sign-in.html')


def LogoutView(request):
    logout(request)
    return redirect("login")

@login_required(login_url='login')
def Home(request):
    context = {
        "news_count": News.objects.all().count(),
        "projects_count": Projects.objects.all().count(),
        "partner_count": Partners.objects.all().count(),
        "council_count": Team.objects.all().count(),
        "trip_count": Team.objects.all().count(),
    }
    return render(request, 'home.html', context)


@login_required(login_url='login')
def InformationView(request):
    context = {
        "information": Information.objects.all()
    }
    if request.method == "POST":
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        logo = request.FILES["logo"]
        instagram_link = request.POST.get("instagram_link")
        telegram_link = request.POST.get("telegram_link")
        fb_link = request.POST.get("fb_link")
        youtube_link = request.POST.get("youtube_link")
        address = request.POST.get("address")
        map = request.POST.get("map")
        info = request.POST.get("info")
        info_ru = request.POST.get("info_ru")
        info_uz = request.POST.get("info_uz")
        info_en = request.POST.get("info_en")
        Information.objects.create(
            phone=phone,
            email=email,
            logo=logo,
            instagram_link=instagram_link,
            telegram_link=telegram_link,
            fb_link=fb_link,
            youtube_link=youtube_link,
            address=address,
            map=map,
            info=info,
            info_ru=info_ru,
            info_uz=info_uz,
            info_en=info_en
        )
        return redirect("information")
    return render(request, "information.html", context)


@login_required(login_url='login')
def ProjectsView(request):
    context = {
        "category": CategoryProjects.objects.all(),
        "projects": Projects.objects.all()
    }
    return render(request, 'projects.html', context)


@login_required(login_url='login')
def ChangeInfo(request, pk):
    context = {
        "info": Information.objects.get(id=pk)
    }
    if request.method == "POST":
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        instagram_link = request.POST.get("instagram_link")
        telegram_link = request.POST.get("telegram_link")
        fb_link = request.POST.get("fb_link")
        youtube_link = request.POST.get("youtube_link")
        address = request.POST.get("address")
        map = request.POST.get("map")
        info = request.POST.get("info")
        info_uz = request.POST.get("info_uz")
        info_ru = request.POST.get("info_ru")
        info_en = request.POST.get("info_en")
        infor = Information.objects.get(id=pk)
        infor.phone = phone
        infor.email = email
        infor.instagram_link = instagram_link
        infor.telegram_link = telegram_link
        infor.fb_link = fb_link
        infor.youtube_link = youtube_link
        infor.address = address
        infor.map = map
        infor.info = info
        infor.info_uz = info_uz
        infor.info_ru = info_ru
        infor.info_en = info_en
        if len(request.FILES) > 0:
            infor.logo = request.FILES['logo']
        infor.save()
        return redirect("change-info", pk)
    return render(request, "change-information.html", context)


@login_required(login_url='login')
def NewsView(request):
    context = {
        "news": News.objects.all(),
        "category": Category.objects.all()
    }
    return render(request, "news.html", context)


@login_required(login_url='login')
def TripsView(request):
    context = {
        "trip": Trips.objects.all(),
        "region": Region.objects.all()
    }
    return render(request, "trips.html", context)


@login_required(login_url='login')
def SingleNews(request, pk):
    context = {
        "new": News.objects.get(id=pk),
    }
    return render(request, "single-new.html", context)


@login_required(login_url='login')
def SingleAbout(request, pk):
    context = {
        "about": AboutXPK.objects.get(id=pk),
    }
    return render(request, "single-about.html", context)


@login_required(login_url='login')
def SingleTrip(request, pk):
    context = {
        "trip": Trips.objects.get(id=pk),
    }
    return render(request, "single-trip.html", context)


@login_required(login_url='login')
def SingleProject(request, pk):
    context = {
        "project": Projects.objects.get(id=pk),
    }
    return render(request, "single-project.html", context)


@login_required(login_url='login')
def ChangeNews(request, pk):
    context = {
        "new": News.objects.get(id=pk),
        'category': Category.objects.all(),
    }
    if request.method == "POST":
        category = request.POST.get('category')
        name = request.POST.get('name')
        name_uz = request.POST.get('name_uz')
        name_ru = request.POST.get('name_ru')
        name_en = request.POST.get('name_en')
        mini_text = request.POST.get('mini_text')
        mini_text_uz = request.POST.get('mini_text_uz')
        mini_text_ru = request.POST.get('mini_text_ru')
        mini_text_en = request.POST.get('mini_text_en')
        text = request.POST.get('text')
        text_uz = request.POST.get('text_uz')
        text_ru = request.POST.get('text_ru')
        text_en = request.POST.get('text_en')
        new = News.objects.get(id=pk)
        if request.POST.get('date') != "":
            date = request.POST.get('date')
            new.date = date
        if request.FILES.get('img1') != None:
            img1 = request.FILES.get('img1')
            new.img1 = img1
        if request.FILES.get('img2') != None:
            img2 = request.FILES.get('img2')
            new.img2 = img2
        if request.POST.get('video_url') != None:
            video_url = request.FILES.get('video_url')
            new.video_url = video_url
        if request.FILES.get('video') != None:
            video = request.FILES.get('video')
            new.video = video
        new.category.id = category
        new.name = name
        new.name_uz = name_uz
        new.name_ru = name_ru
        new.name_en = name_en
        new.mini_text = mini_text
        new.mini_text_uz = mini_text_uz
        new.mini_text_ru = mini_text_ru
        new.mini_text_en = mini_text_en
        new.text = text
        new.text_uz = text_uz
        new.text_ru = text_ru
        new.text_en = text_en
        new.save()
        return redirect("change-new", pk)
    return render(request, "change-new.html", context)


@login_required(login_url='login')
def ChangeProject(request, pk):
    context = {
        "project": Projects.objects.get(id=pk),
        'category': CategoryProjects.objects.all(),
    }
    if request.method == "POST":
        category = request.POST.get('category')
        name = request.POST.get('name')
        name_uz = request.POST.get('name_uz')
        name_ru = request.POST.get('name_ru')
        name_en = request.POST.get('name_en')
        mini_text = request.POST.get('mini_text')
        mini_text_uz = request.POST.get('mini_text_uz')
        mini_text_ru = request.POST.get('mini_text_ru')
        mini_text_en = request.POST.get('mini_text_en')
        text = request.POST.get('text')
        text_uz = request.POST.get('text_uz')
        text_ru = request.POST.get('text_ru')
        text_en = request.POST.get('text_en')
        project = Projects.objects.get(id=pk)
        if request.POST.get('date') != "":
            date = request.POST.get('date')
            project.date = date
        if request.FILES.get('img1') != None:
            img1 = request.FILES.get('img1')
            project.img1 = img1
        if request.FILES.get('img2') != None:
            img2 = request.FILES.get('img2')
            project.img2 = img2
        if request.POST.get('video_url') != None:
            video_url = request.POST.get('video_url')
            project.video_url = video_url
        if request.FILES.get('video') != None:
            video = request.FILES.get('video')
            project.video = video
        project.category.id = category
        project.name = name
        project.name_uz = name_uz
        project.name_ru = name_ru
        project.name_en = name_en
        project.mini_text = mini_text
        project.mini_text_uz = mini_text_uz
        project.mini_text_ru = mini_text_ru
        project.mini_text_en = mini_text_en
        project.text = text
        project.text_uz = text_uz
        project.text_ru = text_ru
        project.text_en = text_en
        project.save()
        return redirect("change-project", pk)
    return render(request, "change-project.html", context)


@login_required(login_url='login')
def PartnerView(request):
    context = {
        "partner": Partners.objects.all()
    }
    return render(request, 'partner.html', context)


@login_required(login_url='login')
def TeamView(request):
    context = {
        "team": Team.objects.all()
    }
    return render(request, 'team.html', context)


@login_required(login_url='login')
def JamoaView(request):
    context = {
        "team": Jamoa.objects.all()
    }
    return render(request, 'jamoa.html', context)


@login_required(login_url='login')
def DeleteNews(request, pk):
    News.objects.get(id=pk).delete()
    return redirect("news")


@login_required(login_url='login')
def DeleteProject(request, pk):
    Projects.objects.get(id=pk).delete()
    return redirect("projects")


@login_required(login_url='login')
def DeleteAbout(request, pk):
    AboutXPK.objects.get(id=pk).delete()
    return redirect("about")


@login_required(login_url='login')
def DeleteInfo(request, pk):
    Information.objects.get(id=pk).delete()
    return redirect("information")


@login_required(login_url='login')
def DeleteTrip(request, pk):
    Trips.objects.get(id=pk).delete()
    return redirect("trips")


@login_required(login_url='login')
def DeleteLogo(request, pk):
    Partners.objects.get(id=pk).delete()
    return redirect("partner")


@login_required(login_url='login')
def AddLogo(request):
    if request.method == "POST":
        logo = request.FILES['logo']
        Partners.objects.create(logo=logo)
        return redirect("partner")


@login_required(login_url='login')
def ChangeLogo(request, pk):
    if request.method == "POST":
        logo = request.FILES['logo']
        p = Partners.objects.get(id=pk)
        p.logo = logo
        p.save()
    return redirect("partner")


@login_required(login_url='login')
def AddTeam(request):
    if request.method == "POST":
        img = request.FILES['img']
        fullname = request.POST.get('fullname')
        fullname_uz = request.POST.get('fullname_uz')
        fullname_ru = request.POST.get('fullname_ru')
        fullname_en = request.POST.get('fullname_en')
        position = request.POST.get('position')
        position_uz = request.POST.get('position_uz')
        position_ru = request.POST.get('position_ru')
        position_en = request.POST.get('position_en')
        Team.objects.create(img=img, fullname=fullname, fullname_uz=fullname_uz, fullname_ru=fullname_ru, fullname_en=fullname_en,
                            position=position, position_uz=position_uz, position_ru=position_ru, position_en=position_en)
    return redirect("team")

@login_required(login_url='login')
def AddJamoa(request):
    if request.method == "POST":
        img = request.FILES['img']
        fullname = request.POST.get('fullname')
        fullname_uz = request.POST.get('fullname_uz')
        fullname_ru = request.POST.get('fullname_ru')
        fullname_en = request.POST.get('fullname_en')
        position = request.POST.get('position')
        position_uz = request.POST.get('position_uz')
        position_ru = request.POST.get('position_ru')
        position_en = request.POST.get('position_en')
        Jamoa.objects.create(img=img, fullname=fullname, fullname_uz=fullname_uz, fullname_ru=fullname_ru, fullname_en=fullname_en,
                            position=position, position_uz=position_uz, position_ru=position_ru, position_en=position_en)
    return redirect("jamoa")


@login_required(login_url='login')
def AddNews(request):
    context = {
        "category": Category.objects.all()
    }
    if request.method == "POST":
        category = request.POST.get('category')
        name = request.POST.get('name')
        name_uz = request.POST.get('name_uz')
        name_ru = request.POST.get('name_ru')
        name_en = request.POST.get('name_en')
        mini_text = request.POST.get('mini_text')
        mini_text_uz = request.POST.get('mini_text_uz')
        mini_text_ru = request.POST.get('mini_text_ru')
        mini_text_en = request.POST.get('mini_text_en')
        text = request.POST.get('text')
        text_uz = request.POST.get('text_uz')
        text_ru = request.POST.get('text_ru')
        text_en = request.POST.get('text_en')
        date = request.POST.get('date')
        img1 = request.FILES.get('img1')
        img2 = request.FILES.get('img2')
        video = request.FILES.get('video')
        video_url = request.POST.get('video_url')
        News.objects.create(
            category_id=category,
            name=name,
            name_uz=name_uz,
            name_ru=name_ru,
            name_en=name_en,
            mini_text=mini_text,
            mini_text_uz=mini_text_uz,
            mini_text_ru=mini_text_ru,
            mini_text_en=mini_text_en,
            text=text,
            text_uz=text_uz,
            text_ru=text_ru,
            text_en=text_en,
            date=date,
            img1=img1,
            img2=img2,
            video=video,
            video_url=video_url
        )
        return redirect('add-new')
    return render(request, "add-new.html", context)


@login_required(login_url='login')
def AddProject(request):
    context = {
        "category": CategoryProjects.objects.all()
    }
    if request.method == "POST":
        category = request.POST.get('category')
        name = request.POST.get('name')
        name_uz = request.POST.get('name_uz')
        name_ru = request.POST.get('name_ru')
        name_en = request.POST.get('name_en')
        mini_text = request.POST.get('mini_text')
        mini_text_uz = request.POST.get('mini_text_uz')
        mini_text_ru = request.POST.get('mini_text_ru')
        mini_text_en = request.POST.get('mini_text_en')
        text = request.POST.get('text')
        text_uz = request.POST.get('text_uz')
        text_ru = request.POST.get('text_ru')
        text_en = request.POST.get('text_en')
        date = request.POST.get("date")
        img1 = request.FILES.get("img1")
        img2 = request.FILES.get("img2")
        video = request.FILES.get("video")
        video_url = request.POST.get("video_url")
        Projects.objects.create(
            category_id=category,
            name=name,
            name_uz=name_uz,
            name_ru=name_ru,
            name_en=name_en,
            mini_text=mini_text,
            mini_text_uz=mini_text_uz,
            mini_text_ru=mini_text_ru,
            mini_text_en=mini_text_en,
            text=text,
            text_uz=text_uz,
            text_ru=text_ru,
            text_en=text_en,
            date=date,
            img1=img1,
            img2=img2,
            video=video,
            video_url=video_url,
        )
        return redirect("add-project")
    return render(request, 'add-project.html', context)


@login_required(login_url='login')
def DeleteTeam(request, pk):
    Team.objects.get(id=pk).delete()
    return redirect("team")


@login_required(login_url='login')
def DeleteJamoa(request, pk):
    Jamoa.objects.get(id=pk).delete()
    return redirect("jamoa")


@login_required(login_url='login')
def ChangeTeam(request, pk):
    if request.method == "POST":
        fullname = request.POST.get('fullname')
        fullname_uz = request.POST.get('fullname_uz')
        fullname_ru = request.POST.get('fullname_ru')
        fullname_en = request.POST.get('fullname_en')
        position = request.POST.get('position')
        position_uz = request.POST.get('position_uz')
        position_ru = request.POST.get('position_ru')
        position_en = request.POST.get('position_en')
        t = Team.objects.get(id=pk)
        t.fullname = fullname
        t.fullname_uz = fullname_uz
        t.fullname_ru = fullname_ru
        t.fullname_en = fullname_en
        t.position = position
        t.position_uz = position_uz
        t.position_ru = position_ru
        t.position_en = position_en
        if len(request.FILES) > 0:
            img = request.FILES['img']
            t.img = img
        t.save()
        return redirect("team")


@login_required(login_url='login')
def ChangeJamoa(request, pk):
    if request.method == "POST":
        fullname = request.POST.get('fullname')
        fullname_uz = request.POST.get('fullname_uz')
        fullname_ru = request.POST.get('fullname_ru')
        fullname_en = request.POST.get('fullname_en')
        position = request.POST.get('position')
        position_uz = request.POST.get('position_uz')
        position_ru = request.POST.get('position_ru')
        position_en = request.POST.get('position_en')
        t = Jamoa.objects.get(id=pk)
        t.fullname = fullname
        t.fullname_uz = fullname_uz
        t.fullname_ru = fullname_ru
        t.fullname_en = fullname_en
        t.position = position
        t.position_uz = position_uz
        t.position_ru = position_ru
        t.position_en = position_en
        if len(request.FILES) > 0:
            img = request.FILES['img']
            t.img = img
        t.save()
        return redirect("jamoa")


@login_required(login_url='login')
def AddCategory(request):
    if request.method == "POST":
        name = request.POST.get("name")
        name_uz = request.POST.get("name_uz")
        name_ru = request.POST.get("name_ru")
        name_en = request.POST.get("name_en")
        Category.objects.create(name=name, name_uz=name_uz, name_ru=name_ru, name_en=name_en)
    return redirect("news")


@login_required(login_url='login')
def ChangeCategory(request, pk):
    if request.method == "POST":
        name = request.POST.get("name")
        name_ru = request.POST.get("name_ru")
        name_uz = request.POST.get("name_uz")
        name_en = request.POST.get("name_en")
        c = Category.objects.get(id=pk)
        c.name = name
        c.name_uz = name_uz
        c.name_ru = name_ru
        c.name_en = name_en
        c.save()
    return redirect("news")


@login_required(login_url='login')
def ChangeRegion(request, pk):
    if request.method == "POST":
        name = request.POST.get("name")
        name_uz = request.POST.get("name_uz")
        name_ru = request.POST.get("name_ru")
        name_en = request.POST.get("name_en")
        c = Region.objects.get(id=pk)
        c.name = name
        c.name_uz = name_uz
        c.name_ru = name_ru
        c.name_en = name_en
        c.save()
    return redirect("trips")


@login_required(login_url='login')
def ChangeCategoryProject(request, pk):
    if request.method == "POST":
        name = request.POST.get("name")
        name_uz = request.POST.get("name_uz")
        name_ru = request.POST.get("name_ru")
        name_en = request.POST.get("name_en")
        c = CategoryProjects.objects.get(id=pk)
        c.name = name
        c.name_uz = name_uz
        c.name_ru = name_ru
        c.name_en = name_en
        c.save()
    return redirect("projects")


@login_required(login_url='login')
def DeleteCategory(request, pk):
    Category.objects.get(id=pk).delete()
    return redirect("news")


@login_required(login_url='login')
def DeleteRegion(request, pk):
    Region.objects.get(id=pk).delete()
    return redirect("trips")


def AddRegion(request):
    if request.method == "POST":
        name = request.POST.get("name")
        name_uz = request.POST.get("name_uz")
        name_ru = request.POST.get("name_ru")
        name_en = request.POST.get("name_en")
        Region.objects.create(
            name=name,
            name_uz=name_uz,
            name_ru=name_ru,
            name_en=name_en,
        )
    return redirect('trips')

@login_required(login_url='login')
def DeleteCategoryProject(request, pk):
    CategoryProjects.objects.get(id=pk).delete()
    return redirect("projects")


@login_required(login_url='login')
def About(request):
    context = {
        "info": AboutXPK.objects.all()
    }
    return render(request, 'about.html', context)


@login_required(login_url='login')
def AddAbout(request):
    if request.method == "POST":
        name = request.POST.get("name")
        name_uz = request.POST.get("name_uz")
        name_ru = request.POST.get("name_ru")
        name_en = request.POST.get("name_en")
        text = request.POST.get("text")
        text_uz = request.POST.get("text_uz")
        text_ru = request.POST.get("text_ru")
        text_en = request.POST.get("text_en")
        img = request.FILES["img"]
        text1 = request.POST.get("text1")
        text1_uz = request.POST.get("text1_uz")
        text1_ru = request.POST.get("text1_ru")
        text1_en = request.POST.get("text1_en")
        AboutXPK.objects.create(
            name=name,
            name_uz=name_uz,
            name_ru=name_ru,
            name_en=name_en,
            text_uz=text_uz,
            text=text,
            text_ru=text_ru,
            text_en=text_en,
            img=img,
            text1=text1,
            text1_uz=text1_uz,
            text1_ru=text1_ru,
            text1_en=text1_en,
        )
    return redirect("about")


@login_required(login_url='login')
def ChangeAbout(request, pk):
    context = {
        "about": AboutXPK.objects.get(id=pk)
    }
    if request.method == "POST":
        name = request.POST.get("name")
        name_uz = request.POST.get("name_uz")
        name_ru = request.POST.get("name_ru")
        name_en = request.POST.get("name_en")
        text = request.POST.get("text")
        text_uz = request.POST.get("text_uz")
        text_ru = request.POST.get("text_ru")
        text_en = request.POST.get("text_en")
        text1 = request.POST.get("text1")
        text1_uz = request.POST.get("text1_uz")
        text1_ru = request.POST.get("text1_ru")
        text1_en = request.POST.get("text1_en")
        ab = AboutXPK.objects.get(id=pk)
        if len(request.FILES):
            img = request.FILES["img"]
            ab.img = img
        ab.name = name
        ab.name_uz = name_uz
        ab.name_ru = name_ru
        ab.name_en = name_en
        ab.text_uz = text_uz
        ab.text = text
        ab.text_ru = text_ru
        ab.text_en = text_en
        ab.text1_uz = text1_uz
        ab.text1 = text1
        ab.text1_ru = text1_ru
        ab.text1_en = text1_en
        ab.save()
        return redirect("change-about", pk)
    return render(request, "change-about.html", context)


@login_required(login_url='login')
def AddTrip(request):
    context = {
        "region": Region.objects.all()
    }
    if request.method == "POST":
        region = request.POST.get("region")
        name = request.POST.get("name")
        name_uz = request.POST.get("name_uz")
        name_ru = request.POST.get("name_ru")
        name_en = request.POST.get("name_en")
        video_or_link = request.POST.get("video_or_link")
        img = request.FILES['img']
        trip = Trips.objects.create(region_id=region, name_uz=name_uz, name=name, name_ru=name_ru, name_en=name_en, video_or_link=video_or_link, img=img)
        if video_or_link == '1':
            link = request.POST.get("link")
            trip.link = link
            trip.video_or_link = 1
            trip.save()
        if video_or_link == '2':
            video = request.FILES.get("video")
            trip.video = video
            trip.video_or_link = 2
            trip.save()
        return redirect("add-trip")
    return render(request, 'add-trip.html', context)


@login_required(login_url='login')
def ChangeTrip(request, pk):
    context = {
        "region": Region.objects.all(),
        "trip": Trips.objects.get(id=pk)
    }
    if request.method == "POST":
        region = request.POST.get("region")
        name = request.POST.get("name")
        name_uz = request.POST.get("name_uz")
        name_ru = request.POST.get("name_ru")
        name_en = request.POST.get("name_en")
        video_or_link = request.POST.get("video_or_link")
        trip = Trips.objects.get(id=pk)
        trip.region.id = region
        trip.name = name
        trip.name_uz = name_uz
        trip.name_ru = name_ru
        trip.name_en = name_en
        img = request.FILES.get("img")
        if img is not None:
            trip.img = img
        trip.video_or_link = video_or_link
        if video_or_link == '2':
            video = request.FILES.get("video")
            trip.video = video
            trip.link = ''
        if video_or_link == '1':
            link = request.POST.get("link")
            trip.link = link
            trip.video = ''
        trip.save()
        return redirect("change-trip", pk)
    return render(request, 'change-trip.html', context)


@login_required(login_url='login')
def AddProjectCategory(request):
    if request.method == "POST":
        name = request.POST.get("name")
        name_uz = request.POST.get("name_uz")
        name_ru = request.POST.get("name_ru")
        name_en = request.POST.get("name_en")
        CategoryProjects.objects.create(name=name, name_uz=name_uz, name_ru=name_ru, name_en=name_en)
    return redirect("projects")


@login_required(login_url='login')
def StreamingView(request):
    context = {
        "stream": Streaming.objects.all()
    }
    return render(request, 'streaming.html', context)


@login_required(login_url='login')
def ChangeStreaming(request, pk):
    if request.method == "POST":
        link = request.POST.get("link")
        title = request.POST.get("title")
        title_uz = request.POST.get("title_uz")
        title_ru = request.POST.get("title_ru")
        title_en = request.POST.get("title_en")
        st = Streaming.objects.get(id=pk)
        st.link = link
        st.title = title
        st.title_uz = title_uz
        st.title_ru = title_ru
        st.title_en = title_en
        st.save()
    return redirect("streaming")


@login_required(login_url='login')
def AddStreaming(request):
    if request.method == "POST":
        link = request.POST.get("link")
        title = request.POST.get("title")
        title_uz = request.POST.get("title_uz")
        title_ru = request.POST.get("title_ru")
        title_en = request.POST.get("title_en")
        Streaming.objects.create(
            link=link,
            title=title,
            title_uz=title_uz,
            title_ru=title_ru,
            title_en=title_en,
        )
    return redirect("streaming")


@login_required(login_url='login')
def DeleteStreaming(request, pk):
    Streaming.objects.get(id=pk).delete()
    return redirect("streaming")


@login_required(login_url='login')
def ChangeStatusStreaming(request):
    if request.method == "POST":
        st = Streaming.objects.get(id=request.POST.get("ids"))
        if st.status:
            st.status = False
        else:
            st.status = True
        st.save()
    return redirect("streaming")


@login_required(login_url='login')
def PhotosView(request):
    context = {
        "photo": Photos.objects.all()
    }
    return render(request, 'photos.html', context)


@login_required(login_url='login')
def VideosView(request):
    context = {
        "video": Videos.objects.all()
    }
    return render(request, 'videos.html', context)


@login_required(login_url='login')
def AddPhoto(request):
    if request.method == "POST":
        photo = request.FILES.get("photo")
        Photos.objects.create(
            photo=photo,
        )
    return redirect("photos")


@login_required(login_url='login')
def add_video(request):
    if request.method == "POST":
        img = request.FILES['img']
        type1 = int(request.POST.get('type'))
        link = request.POST.get('link')
        if type1 == 1:
            video = request.FILES.get("video")
            Videos.objects.create(
                video_or_url=type1, video=video, img=img
            )
        if type1 == 2:
            Videos.objects.create(
                video_or_url=type1, video_url=link, img=img
            )
    return redirect("videos")


@login_required(login_url='login')
def change_video(request, pk):
    if request.method == "POST":
        vid = Videos.objects.get(id=pk)
        type1 = int(request.POST.get('type'))
        img = request.FILES.get('img')
        link = request.POST.get('link')
        if img is not None:
            vid.img = img
            vid.save()
        if type1 == 1:
            if len(request.FILES) > 0:
                video = request.FILES.get("video")
                vid.video = video
            vid.video_or_url = type1
            vid.save()
        if type1 == 2:
            vid.video_or_url = type1
            vid.video_url = link
            vid.save()
    return redirect("videos")


@login_required(login_url='login')
def DeletePhoto(request, pk):
    Photos.objects.get(id=pk).delete()
    return redirect("photos")


@login_required(login_url='login')
def delete_video(request, pk):
    Videos.objects.get(id=pk).delete()
    return redirect("videos")


@login_required(login_url='login')
def ChangePhoto(request, pk):
    if request.method == "POST":
        photo = request.FILES.get("photo")
        st = Photos.objects.get(id=pk)
        st.photo = photo
        st.save()
    return redirect("photos")


@login_required(login_url='login')
def setting_view(request):
    return render(request, 'pages-settings.html')


@login_required(login_url='login')
def change_username(request):
    if request.method == "POST":
        username = request.POST.get('username')
        user = request.user
        user.username = username
        user.save()
    return redirect('setting')


@login_required(login_url='login')
def change_password(request):
    if request.method == "POST":
        current = request.POST.get('current')
        new = request.POST.get('new')
        verify = request.POST.get('verify')
        user = request.user
        if user.check_password(current):
            if new == verify:
                user.set_password(new)
                user.save()
                usr = authenticate(username=user.username, password=new)
                login(request, usr)
                return redirect('home')
            else:
                messages.error(request, 'Yangi kiritilayotgan parollar bir hil emas')
        else:
            messages.error(request, 'Eski parol hato')
    return redirect('setting')



