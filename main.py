import sys
import time

import requests
import json
import csv
from dotenv import load_dotenv
import bs4



def main():
    # load .env file
    load_dotenv()
    # url to know count of users
    # parse headers from headers.txt file
    headers = parse_headers('headers.txt')
    # default count of users
    count_users = 2
    # url to get users in json
    url_json = f'https://leader-id.ru/api/v4/users/search?paginationSize={count_users}&cityId=&query=&employment=1815315'
    # get json
    response = requests.get(url_json, headers=headers)
    # parse json
    json_data = json.loads(response.text)
    # get count of users
    count_users = json_data['data']['_meta']['totalCount']
    # change url to get all users
    url_json = f'https://leader-id.ru/api/v4/users/search?paginationSize={count_users}&cityId=&query=&employment=1815315'
    # get all users
    response = requests.get(url_json, headers=headers)
    # parse json
    json_data = json.loads(response.text)
    # get users
    users = json_data['data']['_items']
    # print count of users
    print(f"count of users: {len(users)}")
    # write users id to array
    users_id = []
    for user in users:
        users_id.append(user['id'])
    # parse users birthday
    i = 0
    for user_id in users_id:

        # url to get user
        url = f'https://leader-id.ru/users/{user_id}'
        # get user
        response = requests.get(url, headers=headers)
        # write response to file
        soup = bs4.BeautifulSoup(response.text, 'html.parser')
        # get user birthday
        try:
            birthday = soup.find('span', attrs={"data-qa": "profileBirthday"}).text
            # add birthday to users
            users[i]['birthday'] = birthday
        # if user not have birthday
        except:
            users[i]['birthday'] = None
            print("\rbirthday not found", end=" ")
            print("user_id:", user_id, "i:", i)

        i += 1
        sys.stdout.flush()
        print(f'\r{round(i/len(users_id)*100, 2)}%', end='')




    # write users to json file
    with open('users.json', 'w') as f:
        json.dump(users, f)
    # write users to csv file
    with open('users.csv', 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['id', 'last_name', 'first_name', 'father_name', 'tags', 'settings', 'requestContacts', 'phone',
                      'email', 'last_seen', 'photo', 'photo_520', 'photo_360', 'photo_180', 'photo_cover',
                      'photo_cover_1024', 'photo_cover_720', 'matches', 'birthday']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for user in users:
            writer.writerow(user)

    input("Press Enter to continue...")


def parse_headers(file_name):
    with open(f'{file_name}', 'r') as f:
        text = f.read()
        array = text.split('\n')
        headers = {}
        for i in array:
            key = i[:i.find(':')]
            value = i[i.find(':') + 1:][1:]
            headers[key] = value

        return headers


if __name__ == '__main__':
    main()
