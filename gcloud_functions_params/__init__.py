def args_or_json_to_dict(request):
  """
  Extract params arguments or json for FlaskRequest

  :param request: FlaskRequest
  :return: dict
  """
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

def event_to_dict(event, context):
  """
  Extract params decoding in base64 and parse Json for event message

  :param event: {'data'}
  :param context: Context
  :return: dict
  """
  import base64
  import json
  try:
    if event['data']:
      return json.loads(base64.b64decode(event['data']).decode('utf-8'))
    else:
      return None
  except:
    return None
