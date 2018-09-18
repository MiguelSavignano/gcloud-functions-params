"""
Convert flask request arguments or json in dictionary
"""

def args_or_json_to_dict(request):
  try:
    if request.args:
      return request.args.to_dict()
    else:
      request_json = request.get_json()
      if request_json:
        return request_json
      else:
        return None
  except:
    return None

"""
Convert event to dict
Decode event message and load json
"""
def event_to_dict(event, context):
  import base64
  import json
  try:
    if event['data']:
      return json.loads(base64.b64decode(event['data']).decode('utf-8'))
    else:
      return None
  except:
    return None
