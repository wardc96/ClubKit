from django.shortcuts import render, redirect
from django.urls import reverse
from clubkit.clubs.forms import ClubInfoForm
from clubkit.clubs.models import ClubInfo


def club_home(request, pk=None):
    if pk:
        club = ClubInfo.objects.filter(pk=pk)
    elif request.user.is_authenticated:
        club = ClubInfo.objects.filter(user=request.user)
    # photo = model.club_logo.ImageField(storage=profile_pics)
    args = {'club': club,
            }
    return render(request, 'club_home_page.html', args)


def edit_club(request):
    instance = ClubInfo.objects.filter(user=request.user).first()
    if request.method == 'POST':
        form = ClubInfoForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            return redirect('/')
    else:
        form = ClubInfoForm(instance=instance)
        return render(request, 'edit_club.html', {'form': form})


'''
class TeamInfo(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'edit_club_roster.html'

    def get(self, request):
        serializer = TeamSerializer()
        return Response({'serializer': serializer,
                         })

    def post(self, request):
        serializer = TeamSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'serializer': serializer,
                             })

'''