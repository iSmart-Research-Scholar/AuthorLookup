from django.shortcuts import redirect
from http.client import HTTPResponse
import requests,json
from django.http import JsonResponse

def findAuthorDetails(req):
    if req.method=='GET':
        author=req.GET.get("author")
        print(author)
        link=f'https://api.semanticscholar.org/graph/v1/author/search?query={author}'
        res=requests.get(link).json()['data']
        authors=[]
        for i in res:
            authors.append(i['authorId'])
        headers = {'content-type': 'application/json'}
        data={"ids": authors}
        link='https://api.semanticscholar.org/graph/v1/author/batch?fields=url,name,paperCount,papers,papers.title,papers.openAccessPdf'
        result = requests.post(link,data=json.dumps(data), headers=headers).json()
        return JsonResponse(result,safe=False)
        
        