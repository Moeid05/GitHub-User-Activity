import argparse
import http.client
import json
from decouple import config

def fetch_github_activity(username):

    token = config('token')
    conn = http.client.HTTPSConnection("api.github.com")
    headers = {
        'Authorization': token,
        'X-GitHub-Api-Version': '2022-11-28'
    }
    conn.request("GET", "/events", headers=headers)
    response = conn.getresponse()
    data = response.read()
    if response.status == 200:
        events = json.loads(data)
        print(events)
    else:
        print(f"Error: {response.status} - {data.decode('utf-8')}")
    conn.close()

def main():
    parser = argparse.ArgumentParser(description='Fetch GitHub activity for a user.')
    parser.add_argument('username', type=str, help='GitHub username to fetch activity for')
    args = parser.parse_args()
    fetch_github_activity(args.username)

if __name__ == '__main__':
    main()