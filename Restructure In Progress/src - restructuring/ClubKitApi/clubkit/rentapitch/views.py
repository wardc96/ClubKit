from clubkit.rentapitch.models import RentPitch
from clubkit.clubs.models import Pitch
from clubkit.rentapitch.forms import RentalForm
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render, redirect


class PitchRental(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'pitch_rental.html'

    def get(self, request):
        club_pk = request.session.get('pk')
        inital_data = {
            'club_id': club_pk
        }
        form = RentalForm(initial=inital_data)
        form.fields['pitch_id'].queryset = Pitch.objects.filter(club_id=club_pk)
        return Response({'form': form,
                         'club_pk': club_pk
                         })

    def post(self, request):
        form = RentalForm(data=request.data)
        if form.is_valid():
            form.save()
            return Response(template_name='booking_complete.html')
        else:
            return Response({'form': form,
                             })


class PitchBookings(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'pitch_bookings.html'

    def get(self, request):
            club_pk = request.session.get('pk')
            # club = ClubInfo.objects.filter(user=request.user)
            bookings = RentPitch.objects.filter(club_id=club_pk)
            return Response({'bookings': bookings,
                             'club_pk': club_pk
                            })


def cancel_booking(request, pk):
    rental_id = RentPitch.objects.filter(pk=pk)
    rental_id.delete()
    return redirect('rentapitch:pitch_bookings')


def edit_booking(request, pk):
    instance = RentPitch.objects.filter(pk=pk).first()
    if request.method == 'POST':
        form = RentalForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('clubs:club_home')
        else:
            return redirect('clubs:club_home')
    else:
        form = RentalForm(instance=instance)
        return render(request, 'edit_post.html', {'form': form,
                                                  'instance': instance})



