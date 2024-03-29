from django.shortcuts import render
from api.models import Post
from django.http import JsonResponse
import json

def detail(request):
    try:
        id = request.GET['id']
        res = Post.objects.filter(id=id)
    except Exception:
        res = Post.objects.all()
    data = {}
    for row in res.values_list():
        print(type(json.loads(row[2])), json.loads(row[2]))
        data = {
            "meta": json.loads(row[2]) if row[2] else {},
            "keyword": {
                "available": True if row[3] else False,
                "keywords": json.loads(row[3]) if row[3] else []
            },
            "posts": json.loads(row[4])
        }
        break
    return JsonResponse( data )


def main(request):
    id = request.GET['id']
    res = Post.objects.filter(id=id)
    data = {
        "meta": res.meta,
        "keyword": {
            "available": True if res.keyword else False,
            "keywords": res.keyword if res else []
        },
        "posts": res.posts
    }
    return HttpResponse( json.dumps(data) )
    

def add(request):
    x = Post(author="i_iary2", meta={
        "thumbnail":"https://scontent-icn1-1.cdninstagram.com/vp/93c5f4e4a0f30ab4929b8f514310fc45/5E520F48/t51.2885-19/s320x320/71219904_394028257956097_6460407248781836288_n.jpg?_nc_ht=scontent-icn1-1.cdninstagram.com",
        "author":"i_iary2",
        "follower":"14900",
        "name": "이아리",
        "description": "🌼 시시콜콜한 이야기✉ i.iary.diary@gmail.com"
    }, keywords=[ 
                { "label": "#갬성곰", "value": 1 },
                { "label": "#렛츠락페스티벌", "value": 1 },
                { "label": "#말든가", "value": 1 },
                { "label": "#그러든가", "value": 1 },
                { "label": "#자존곰", "value": 1 },
                { "label": "#텐션짱", "value": 1 },
                { "label": "#이불밖은", "value": 1 },
                { "label": "#위험해", "value": 1 },
                { "label": "#하늘공원", "value": 1 },
                { "label": "#핑크뮬리", "value": 1 },
                { "label": "#핑크풀카페", "value": 1 },
                { "label": "#배경화면", "value": 1 },
                { "label": "#아이폰배경화면", "value": 1 },
                { "label": "#갤럭시배경화면", "value": 1 },
                { "label": "#배경화면나눔", "value": 1 },
                { "label": "#무료배경화면", "value": 1 },
                { "label": "#당첨자발표", "value": 1 },
                { "label": "#숭실대", "value": 1 },
                { "label": "#과식", "value": 1 },
                { "label": "#과음아님", "value": 1 },
                { "label": "#억새숲", "value": 1 },
                { "label": "#가을감성", "value": 1 },
                { "label": "#가글아님", "value": 1 },
                { "label": "#닮은꼴찾기", "value": 1 },
                { "label": "#끼어들기성공", "value": 1 },
                { "label": "#ㅎㅎ", "value": 1 },
                { "label": "#ddp패션위크", "value": 1 },
                { "label": "#월요병", "value": 1 },
                { "label": "#분노곰", "value": 1 },
                { "label": "#집가고싶다", "value": 1 },
                { "label": "#독서", "value": 1 },
                { "label": "#가을날씨", "value": 1 },
                { "label": "#한정판굿즈", "value": 2 },
                { "label": "#5만명", "value": 2 },
                { "label": "#구독자이벤트", "value": 2 },
                { "label": "#귀여운캐릭터", "value": 4 },
                { "label": "#벨리곰이야기", "value": 4 },
                { "label": "#인스타툰", "value": 5 },
                { "label": "#그림", "value": 5 },
                { "label": "#벨리곰이야기_모아보기", "value": 5 },
                { "label": "#벨리곰", "value": 7 },
                { "label": "#cutecharacter", "value": 9 } 
        ], posts=[ {"likes":5572, "image":"https://scontent-icn1-1.cdninstagram.com/vp/9d9061a98d38d659bf89bbf2f2a358d6/5E4D21DF/t51.2885-15/sh0.08/e35/s640x640/74527310_931825897199105_5780876061267631189_n.jpg?_nc_ht=scontent-icn1-1.cdninstagram.com&_nc_cat=1"}, 
{"likes":4943, "image":"https://scontent-icn1-1.cdninstagram.com/vp/9d9061a98d38d659bf89bbf2f2a358d6/5E4D21DF/t51.2885-15/sh0.08/e35/s640x640/74527310_931825897199105_5780876061267631189_n.jpg?_nc_ht=scontent-icn1-1.cdninstagram.com&_nc_cat=1"}, 
{"likes":4373, "image":"https://scontent-icn1-1.cdninstagram.com/vp/9d9061a98d38d659bf89bbf2f2a358d6/5E4D21DF/t51.2885-15/sh0.08/e35/s640x640/74527310_931825897199105_5780876061267631189_n.jpg?_nc_ht=scontent-icn1-1.cdninstagram.com&_nc_cat=1"}, 
{"likes":4110, "image":"https://scontent-icn1-1.cdninstagram.com/vp/9d9061a98d38d659bf89bbf2f2a358d6/5E4D21DF/t51.2885-15/sh0.08/e35/s640x640/74527310_931825897199105_5780876061267631189_n.jpg?_nc_ht=scontent-icn1-1.cdninstagram.com&_nc_cat=1"}, 
{"likes":4015, "image":"https://scontent-icn1-1.cdninstagram.com/vp/9d9061a98d38d659bf89bbf2f2a358d6/5E4D21DF/t51.2885-15/sh0.08/e35/s640x640/74527310_931825897199105_5780876061267631189_n.jpg?_nc_ht=scontent-icn1-1.cdninstagram.com&_nc_cat=1"}, 
{"likes":3912, "image":"https://scontent-icn1-1.cdninstagram.com/vp/9d9061a98d38d659bf89bbf2f2a358d6/5E4D21DF/t51.2885-15/sh0.08/e35/s640x640/74527310_931825897199105_5780876061267631189_n.jpg?_nc_ht=scontent-icn1-1.cdninstagram.com&_nc_cat=1"}, 
{"likes":3350, "image":"https://scontent-icn1-1.cdninstagram.com/vp/9d9061a98d38d659bf89bbf2f2a358d6/5E4D21DF/t51.2885-15/sh0.08/e35/s640x640/74527310_931825897199105_5780876061267631189_n.jpg?_nc_ht=scontent-icn1-1.cdninstagram.com&_nc_cat=1"}, 
{"likes":3310, "image":"https://scontent-icn1-1.cdninstagram.com/vp/9d9061a98d38d659bf89bbf2f2a358d6/5E4D21DF/t51.2885-15/sh0.08/e35/s640x640/74527310_931825897199105_5780876061267631189_n.jpg?_nc_ht=scontent-icn1-1.cdninstagram.com&_nc_cat=1"}, 
{"likes":3060, "image":"https://scontent-icn1-1.cdninstagram.com/vp/9d9061a98d38d659bf89bbf2f2a358d6/5E4D21DF/t51.2885-15/sh0.08/e35/s640x640/74527310_931825897199105_5780876061267631189_n.jpg?_nc_ht=scontent-icn1-1.cdninstagram.com&_nc_cat=1"}, 
{"likes":3046, "image":"https://scontent-icn1-1.cdninstagram.com/vp/9d9061a98d38d659bf89bbf2f2a358d6/5E4D21DF/t51.2885-15/sh0.08/e35/s640x640/74527310_931825897199105_5780876061267631189_n.jpg?_nc_ht=scontent-icn1-1.cdninstagram.com&_nc_cat=1"}, 
{"likes":2356, "image":"https://scontent-icn1-1.cdninstagram.com/vp/9d9061a98d38d659bf89bbf2f2a358d6/5E4D21DF/t51.2885-15/sh0.08/e35/s640x640/74527310_931825897199105_5780876061267631189_n.jpg?_nc_ht=scontent-icn1-1.cdninstagram.com&_nc_cat=1"}, 
{"likes":1549, "image":"https://scontent-icn1-1.cdninstagram.com/vp/9d9061a98d38d659bf89bbf2f2a358d6/5E4D21DF/t51.2885-15/sh0.08/e35/s640x640/74527310_931825897199105_5780876061267631189_n.jpg?_nc_ht=scontent-icn1-1.cdninstagram.com&_nc_cat=1"} ] 
)
    x.save()
    return HttpResponse( "OK" )
  #  x.save()