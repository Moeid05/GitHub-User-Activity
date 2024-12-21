import sys
import json
import http.client
def get_latest_events(username):
    conn = http.client.HTTPSConnection("api.github.com")
    headers = {
        'User-Agent': 'Python GitHub Events Script'
    }
    conn.request("GET", f"/users/{username}/events", headers=headers)

    response = conn.getresponse()
    if response.status == 200 :
        events = json.load(response)
        for e in events :
            event_type = e['type']
            if event_type == 'PushEvent' :
                commits_count = len(e['payload']['commits'])
                print(f'- Pushed {commits_count} commits to {e["repo"]["url"]}')
            elif event_type == 'IssuesEvent' :
                print(f'- Opened a new issue in {e["repo"]["url"]}')
            elif event_type =='WatchEvent' :
                print(f'- Starred {e["repo"]["url"]}')
            elif event_type == 'PullRequestEvent' :
                print(f'- pulled from {e["repo"]["url"]}')
            elif event_type == 'ForkEvent' :
                print(f'- forked {e["repo"]["url"]}')
            elif event_type == 'CreateEvent' :
                print(f'- created {e["payload"]["ref_type"]} {e["payload"]["ref"]} in {e["repo"]["url"]}')
            elif event_type == 'DeleteEvent' :
                print(f'- deleted {e["repo"]["url"]}')

    else :
        print(response.status)
    conn.close()

if __name__ == "__main__":
    if len(sys.argv) > 1:
        username = sys.argv[1]
        get_latest_events(username)
    else:
        print("Please provide a GitHub username and a personal access token as command line arguments.")