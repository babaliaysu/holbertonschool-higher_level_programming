#!/usr/bin/env python3
"""API-dan melumat cekmek ve CSV-ye yazmaq ucun modul."""
import requests
import csv


def fetch_and_print_posts():
    """API-dan postlari cekir ve basliqlari cap edir."""
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    
    print(f"Status Code: {response.status_code}")
    
    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post['title'])


def fetch_and_save_posts():
    """API-dan postlari cekir ve posts.csv faylina yazir."""
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    
    if response.status_code == 200:
        posts = response.json()
        
        # Lazimi melumatlari secib siyahıya yigiriq
        structured_data = [
            {'id': p['id'], 'title': p['title'], 'body': p['body']} 
            for p in posts
        ]
        
        # CSV faylina yazmaq
        filename = "posts.csv"
        fieldnames = ['id', 'title', 'body']
        
        with open(filename, mode='w', encoding='utf-8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(structured_data)
