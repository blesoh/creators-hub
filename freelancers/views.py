from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import FreelancerProfile
from .serializers import FreelancerProfileSerializer


@api_view(['GET'])
def list_freelancers(request):
    freelancers = FreelancerProfile.objects.all()
    serializer = FreelancerProfileSerializer(freelancers, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def freelancer_detail(request, id):
    try:
        freelancer = FreelancerProfile.objects.get(id=id)
    except FreelancerProfile.DoesNotExist:
        return Response(
            {'error': 'Freelancer not found'},
            status=status.HTTP_404_NOT_FOUND
        )

    serializer = FreelancerProfileSerializer(freelancer)
    return Response(serializer.data)


@api_view(['POST'])
def update_portfolio(request, id):
    try:
        freelancer = FreelancerProfile.objects.get(id=id)
    except FreelancerProfile.DoesNotExist:
        return Response(
            {'error': 'Freelancer not found'},
            status=status.HTTP_404_NOT_FOUND
        )

    freelancer.portfolio_link = request.data.get('portfolio_link')
    freelancer.save()

    return Response(
        {'message': 'Portfolio updated successfully'},
        status=status.HTTP_200_OK
    )

