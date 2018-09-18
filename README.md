# Gcloud functions params

package for manage params in python gcloud functions

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

you can send a json in the event message

message: '{"name": "example"}'

```python
from gcloud_functions_params import event_to_dict

def main(event, context):
  params = event_to_dict(event)
```
