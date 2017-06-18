json = {
    'messaging': [{
        'message': {
            'mid': 'mid.$cAAIGGkCJsaBi6J0_Hlct1f5M-O4m',
            'attachments': [{
                'payload': {
                    'coordinates': {
                        'long': 77.312523,
                        'lat': 28.589116
                    }
                },
                'type': 'location',
                'title': "Simran's Location",
                'url': 'https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.bing.com%2Fmaps%2Fdefault.aspx%3Fv%3D2%26pc%3DFACEBK%26mid%3D8100%26where1%3D28.589116%252C%2B77.312523%26FORM%3DFBKPL1%26mkt%3Den-US&h=ATPP-mYIQ3oIXyx9NNy1US4WyZUpQgnbJlcT-LRVq-oxQjTYkqzOq8g4a9n4PsJkJ4udN071ZevFcQaFRpKgURVO8cYU51PY9wB1QcsBpofDX_YhEw&s=1&enc=AZOebLKjecJg27cEllUNnapetYYSJBxHI0rgv2JAqGsZl8lLBUoC2RbkP8NrUYgV9rDnmjj6F-QYuWF7Kdm5dyGE'
            }],
            'seq': 325223
        },
        'timestamp': 1497724614430,
        'recipient': {
            'id': '665107123673790'
        },
        'sender': {
            'id': '1520710114636982'
        }
    }],
    'time': 1497724614537,
    'id': '665107123673790'
}

def latlon():
    loc = json["messaging"]
    for i in loc:
        ar = i["message"]["attachments"]
        for j in ar:
            content_type = j['type']
            if content_type == 'location':
                message_coordinates = (j['payload']['coordinates'])
                latitude = message_coordinates['lat']
                longitude = message_coordinates['long']
                print(latitude,longitude)
    return latitude, longitude
