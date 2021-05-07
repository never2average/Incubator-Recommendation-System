import json
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from app.serializers import UserSerializer, GroupSerializer, ContactUsSerializer, GenerateResultsSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response

import numpy as np
import pandas as pd
from sqlalchemy import create_engine

def recommendation(location=[], *args):
    pd.set_option('display.max_columns', None)
    engine = create_engine('postgresql://postgres:root@localhost:5432/inqb8r')
    a=pd.read_sql_query('select * from "startupneeds"',con=engine)
    needs_map = {"EN": 3, "DB": 4, "NR": 0, "SR": 1, "NC": 2}
    needs_lmb = lambda x: needs_map.get(x,x)
    a = a.applymap(needs_lmb)
    a.drop("research_labs", axis=1, inplace=True)
    a.drop("market_access", axis=1, inplace=True)
    df2 = a.groupby(['industry']).mean()
    net_needs = []
    for i in args:
        if i not in df2.index:
            net_needs.append([2 for i in range(8)])
        else:
            net_needs.append(list(df2.loc[i])[1:])
    final = [0 for i in range(8)]
    for i in range(8):
        for j in net_needs:
            final[i] += j[i]
        final[i] /= len(net_needs)
        final[i] = round(final[i], 2)

    a=pd.read_sql_query('select * from "incubators"',con=engine)
    if location != []:
       a = a[a.city_name.isin(location)]
    data = []
    for i in a.index:
        temp = [0 for i in range(8)]
        temp[0] = int(a.loc[i]["physical_amenities"])
        temp[1] = int(a.loc[i]["seed_funding_score"])
        temp[2] = int(a.loc[i]["talent_score"])
        temp[3] = int(a.loc[i]["further_funding"])
        temp[4] = int(a.loc[i]["networking_events"])
        temp[5] = int(a.loc[i]["technical_mentorship"])
        temp[6] = int(a.loc[i]["logistics_support"])
        temp[7] = int(a.loc[i]["business_mentorship"])
        data.append(temp)

    performance = np.matrix(data)
    needs = np.matrix(final)
    result = performance*np.transpose(needs)
    a["Total Score"] = result
    a.sort_values("Total Score", axis=0, ascending=False, inplace=True)
    return a.to_dict("records")

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
    def _init_(self, email, name, message, subject):
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
    def _init_(self, companies, profile):
        self.companies = companies
        self.profile = profile

# temp func
# def companyGen(c):
    


@api_view(['POST'])
def generateResults_view(request):
    print(request.data)
    profile = request.data['profile']
    dataSerialized = {
        'incubators': recommendation([], request.data['categories'])
    }
    return Response(dataSerialized)
