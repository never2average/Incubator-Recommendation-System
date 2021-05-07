import json

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from app.serializers import UserSerializer, GroupSerializer, ContactUsSerializer, GenerateResultsSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class ContactUs():
    def __init__(self, email, name, message, subject):
        self.email = email
        self.name = name
        self.subject = subject
        self.message = message


@api_view(['POST'])
def contactUs_view(request):
    print(request.data)
    email = request.data['email'][0]
    name = request.data['name'][0]
    message = request.data['message'][0]
    subject = request.data['subject'][0]
    comment = ContactUs(email=email, name=name,
                        message=message, subject=subject)
    serializer = ContactUsSerializer(comment)
    return Response(serializer.data)


class GenerateResults():
    def __init__(self, companies, profile):
        self.companies = companies
        self.profile = profile

# temp func
# def companyGen(c):
    


@api_view(['POST'])
def generateResults_view(request):
    print(request.data)
    profile = request.data['profile']
    # TODO: do some processing
    # adding dummy data for now
    # generatedResults = GenerateResults(
    #     [
    #         {
    #             "company1": [10, 20, 30, 'l1', 'l2'],
    #             "company2": [40, 50, 60, 'l1', 'l2'],
    #             "company3": [70, 80, 90, 'l1', 'l2']
    #             # "company1": {
    #             #     "ai": 10,
    #             #     "cos": 20,
    #             #     "funding": 30,
    #             #     "link1": "l1",
    #             #     "link2": "l2",
    #             #     "city": 
    #             # }
    #         }
    #     ],
    #     profile
    # )
    # serializer = GenerateResultsSerializer(generatedResults)

    # return Response(serializer.data)

    f = open("./21.json", mode='r')
    dummyData = json.load(f)
    dummyDataSerialized = {
        'incubators': dummyData
    }
    return Response(dummyDataSerialized)
