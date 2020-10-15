def main():
    import requests
    from bs4 import BeautifulSoup
    import re

    response = requests.get('https://sovetskaya-adygeya.ru/news/')
    response = response.text
    pattern = '<a href="(\/index\.php\/\/[0-9-a-z]+)">[А-ЯЁа-яё 0-9.,!?()\-""]+<\/a>'
    links_list = re.findall(pattern, response)
    for link in links_list:
        new_link = 'https://sovetskaya-adygeya.ru'+link
        response = requests.get(new_link)
        response = response.text
        soup = BeautifulSoup(response, features="html.parser")
        title = str(soup.h2.text)
        title = title.replace('\t', '')
        title = title.replace('\n', '')
        pattern = '\d\d\d\d\-\d\d\-\d\d'
        news_time = re.search(pattern, str(soup.time))
        tetext = soup.findAll('div', itemprop="articleBody")
        art = ''
        for elem in tetext:
            elem = str(elem)
            elem = BeautifulSoup(elem, features="html.parser")
            elem = elem.get_text()
            elem = str(elem)
            elem = elem.replace('\n', '')
            art = elem
        data_news = '=====' +'\n'+ str(new_link) + '\n' + 'Советская Адыгея\n' + str(news_time.group()) + '\n' + 'None\n' + title + '\n' + art + '\n'
        with open("data_file.txt", "a", encoding="utf-8") as f:
            f.write(data_news)
        with open("news_texts.txt", "a", encoding="utf-8") as f:
            f.write('=====' + '\n' + art + '\n')
    i = 36
    while i < 2881:
        adr = 'https://sovetskaya-adygeya.ru/index.php/news?start=' + str(i)
        response = requests.get(adr)
        response = response.text
        pattern = '<a href="(\/index\.php\/\/[0-9-a-z]+)">[А-ЯЁа-яё 0-9.,!?()\-""]+<\/a>'
        links_list = re.findall(pattern, response)
        for link in links_list:
            new_link = 'https://sovetskaya-adygeya.ru' + link
            response = requests.get(new_link)
            response = response.text
            soup = BeautifulSoup(response, features="html.parser")
            title = str(soup.h2.text)
            title = title.replace('\t', '')
            title = title.replace('\n', '')
            pattern = '\d\d\d\d\-\d\d\-\d\d'
            news_time = re.search(pattern, str(soup.time))
            tetext = soup.findAll('div', itemprop="articleBody")
            art = ''
            for elem in tetext:
                elem = str(elem)
                elem = BeautifulSoup(elem, features="html.parser")
                elem = elem.get_text()
                elem = str(elem)
                elem = elem.replace('\n', '')
                art = elem
            data_news = '=====' + '\n' + str(new_link) + '\n' + 'Советская Адыгея\n' + str(news_time.group()) + '\n' + 'None\n' + title + '\n' + art + '\n'
            with open("data_file.txt", "a", encoding="utf-8") as f:
                f.write(data_news)
            with open("news_texts.txt", "a", encoding="utf-8") as f:
                f.write('=====' + '\n' + art + '\n')
        i += 24




if __name__ == '__main__':
    main()

