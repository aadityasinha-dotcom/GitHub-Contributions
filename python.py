import requests
import json

repo_owner = 'aadityasinha-dotcom'
repo_name = 'kubernetes-client'
pr_number = '#3409'

url = f'https://api.github.com/repos/{repo_owner}/{repo_name}/pulls/{pr_number}'
response = requests.get(url)
data = json.loads(response.text)
pr_description = data['body']

# Insert pr_description into your README file

