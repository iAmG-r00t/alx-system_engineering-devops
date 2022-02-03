#!/usr/bin/python3
"""
A script that gathers data from an API
"""

import requests
import re
import sys

REST_API = "https://jsonplaceholder.typicode.com"


if __name__ == '__main__':
    if len(sys.argv) > 1:
        if re.fullmatch(r'\d+', sys.argv[1]):
            id = int(sys.argv[1])
            emp_req = requests.get('{}/users/{}'.format(REST_API, id)).json()
            todo_req = requests.get('{}/todos'.format(REST_API, id)).json()
            emp_name = emp_req.get('name')
            todo = list(filter(lambda x: x.get('userId') == id, todo_req))
            completed_todo = list(filter(lambda x: x.get('completed'), todo))
            print(
                'Employee {} is done with tasks({}/{}):'.format(
                    emp_name,
                    len(completed_todo),
                    len(todo)
                    )
                )
            for completed in completed_todo:
                print('\t {}'.format(completed.get('title')))
