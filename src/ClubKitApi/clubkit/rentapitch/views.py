from clubkit.rentapitch.models import RentPitch
from clubkit.clubs.models import Pitch, ClubInfo
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
        club = ClubInfo.objects.filter(pk=club_pk)
        inital_data = {
            'club_id': club_pk
        }
        form = RentalForm(initial=inital_data)
        form.fields['pitch_id'].queryset = Pitch.objects.filter(club_id=club_pk, rental=1)
        return Response({'form': form,
                         'club_pk': club_pk,
                         'club': club
                         })

    def post(self, request):
        club_pk = request.session.get('pk')
        club = ClubInfo.objects.filter(pk=club_pk)
        form = RentalForm(data=request.data)
        form.fields['pitch_id'].queryset = Pitch.objects.filter(club_id=club_pk, rental=1)
        if form.is_valid():
            form.save()
            return render(request, 'booking_complete.html', {'club': club,
                                                             'form': form})
        else:
            return Response({'form': form,
                             'club': club
                             })


def load_pitch_price(request):
    pitch_name = request.GET.get('pitch_name')
    pitch_id = Pitch.objects.filter(pk=pitch_name)
    return render(request, 'load_pitch_price_value.html', {'pitch_id': pitch_id})


class PitchBookings(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'pitch_bookings.html'

    def get(self, request):
        club_pk = request.session.get('pk')
        club = ClubInfo.objects.filter(pk=club_pk)
        bookings = RentPitch.objects.filter(club_id=club_pk)
        return Response({'bookings': bookings,
                         'club_pk': club_pk,
                         'club': club
                         })


def cancel_booking(request, pk):
    rental_id = RentPitch.objects.filter(pk=pk)
    rental_id.delete()
    return redirect('rentapitch:pitch_bookings')


def edit_booking(request, pk):
    club_pk = request.session.get('pk')
    club = ClubInfo.objects.filter(pk=club_pk)
    instance = RentPitch.objects.filter(pk=pk).first()
    if request.method == 'POST':
        form = RentalForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('rentapitch:pitch_bookings')
        else:
            return redirect('rentapitch:pitch_bookings')
    else:
        form = RentalForm(instance=instance)
        return render(request, 'edit_booking.html', {'form': form,
                                                     'instance': instance,
                                                     'club': club})



