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

    dummyData = '''
    [{
    "uniqueId": "601cee12e4b07bbc25b7fdfa",
    "email": null,
    "phone": null,
    "role": "Incubator",
    "name": "NRRI-ABIs",
    "website": "https://nrri-abi.com/caip.php/",
    "incubator_linkedin": ["https://www.linkedin.com/in/nrri-abi-1418a7199/"],
    "company_linkedin": ["https://www.linkedin.com/in/b-c-patra-b8713719/"],
    "application": "https://nrri-abi.com/caip.php/",
    "image": "6a67f04f-09a0-41ff-8ccd-73defba02cd7.jpg",
    "companyLogo": true,
    "stateRecognized": null,
    "migratedUser": false,
    "coverImage": null,
    "gallery": null,
    "dateOfEstablishment": "01/01/2016",
    "description": "<p><a href=\"https://nrri-abi.com/caip.php\" target=\"_blank\">https://nrri-abi.com/caip.php</a><a href=\"https://nrri-abi.com/caip.php\" target=\"_blank\"></a></p><p><a href=\"https://nrri-abi.com/tedp.php\" target=\"_blank\">https://nrri-abi.com/tedp.php</a><a href=\"https://nrri-abi.com/sedp.php\" target=\"_blank\"></a></p><p><a href=\"https://www.google.com/maps/place/Common+service+center/@20.462147,85.914486,15z/data=!4m5!3m4!1s0x0:0x57560bd295cedc2e!8m2!3d20.4621472!4d85.9144864?hl=en-US\" target=\"_blank\">https://nrri-abi.com/sedp.php</a></p><p><a href=\"https://nrri-abi.com/training-on-demand.php\" target=\"_blank\">https://nrri-abi.com/training-on-demand.php</a><a href=\"https://nrri-abi.com/training-on-demand.php\" target=\"_blank\"></a></p><p>https://www.vikasrabi.com/</p><p><br></p><p><br><br></p>",
    "location": {
        "country": {
            "id": "5f02e38c6f3de87babe20cd2",
            "name": null,
            "text": null,
            "countryName": "India",
            "deleted": false
        },
        "state": {
            "id": "5f48ce592a9bb065cdf9fb36",
            "name": null,
            "text": null,
            "stateName": "Odisha",
            "deleted": false,
            "isUnionTerritory": false
        },
        "city": {
            "id": "5f48ce5a2a9bb065cdf9fca0",
            "name": null,
            "text": null,
            "districtName": "Cuttack",
            "deleted": false,
            "state": {
                "id": "5f48ce592a9bb065cdf9fb36",
                "name": null,
                "text": null,
                "stateName": "Odisha",
                "deleted": false,
                "isUnionTerritory": false
            },
            "isActive": true
        },
        "cities": null
    },
    "pan": null,
    "services": ["5f48ce5f2a9bb065cdfa184d", "5f48ce5f2a9bb065cdfa1844", "5f48ce5f2a9bb065cdfa1855"],
    "preferredStartupStages": ["Prototype", "Validation", "EarlyTraction", "Scaling"],
    "programDuration": 6,
    "numberOfIncubatees": 5,
    "numberOFIncubateesGraduated": 9,
    "applicationLink": null,
    "dippEmpanelmentNumber": null,
    "govtFunded": true,
    "portfolios": [{
        "startupName": "\u201cIT Enabled Self Sufficient Sustainable Seed System in Rice (4S4R)\u201d",
        "url": "https://nrri-abi.com/incubation.php",
        "sihProfileUrl": null,
        "brief": "<p>The 4S4R model provides solution to the problem associated with formal seed sector Since the seed production is closely supervised by FPO members, the RIGHT quality is ensured. The seed is also certified by seed certification agency, in our case OSSOPCA \u2013 Odisha State Seed and Organic Product Certification Agency. The seed requirement is assessed through remote sensing data and ground trothing, therefore, farmers get RIGHT quantity of seed as well as RIGHT variety as per their preference.</p>",
        "startupEntryDate": "01/01/2018",
        "startupLogo": "79be2980-3fac-420d-ac1b-04117f26f712.jpg",
        "guidanceAreas": null
    }],
    "contacts": [{
        "firstName": "Dr. G.A.K",
        "lastName": "KUMAR",
        "designation": "HEAD-NRRI-ABI",
        "emailId": "gak.kumar26@gmail.com",
        "mobileNumber": "9437484576",
        "landlineNumber": null,
        "website": "https://nrri-abi.com/",
        "socialMediaAccountURL": null
    }],
    "lookingToConnectTo": null,
    "members": null,
    "socialInfos": null,
    "centerLocations": [{
        "incubatorCenterLocationAddress": "AGRIBUSINESS INCUBATION CENTRE(ABI)ICAR-NATIONAL RICE RESEARCH INSTITUTE(NRRI),CUTTACK-753006,ODISHA",
        "incubationCenterLocation": "https://www.google.co.in/maps/place/NRRI-AGRIBUSINESS+INCUBATION+CENTRE/@20.4519529,85.9346536,17z/data=!3m1!4b1!4m5!3m4!1s0x3a197366e9982ff9:0x51056b7f1d255a35!8m2!3d20.4519479!4d85.9368423"
    }],
    "address": null,
    "interestedAreas": null,
    "startupServices": null,
    "seed_funding_score": 74,
    "physical_amenities": 95,
    "talent_score": 54,
    "further_funding": 3
    }, {
    "uniqueId": "6016cdd1e4b0ba5b7b2db6af",
    "email": null,
    "phone": null,
    "role": "Incubator",
    "name": "K-tech Innovation Hub NASSCOM ",
    "website": "http://k-tech.org/",
    "incubator_linkedin": ["https://www.linkedin.com/in/ktechbfc/", "https://www.linkedin.com/company/nasscom-centre-of-excellence-data-science-artificial-intelligence/"],
    "company_linkedin": ["https://www.linkedin.com/company/gnani-ai/", "https://www.linkedin.com/company/mobile10x/", "https://www.linkedin.com/in/atgcbiotech/"],
    "application": "http://k-tech.org/funding/",
    "image": null,
    "companyLogo": false,
    "stateRecognized": null,
    "migratedUser": false,
    "coverImage": null,
    "gallery": null,
    "dateOfEstablishment": "08/01/2013",
    "description": "<p>K-TECH INNOVATION HUB BY NASSCOM :\n</p><p>Overview:\n</p><p>The Government of Karnataka in line with its i4 policy has set up a K-Tech Innovation Hub at NASSCOM Diamond District, Old Airport Road, Domlur, Bengaluru. The facility has been fully set up and has been operational since 2013. K-Tech Innovation Hub is housed in the premises of Diamond District, Old Airport Road, Bengaluru. It is spread over an area of 37,000 sq. ft. and has a seating capacity of 350 with a 100% power backup, leased internet line, a vibrant ambiance, Conference room with AV facility, over 10 meeting rooms, cafeteria and housekeeping facilities. The facility offers subsidized incubation space which will help the Start-ups to make use of the ecosystem and in turn help the companies which are in their nascent stages to attract angel investors, VC\u2019s and enterprises to play a major role in Bengaluru and helping more such Start-ups to thrive and succeed. They offer various services for e.g. providing physical workspace (Plug &amp; Play), Support Services (HR/Legal/Accounting etc.), access to network of investors, mentors, and industry experts etc., access to Startup Kits etc. besides the subsidised seat rentals</p>",
    "location": {
        "country": {
            "id": "5f02e38c6f3de87babe20cd2",
            "name": null,
            "text": null,
            "countryName": "India",
            "deleted": false
        },
        "state": {
            "id": "5f48ce592a9bb065cdf9fb2d",
            "name": null,
            "text": null,
            "stateName": "Karnataka",
            "deleted": false,
            "isUnionTerritory": false
        },
        "city": {
            "id": "5f48d0c92a9bb065cdfc4507",
            "name": null,
            "text": null,
            "districtName": "Bengaluru",
            "deleted": false,
            "state": {
                "id": "5f48ce592a9bb065cdf9fb2d",
                "name": null,
                "text": null,
                "stateName": "Karnataka",
                "deleted": false,
                "isUnionTerritory": false
            },
            "isActive": true
        },
        "cities": null
    },
    "pan": null,
    "services": ["5f48ce5f2a9bb065cdfa184a"],
    "preferredStartupStages": ["Scaling"],
    "programDuration": 12,
    "numberOfIncubatees": 50,
    "numberOFIncubateesGraduated": 200,
    "applicationLink": null,
    "dippEmpanelmentNumber": null,
    "govtFunded": true,
    "portfolios": null,
    "contacts": [{
        "firstName": "GAURVA ",
        "lastName": "PATWA",
        "designation": "Incubation Lead",
        "emailId": "gpatwa@nasscom.in",
        "mobileNumber": "7976970424",
        "landlineNumber": null,
        "website": "http://www.10000startups.com/",
        "socialMediaAccountURL": null
    }],
    "lookingToConnectTo": null,
    "members": null,
    "socialInfos": null,
    "centerLocations": [{
        "incubatorCenterLocationAddress": null,
        "incubationCenterLocation": null
    }],
    "address": null,
    "interestedAreas": null,
    "startupServices": null,
    "seed_funding_score": 89,
    "physical_amenities": 40,
    "talent_score": 1,
    "further_funding": 2
    }, {
    "uniqueId": "601696d6e4b0ba5b7b2d9e7d",
    "email": null,
    "phone": null,
    "role": "Incubator",
    "name": "Gopalakrishnan-Deshpande Centre for Innovation & Entrepreneurship",
    "image": "bd99ebb5-0028-4e10-98a6-e74994950b88.jpg",
    "companyLogo": true,
    "stateRecognized": null,
    "migratedUser": false,
    "coverImage": null,
    "gallery": null,
    "dateOfEstablishment": "01/01/2017",
    "description": "<p>GDC is an alumni-funded initiative set up at IIT Madras. Our charter is to work with faculty, researchers, students, and alumni of all STEM colleges in India who wish to commercialise their science-based research by way of start-ups to create impact at scale in society. We work with early-stage, deep-tech startup ideas (typically about TRL3) and endeavour to help the founders move up to TRL6. Through our highly acclaimed programs, I-NCUBATE and I-NSPIRE, we have worked with nearly 600 researchers and entrepreneurs from nearly 125 start-ups from nearly 20 academic institutions. I-NCUBATE and I-NSPIRE are highly transformative programs and all participants experience a dramatic transformation in their capabilities, knowledge, and entrpreneurial quotient. See a promo video at https://www.youtube.com/watch?v=MkFdpYztED0</p><p>&nbsp;</p>",
    "location": {
        "country": {
            "id": "5f02e38c6f3de87babe20cd2",
            "name": null,
            "text": null,
            "countryName": "India",
            "deleted": false
        },
        "state": {
            "id": "5f48ce592a9bb065cdf9fb3b",
            "name": null,
            "text": null,
            "stateName": "Tamil Nadu",
            "deleted": false,
            "isUnionTerritory": false
        },
        "city": {
            "id": "5f48ce5a2a9bb065cdf9fd7a",
            "name": null,
            "text": null,
            "districtName": "Chennai",
            "deleted": false,
            "state": {
                "id": "5f48ce592a9bb065cdf9fb3b",
                "name": null,
                "text": null,
                "stateName": "Tamil Nadu",
                "deleted": false,
                "isUnionTerritory": false
            },
            "isActive": true
        },
        "cities": null
    },
    "pan": null,
    "services": ["5f48ce5f2a9bb065cdfa184a", "5f48ce5f2a9bb065cdfa184d", "5f48ce5f2a9bb065cdfa1848", "5f48ce5f2a9bb065cdfa1855", "5f48ce5f2a9bb065cdfa1858"],
    "preferredStartupStages": ["Prototype", "Validation"],
    "programDuration": 6,
    "numberOfIncubatees": 15,
    "numberOFIncubateesGraduated": 125,
    "applicationLink": null,
    "dippEmpanelmentNumber": null,
    "govtFunded": false,
    "portfolios": [{
        "startupName": "Tan90 Innovation",
        "url": "https://www.t5eiitm.org/tan90-thermal-solutions-the-journey-from-an-idea-to-a-start-up/",
        "sihProfileUrl": "https://www.startupindia.gov.in/content/sih/en/profile.Startup.5e13207ae4b0ea02f54c8d4c.html",
        "brief": "<p>Tan90 is an energy efficient, green, cost effective enabler of refrigerated transport from farm to fork, providing portable, scalable and modular solutions, to increase shelf life of perishables. We provide end-to-end coverage from farm to fork, serving the hitherto un-served, unorganized primary producers, on the other hand and serving relatively organized intermediaries and end suppliers with lower capital cost and lower operating expenditure</p>",
        "startupEntryDate": "03/01/2018",
        "startupLogo": null,
        "guidanceAreas": null
    }, {
        "startupName": "Waste Chakra",
        "url": "https://www.wastechakra.com/",
        "sihProfileUrl": null,
        "brief": "<p>Waste Chakra is a clean tech company specialized in manufacturing of decentralized plastic pyrolysis machines. Our machines convert plastic waste to commercial fuel oil, facilitating sustainable plastic waste management. Our compact machines make sure plastic waste can be treated from your backyard.</p>",
        "startupEntryDate": "03/01/2018",
        "startupLogo": null,
        "guidanceAreas": null
    }, {
        "startupName": "Solinas Integrity Pvt Ltd",
        "url": "http://solinas.in/",
        "sihProfileUrl": null,
        "brief": "<p>At Solinas, we build inline inspection robotic technologies for critical pipeline infrastructure to detect existing defects and also prevent failures, maximising the lifespan of assets. We serve O&amp;G, Petrochemical, Power plants, Water, Sanitation and Process Industries.</p>",
        "startupEntryDate": "03/01/2018",
        "startupLogo": null,
        "guidanceAreas": null
    }, {
        "startupName": "VayyJal Technologies Pvt Ltd",
        "url": "https://vayujal.com/",
        "sihProfileUrl": null,
        "brief": "<p>VayuJal Technologies Pvt. Ltd. is an Indian company that aims to alleviate the global water shortage crisis through the development and manufacturing of Atmospheric Water Generators (AWGs). We started in 2016 and our AWGs were designed to be an affordable water extraction solution that was also environmentally sustainable to quench the thirst of millions. We are incubated by IIT Madras Research Center and are part of their \u2018Water for the Future\u2019 initiative.</p><p><br></p>",
        "startupEntryDate": "08/01/2019",
        "startupLogo": null,
        "guidanceAreas": null
    }],
    "contacts": [{
        "firstName": "Raghuttama",
        "lastName": "Rao",
        "designation": "CEO",
        "emailId": "raghu@gdciitm.org",
        "mobileNumber": "9840070795",
        "landlineNumber": null,
        "website": "http://www.gdc-iitm.org/",
        "socialMediaAccountURL": null
    }],
    "website": null,
    "lookingToConnectTo": null,
    "members": null,
    "socialInfos": null,
    "centerLocations": [{
        "incubatorCenterLocationAddress": "GDC, 2nd Floor, IC & SR Building (Annexe), IIT Madras, Chennai - 600036",
        "incubationCenterLocation": "12.993556574723657, 80.23221035074646"
    }],
    "address": null,
    "interestedAreas": null,
    "startupServices": null,
    "seed_funding_score": 72,
    "physical_amenities": 50,
    "talent_score": 61,
    "further_funding": 4
    }]
    '''.strip()
    
    return Response(dummyData)
