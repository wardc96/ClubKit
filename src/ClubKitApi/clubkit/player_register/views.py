from clubkit.player_register.forms import PlayerRegistrationForm
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView
from rest_framework.response import Response
from clubkit.clubs.models import ClubInfo, ClubMemberships
from clubkit.player_register.models import Player
from django.shortcuts import render, redirect
from django.http import JsonResponse


# Class to handle membership registration information
class RegisterPlayer(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'player_registration.html'

    # Get method membership information and registration from
    def get(self, request):
        club_pk = request.session.get('pk')
        membership_price = request.session.get('membership_price')
        club = ClubInfo.objects.filter(pk=club_pk)
        club_info = ClubInfo.objects.filter(pk=club_pk).first()
        club_memberships = ClubMemberships.objects.filter(club_id=club_info)
        inital_data = {
            'club_id': club_info,
            'membership_title': club_memberships,
            'club_pk': club_pk,
            # 'price': price
        }
        form = PlayerRegistrationForm(initial=inital_data)
        # membership_id = form.fields['membership_title']
        form.fields['membership_title'].queryset = ClubMemberships.objects.filter(club_id=club_pk)
        # form.fields['price'].queryset = ClubMemberships.objects.numberfilter(title=membership_id).values('price')
        return Response({'form': form,
                         'club_pk': club_pk,
                         'club': club,
                         'membership_price': membership_price
                         })

    # Post method to save player registration
    def post(self, request):
        club_pk = request.session.get('pk')
        # membership_price = request.GET.get('membership_price')
        # price = ClubMemberships.objects.filter(price=membership_price).first()
        # membership_price = request.GET.get('membership_price')
        club = ClubInfo.objects.filter(pk=club_pk)
        form = PlayerRegistrationForm(data=request.data)
        # membership = ClubMemberships.objects.filter(membership_title=form.membership_title)
        if form.is_valid():
            form.save()
            return render(request, 'player_registration_complete.html', {'club': club,
                                                                         'club_pk': club_pk,
                                                                         # 'membership': membership,
                                                                         # 'price': price,
                                                                         'form': form
                                                                         })


def ajax_load_price(request):
    membership = request.GET.get('membership_title')
    mem_id = ClubMemberships.objects.filter(pk=membership)
    return render(request, 'load_price_value.html', {'mem_id': mem_id})

# Class to handle membership registration information
class Members(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'members.html'

    # Get method membership information and registration from
    def get(self, request):
        club_pk = request.session.get('pk')
        club = ClubInfo.objects.filter(pk=club_pk)
        club_info = ClubInfo.objects.filter(pk=club_pk).first()
        inital_data = {
            'club_id': club_info,
        }
        form = PlayerRegistrationForm(initial=inital_data)
        form.fields['membership_title'].queryset = ClubMemberships.objects.filter(club_id=club_pk)
        members = Player.objects.filter(club_id=club_info)
        return Response({'club_pk': club_pk,
                         'club': club,
                         'members': members,
                         'form': form,
                         })

    # Post method to add roster information
    def post(self, request):
        form = PlayerRegistrationForm(data=request.data)
        if form.is_valid():
            form.save()
            return redirect('player_register:members')


# Method to delete member
def delete_member(request, pk):
    member = Player.objects.filter(pk=pk)
    member.delete()
    return redirect('player_register:members')


# Method to edit roster information
def edit_member(request, pk):
    club_pk = request.session.get('pk')
    club = ClubInfo.objects.filter(pk=club_pk)
    instance = Player.objects.filter(pk=pk).first()
    if request.method == 'POST':
        form = PlayerRegistrationForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('player_register:members')
        else:
            return redirect('player_register:members')
    else:
        form = PlayerRegistrationForm(instance=instance)
        return render(request, 'edit_member.html', {'form': form,
                                                    'club': club,
                                                    'instance': instance})




'''
def ajax_set_price(request):
    membership_price = request.GET.get('membership_price')
    request.session['membership_price'] = membership_price
    # price = ClubMemberships.objects.filter(pk=membership).values('price')
    return membership_price
'''