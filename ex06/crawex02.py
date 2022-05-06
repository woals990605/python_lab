import requests

list = []

num = 1
error = 0

while True:
    try:
        i = ('{:0>10}'.format(num))
        html = requests.get(
            f"https://n.news.naver.com/mnews/article/005/{i}?sid=100")
        num = num+1
        print(html.status_code)
        if(html.status_code == 200):
            list.append(html.text)
            error = 0
        else:
            error = error+1
            
        if num%1000==0:
            print(f"다운받은개수 : {num}")
    except Exception as e:
        pass
    if error == 30:
        break

    print(len(list))
