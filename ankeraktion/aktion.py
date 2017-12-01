#!/usr/bin/env python3
"""
this script helps you find cheap anker beer
"""

import requests
import argparse
import json
import sys

# default urls to search for anker beer
URLS = ['http://www.denner.ch/de/aktionen/articleaction/list/groupfilter0/bier/',
        'https://www.aktionis.ch/q/Bier']

def cli_args_parser():
    """ argument parser """
    parser = argparse.ArgumentParser(
        description='Anker-Service-CLI',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument(
        '-u',
        '--url',
        action='store',
        dest='url',
        help="url for Anker request"
    )
    parser.add_argument(
        '-r',
        choices=['html', 'json'],
        default='html',
        dest='request_type'
    )
    return parser.parse_args()

def get_html(urls):
    """ get content with request lib """
    url_list = urls
    content = []
    if type(urls) != list:
        url_list = []
        url_list.append(urls)
    try:
        for url in url_list:
            response = requests.get(url)
            content.append(response.content)
        return content
    except requests.exceptions.RequestException as err:
        print(err)
        sys.exit(1)

def get_json(urls):
    """ get information from json source """
    pass

def beer_check(content):
    """ check for anker """
    if b'Anker Lagerbier' in content:
        print('Anker ist Aktion!')
        exit(0)
    else:
        print('Anker leider nicht Aktion')
        exit(1)

if __name__ == "__main__":
    # catch input from cli
    # starte cli
    args = cli_args_parser()
    # scrap webcontent
    if args.url == None:
        content = get_html(URLS)
    else:
        content = get_html(args.url)
    # check if anker beer is cheap right now!
    beer_check(content)
