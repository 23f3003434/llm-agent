import requests
import json
from config import url ,AI_TOKEN , function_list


#used internally
def getheaders():
    
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {AI_TOKEN}"
    }
    return headers

#used internally
def getjson(message):
    json=  {
        "model": "gpt-4o-mini",
        "messages": [
                                    {"role": "system", "content": "You are a function classifier that extracts structured parameters from queries."},
                                    {"role": "user", "content": message}
                                ],
                    "tools": [
                                {
                                    "type": "function",
                                    "function": function
                                } for function in function_list
                            ],
                    "tool_choice": "auto"
                }
    return json


def getfunctiondata(taskstring):
    jsondata = getjson(taskstring)
    headers = getheaders()
    response = requests.post(url, json=jsondata, headers=headers)
    response_json = response.json()

    choice = response_json['choices'][0]['message']

    if 'tool_calls' in choice:
        reply = choice['tool_calls'][0]['function']
        # print("Function Call:", reply)
        return reply
    else:
        reply = {"name": None, "arguments": None}
        # print("No function called. GPT Response:", choice.get('content'))
        return "Failed"
    







if __name__ == "__main__":
    taskstring = "Run 'SELECT * FROM students' on the database located at '/data/mydb.db' and save the result to '/output/result.txt'."
    got = getfunctiondata(taskstring)
    print(got)
