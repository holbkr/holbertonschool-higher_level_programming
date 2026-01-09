#!/usr/bin/python3
import requests
import csv

"""Module that add two functions who retreive the respond of an API request and
print the status code respond, and print all the title of the posts of this
page. The second function allow us to convert the response into a csv format in
a CSV file"""


def fetch_and_print_posts():
    """Function that print the status code of a response, and print the titles
    of the data retrieved"""
    answer = requests.get("https://jsonplaceholder.typicode.com/posts")
    print(f"Status Code: {answer.status_code}")

    if answer.status_code == 200:
        answer_json = answer.json()
        for i in answer_json:
            print(i['title'])


def fetch_and_save_posts():
    """Function that retrieve the response of a request and put some keys
    elements in a dictionary. It returns a list of this dictionaries"""
    answer = requests.get("https://jsonplaceholder.typicode.com/posts")
    if answer.status_code == 200:
        answer_json = answer.json()
        dict_list = []
        for i in answer_json:
            new_dict = {}
            new_dict['id'] = i['id']
            new_dict['title'] = i['title']
            new_dict['body'] = i['body']
            dict_list.append(new_dict)
        fields = ['id', 'title', 'body']
        with open("posts.csv", "w") as csv_file:
            write_dict = csv.DictWriter(csv_file, fieldnames=fields)
            write_dict.writeheader()
            write_dict.writerows(dict_list)
        return csv_file
