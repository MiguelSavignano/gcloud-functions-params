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

The FlaskRequest arguments or json it's parse in dictionary

```python
from gcloud_functions_params import args_or_json_to_dict

def main(request):
  params = args_or_json_to_dict(request)
  print(str(params))
```

## Pubsub function

Send a Json in the event message

message: '{"message": "example"}'

Test in Gcloud Function details:
(message are decode in base64)

{"data": "eyJtZXNzYWdlIjogImV4YW1wbGUifQo="}

The event it's decode in base64 and parse in dictionary

```python
from gcloud_functions_params import event_to_dict

def main(event, context):
  params = event_to_dict(event, context)
  print(str(params))
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

## Module Doc

[gcloud_functions_params](https://miguelsavignano.github.io/gcloud-functions-params/source/gcloud_functions_params.html#module-gcloud_functions_params)

## Test

```
pip3 install ostruct
```

```
python3 test.py
```

or

```
docker-compose run --rm app
```
