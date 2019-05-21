from django.shortcuts import render, redirect, get_object_or_404
from clubkit.clubs.forms import ClubInfoForm, TeamForm, PitchForm, ClubPostForm, MembershipsForm
from clubkit.clubs.models import ClubInfo, Team, Pitch, ClubPosts, ClubMemberships, Packages
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView
from rest_framework.response import Response
from clubkit.cart.forms import CartAddProductForm


# Method to render club home page using pk to create session key
def club_home(request, pk=None):
    if pk:
        request.session['pk'] = pk
        club_pk = request.session.get('pk')
        club = ClubInfo.objects.filter(pk=club_pk)
        club_posts = ClubPosts.objects.filter(club_id=club[0])
        # club_info = ClubInfo.objects.filter(user=request.user).first()
        inital_data = {
            'club_id': club
        }
        new_post = ClubPostForm(initial=inital_data)
        if request.method == 'POST':
            new_post = ClubPostForm(data=request.POST)
            if new_post.is_valid():
                new_post.save()
                return redirect('clubs:club_home')
            else:
                return redirect('clubs:club_home')

        args = {'club': club,
                'club_posts': club_posts,
                'club_pk': club_pk,
                'new_post': new_post
                }

    else:
        club_pk = request.session.get('pk')
        club = ClubInfo.objects.filter(pk=club_pk)
        club_posts = ClubPosts.objects.filter(club_id=club[0])
        args = {'club': club,
                'club_posts': club_posts,
                'club_pk': club_pk
                }
    return render(request, 'club_home_page.html', args)


# Method to allow club owners edit their details
def edit_club(request):
    club_pk = request.session.get('pk')
    club = ClubInfo.objects.filter(pk=club_pk)
    instance = ClubInfo.objects.filter(user=request.user).first()
    if request.method == 'POST':
        form = ClubInfoForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('clubs:club_home')
        else:
            return redirect('clubs:club_home')
    else:
        form = ClubInfoForm(instance=instance)
        return render(request, 'edit_club.html', {'form': form,
                                                  'club': club
                                                  })


# Class to handle club posts
class ClubAddPosts(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'add_post.html'

    # Get method to display club posts on home page
    def get(self, request):
        club_pk = request.session.get('pk')
        club = ClubInfo.objects.filter(pk=club_pk)
        club_info = ClubInfo.objects.filter(user=request.user).first()
        inital_data = {
            'club_id': club_info
        }
        form = ClubPostForm(initial=inital_data)
        club_post = ClubPosts.objects.filter(club_id=club_pk)
        return Response({'form': form,
                         'club_post': club_post,
                         'club_pk': club_pk,
                         'club': club
                         })

    # Post method for publishing new club posts
    def post(self, request):
        club_pk = request.session.get('pk')
        club = ClubInfo.objects.filter(pk=club_pk)
        if request.method == 'POST':
            form = ClubPostForm(request.POST, request.FILES)
            user = ClubInfo.objects.filter(user=request.user).first()
            new_post = ClubPosts.objects.filter(club_id=user.pk)
            if form.is_valid():
                form.save()
                return redirect('clubs:club_home')
            else:
                return Response({'form': form,
                               'new_post': new_post,
                                 'club': club
                                 })


# Method to delete club posts using pk
def delete_post(request, pk):
    club_post = ClubPosts.objects.filter(pk=pk)
    club_post.delete()
    return redirect('clubs:club_home')


# Method to edit club posts using pk
def edit_post(request, pk):
    club_pk = request.session.get('pk')
    club = ClubInfo.objects.filter(pk=club_pk)
    instance = ClubPosts.objects.filter(pk=pk).first()
    if request.method == 'POST':
        form = ClubPostForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('clubs:club_home')
        else:
            return redirect('clubs:club_home')
    else:
        form = ClubPostForm(instance=instance)
        return render(request, 'edit_post.html', {'form': form,
                                                  'instance': instance,
                                                  'club': club})


# Class to handle team information
class TeamInfo(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'teams.html'

    # Get method to retrieve clubs team information using session key
    def get(self, request):
        if request.user.is_authenticated:
            club_pk = request.session.get('pk')
            club = ClubInfo.objects.filter(pk=club_pk)
            teams = Team.objects.filter(club_id=club_pk)
            club_info = ClubInfo.objects.filter(user=request.user).first()
            inital_data = {
                'club_id': club_info
            }
            form = TeamForm(initial=inital_data)
            return Response({
                'form': form,
                'teams': teams,
                'club_pk': club_pk,
                'club': club
            })
        else:
            club_pk = request.session.get('pk')
            club = ClubInfo.objects.filter(pk=club_pk)
            teams = Team.objects.filter(club_id=club_pk)
            return Response({
                             'teams': teams,
                             'club_pk': club_pk,
                             'club': club
                             })

    # Post method to post new team to club
    def post(self, request):
        form = TeamForm(data=request.data)
        if form.is_valid():
            form.save()
            return redirect('clubs:add_teams')


# Method to render form to add new teams to club
def add_team(request):
    if request.user.is_authenticated:
        club_pk = request.session.get('pk')
        club = ClubInfo.objects.filter(pk=club_pk)
        teams = Team.objects.filter(club_id=club_pk)
        club_info = ClubInfo.objects.filter(user=request.user).first()
        inital_data = {
            'club_id': club_info
        }
        form = TeamForm(initial=inital_data)
        return render(request, 'add_teams.html', {'form': form,
                                                  'teams': teams,
                                                  'club_pk': club_pk,
                                                  'club': club})
    else:
        return redirect('clubs:add_teams')


# Method to delete team using pk
def delete_team(request, pk):
    team = Team.objects.filter(pk=pk)
    team.delete()
    return redirect('clubs:teams')


# Method to edit team using pk
def edit_team(request, pk):
    club_pk = request.session.get('pk')
    club = ClubInfo.objects.filter(pk=club_pk)
    instance = Team.objects.filter(pk=pk).first()
    if request.method == 'POST':
        form = TeamForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('clubs:teams')
        else:
            return redirect('clubs:teams')
    else:
        form = TeamForm(instance=instance)
        return render(request, 'edit_team.html', {'form': form,
                                                  'instance': instance,
                                                  'club': club})


# Class to handle pitch information
class PitchInfo(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'pitches.html'

    # Get method to retrieve clubs pitch information using session key
    def get(self, request):
        if request.user.is_authenticated:
            club_pk = request.session.get('pk')
            club = ClubInfo.objects.filter(pk=club_pk)
            club_info = ClubInfo.objects.filter(user=request.user).first()
            inital_data = {
                'club_id': club_info
            }
            form = PitchForm(initial=inital_data)
            pitch = Pitch.objects.filter(club_id=club_pk)
            return Response({'form': form,
                             'pitch': pitch,
                             'club_pk': club_pk,
                             'club': club
                             })
        else:
            club_pk = request.session.get('pk')
            club = ClubInfo.objects.filter(pk=club_pk)
            pitch = Pitch.objects.filter(club_id=club_pk)
            return Response({'pitch': pitch,
                             'club_pk': club_pk,
                             'club': club
                             })

    # Post method to post new pitch to club
    def post(self, request):
        form = PitchForm(data=request.data)
        if form.is_valid():
            form.save()
            return redirect('clubs:pitches')


# Method to render form to add new pitches to club
def add_pitches(request):
    if request.user.is_authenticated:
        club_pk = request.session.get('pk')
        club = ClubInfo.objects.filter(pk=club_pk)
        pitch = Pitch.objects.filter(club_id=club_pk)
        club_info = ClubInfo.objects.filter(user=request.user).first()
        inital_data = {
            'club_id': club_info
        }
        form = PitchForm(initial=inital_data)
        return render(request, 'add_pitches.html', {'form': form,
                                                    'pitch': pitch,
                                                    'club_pk': club_pk,
                                                    'club': club})
    else:
        return redirect('clubs:add_pitches')


# Method to delete pitch using pk
def delete_pitch(request, pk):
    pitch = Pitch.objects.filter(pk=pk)
    pitch.delete()
    return redirect('clubs:pitches')


# Method to edit pitch using pk
def edit_pitch(request, pk):
    club_pk = request.session.get('pk')
    club = ClubInfo.objects.filter(pk=club_pk)
    instance = Pitch.objects.filter(pk=pk).first()
    if request.method == 'POST':
        form = PitchForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('clubs:pitches')
        else:
            return redirect('clubs:pitches')
    else:
        form = PitchForm(instance=instance)
        return render(request, 'edit_pitch.html', {'form': form,
                                                   'instance': instance,
                                                   'club': club})


# Class to handle membership information
class Memberships(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'memberships.html'

    # Get method to retrieve clubs membership information using session key
    def get(self, request):
        if request.user.is_authenticated:
            club_pk = request.session.get('pk')
            club = ClubInfo.objects.filter(pk=club_pk)
            club_info = ClubInfo.objects.filter(user=request.user).first()
            inital_data = {
                'club_id': club_info
            }
            form = MembershipsForm(initial=inital_data)
            # user = ClubInfo.objects.filter(user=request.user).first()
            memberships = ClubMemberships.objects.filter(club_id=club_pk)
            return Response({'form': form,
                             'memberships': memberships,
                             'club_pk': club_pk,
                             'club': club
                             })
        else:
            club_pk = request.session.get('pk')
            club = ClubInfo.objects.filter(pk=club_pk)
            memberships = ClubMemberships.objects.filter(club_id=club_pk)
            return Response({'memberships': memberships,
                             'club_pk': club_pk,
                             'club': club
                             })

    # Post method to post new membership to club
    def post(self, request):
        form = MembershipsForm(data=request.data)
        if form.is_valid():
            form.save()
            return redirect('clubs:memberships')


# Method to render form to add new memberships to club
def add_memberships(request):
    if request.user.is_authenticated:
        club_pk = request.session.get('pk')
        club = ClubInfo.objects.filter(pk=club_pk)
        membership = ClubMemberships.objects.filter(club_id=club_pk)
        club_info = ClubInfo.objects.filter(user=request.user).first()
        inital_data = {
            'club_id': club_info
        }
        form = MembershipsForm(initial=inital_data)
        return render(request, 'add_memberships.html', {'form': form,
                                                        'membership': membership,
                                                        'club_pk': club_pk,
                                                        'club': club})
    else:
        return redirect('clubs:add_membership')


# Method to delete membership using pk
def delete_membership(request, pk):
    memberships = ClubMemberships.objects.filter(pk=pk)
    memberships.delete()
    return redirect('clubs:memberships')


# Method to edit membership using pk
def edit_membership(request, pk):
    club_pk = request.session.get('pk')
    club = ClubInfo.objects.filter(pk=club_pk)
    instance = ClubMemberships.objects.filter(pk=pk).first()
    if request.method == 'POST':
        form = MembershipsForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('clubs:memberships')
        else:
            return redirect('clubs:memberships')
    else:
        form = MembershipsForm(instance=instance)
        return render(request, 'edit_membership.html', {'form': form,
                                                        'instance': instance,
                                                        'club': club})


def package_list(request):
    club_pk = request.session.get('pk')
    club = ClubInfo.objects.filter(pk=club_pk)
    packages = Packages.objects.filter(paid=False)
    context = {
        'packages': packages,
        'club_pk': club_pk,
        'club': club
    }
    return render(request, 'package-list.html', context)


'''
def package_detail(request, id, slug):
    club_pk = request.session.get('pk')
    club = ClubInfo.objects.filter(pk=club_pk)
    product = get_object_or_404(Packages, id=id, slug=slug, paid=False)
    cart_product_form = CartAddProductForm()
    context = {
        'product': product,
        'cart_product_form': cart_product_form,
        'club_pk': club_pk,
        'club': club
    }
    return render(request, 'package-detail.html', context)
'''
