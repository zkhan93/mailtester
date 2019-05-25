import bs4
import requests

base_url = "http://mailtester.com/testmail.php"

def verify_email(email):
    try:
        res = requests.post(base_url, data=dict(email=email, lang='en'))
    except Exception as ex:
        return dict(status='fail', message='error occured', color='#FF4444')
    else:
        if not res.ok:
            return dict(status='fail', message='error occured', color='#FF4444')
        else:
            soup = bs4.BeautifulSoup(res.text, 'html.parser')
            table = soup.find('div', id='content').find('table', recursive=False)
            tds = [td for tr in table.find_all('tr')[2:] for td in tr.find_all('td') if td.has_attr('bgcolor')]
            color = None
            color_map = {
                '#FFBB00': 'warn',
                '#00DD00': 'success',
                '#FF4444': 'fail',
                None: 'fail'
            }
            status = 0
            message = tds[-1].text
            if len(tds) > 0:
                color = tds[-1].get('bgcolor')
            return dict(color=color,
                        message=message,
                        status=color_map.get(color))
