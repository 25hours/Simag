#!/usr/bin/env python
from flask import make_response
def online(task_id):
    # resp = make_response('ok')
    resp = make_response(task_id)
    # resp = 'ok'
    print(resp)
    return resp

if __name__ == '__main__':
    online()