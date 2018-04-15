from django.shortcuts import render


def indexRender(request):
    returnData = dict()
    RTlist = {a: a ** 2 for a in range(7)}
    returnData.update(a=RTlist)
    return render(request, 'mainpage/1.html', returnData)

