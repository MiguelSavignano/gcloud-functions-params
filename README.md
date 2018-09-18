# Gcloud functions params

Package for manage params in Python Gcloud functions

## Install
```requirements.txt
gcloud-functions-params==0.0.2
```

## Http function

You can call the function sending arguments:

http://function-url?name=example

or sending json

```
curl http://function-url -H "Content-Type: application/json" -d '{"name": "example"}'
```

```python
from gcloud_functions_params import args_or_json_to_dict

def main(request):
  params = args_or_json_to_dict(request)
```

## Pubsub function

Send a Json in the event message

message: '{"name": "example"}'

```python
from gcloud_functions_params import event_to_dict

def main(event, context):
  params = event_to_dict(event, context)
```

## Error handler

args_or_json_to_dict or event_to_dict return None if some error happen with the Json parse or if not send arguments

```python
from gcloud_functions_params import args_or_json_to_dict

def main(request):
  params = args_or_json_to_dict(request)
  if params:
    # ...
  else:
    raise Exception("Error sending params")
```
