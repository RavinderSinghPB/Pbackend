import time
from django.shortcuts import HttpResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response

import json
from bson.json_util import dumps, loads

from utils.mongo import get_db

# Create your views here.


@api_view(['GET'])
def our_work(request):
    
    db, client = get_db(db_name='pb_dev')
    collection = db['our_work']

    our_works = collection.find()
    our_works = json.loads(dumps(our_works))[:5]

    for our_work in our_works:
        our_work['id'] = our_work['_id']['$oid']
        del our_work['_id']

    client.close()
    return Response(our_works)

@api_view(['GET'])
def doner(request):
    
    db, client = get_db(db_name='pb_dev')
    collection = db['doner']

    doners = collection.find()
    doners = json.loads(dumps(doners))[:5]

    for people in doners:
        people['id'] = people['_id']['$oid']
        del people['_id']

    client.close()
    return Response(doners)

@api_view(['GET'])
def team(request):
    
    db, client = get_db(db_name='pb_dev')
    collection = db['team']

    teams = collection.find()
    teams = json.loads(dumps(teams))[:5]

    for people in teams:
        people['id'] = people['_id']['$oid']
        del people['_id']

    client.close()
    return Response(teams)
