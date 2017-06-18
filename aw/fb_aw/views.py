from django.shortcuts import render
from django.views import generic
from pprint import pprint
import json,requests,random,re
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.http.response import HttpResponse


PAGE_ACCESS_TOKEN = "EAAXzB35M7mQBAIRdhJlvaMZCxSzLBfMnidu7cBDGuiUXO6efMxGM7l2bZACLbvbeeB3fk5KPyFXIMLMwAvna1iGwyIkQ2bqe5BNyPkwb4Y0HOBRASDHKpmyy2CXqn0NHp0wSOVZAtecMSQGSXQOsbCnzQy0WdIcW1wBxICcLAZDZD"
VERIFY_TOKEN = "01081996"

jokes = { 'stupid': ["""Yo' Mama is so stupid, she needs a recipe to make ice cubes.""", 
                     """Yo' Mama is so stupid, she thinks DNA is the National Dyslexics Association."""], 
         'fat':      ["""Yo' Mama is so fat, when she goes to a restaurant, instead of a menu, she gets an estimate.""", 
                      """ Yo' Mama is so fat, when the cops see her on a street corner, they yell, "Hey you guys, break it up!" """], 
         'dumb': ["""Yo' Mama is so dumb, when God was giving out brains, she thought they were milkshakes and asked for extra thick.""", 
                  """Yo' Mama is so dumb, she locked her keys inside her motorcycle."""] }
def post_facebook_message(fbid,rlat,rlong):


    #Remove all punctuations, lower case the text and split it based on space
    # tokens = re.sub(r"[^a-zA-Z0-9\s]",' ',recevied_message).lower().split()
    # joke_text = ''
    # for token in tokens:
    #     if token in jokes:
    #         joke_text = random.choice(jokes[token])
    # print ("latitude"+rlat)
    # print ("longitude"+rlong)
    # #         break
    # if not joke_text:
    #     joke_text = "I didn't understand! Send 'stupid', 'fat', 'dumb' for a Yo Mama joke!" 

    user_details_url = "https://graph.facebook.com/v2.6/%s"%fbid
    user_details_params = {'fields':'first_name,last_name,profile_pic', 'access_token':PAGE_ACCESS_TOKEN} 
    user_details = requests.get(user_details_url, user_details_params).json() 
    print(fbid)               
    post_message_url = 'https://graph.facebook.com/v2.6/me/messages?access_token=%s'%PAGE_ACCESS_TOKEN
    response_msg = json.dumps({"recipient":{"id":fbid}, })
    status = requests.post(post_message_url, headers={"Content-Type": "application/json"},data=response_msg)
    pprint(status.json())




class AWView(generic.View):
    def get(self, request, *args, **kwargs):
        if self.request.GET['hub.verify_token'] == '01081996':
            return HttpResponse(self.request.GET['hub.challenge'])

        else:
            return HttpResponse('Error, invalid token')
    @method_decorator(csrf_exempt)
    def dispatch(self,request,*args,**kwargs):
        return generic.View.dispatch(self,request,*args,**kwargs)

    def post(self,request,*args,**kwargs):
        incoming_message=json.loads(self.request.body.decode('utf-8'))
        for entry in incoming_message['entry']:
            
            for message in entry['messaging']:
                if 'message' in message:
                    
                    pprint(message)
                    if 'attachments' in message['message']:
                        ar=message['message']['attachments']
                        for j in ar:
                            content_type = j['type']
                            if content_type == 'location':
                                message_coordinates = (j['payload']['coordinates'])
                                latitude = message_coordinates['lat']
                                longitude = message_coordinates['long']
                                print(latitude,longitude)
                                post_facebook_message(message['sender']['id'], str (latitude), str( longitude))
                    
        return HttpResponse()

