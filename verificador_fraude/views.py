from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from utils import connectMongo
from bson.objectid import ObjectId
import json
import bson.json_util as json_util

db_client = connectMongo('Altair')

def homeAud(request):
    template = loader.get_template('verificador_fraude/homeAud.html')
    collection_licitacao = db_client['licitacao']
    licitacoes = collection_licitacao.find({})
    context = {
        'licitacoes':licitacoes
    }
    return HttpResponse(template.render(context, request))

def avaliar(request,pk):
    collection_licitacao = db_client['licitacao']
    licitacao = collection_licitacao.find_one({"_id":ObjectId(pk)})
    context = {
        'licitacao':json_util.dumps(licitacao)
    }
    modelo = loader.get_template('verificador_fraude/avaliar.html')
    return HttpResponse(modelo.render(context, request))
