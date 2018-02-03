def parse_request(request):
    print(request.json)
    conversion = {
        'data': request.json['data']
    }
    return conversion
