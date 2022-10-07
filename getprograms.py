import requests
import json

headers = {
    'Authorization': 'Basic <your_h1_username:your_h1_api_token>',
}

response = requests.get('https://api.hackerone.com/v1/hackers/programs?page[number]=1&page[size]=100', headers=headers)
output = json.loads(response.content)
first_program = 0
num_of_programs = len(output['data'])

def getprogs(first_program,num_of_programs,output):
    for i in range(0,num_of_programs):
        print(str(first_program+1) + " - " + output['data'][i]['attributes']['name'])      
        if (first_program == num_of_programs-1):
            try:
                next_programs = output['links']['next']
                response = requests.get(next_programs, headers=headers)
                output = json.loads(response.content)
                num_of_programs = len(output['data']) + first_program
                getprogs(first_program,num_of_programs,output)
            except:
                return
        first_program += 1
        
getprogs(first_program, num_of_programs,output)