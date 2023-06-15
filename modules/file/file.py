import requests
import os.path as path


def get_filename_by_url(url):
    if url is None:
        return False
    return url.split('/')[-1]


def download(url, folder):

    if url is None:
        return False

    filename = get_filename_by_url(url)

    if not filename:
        return False

    if not path.isfile(folder + filename):

        data = requests.get(url, allow_redirects=True).content

        with open(folder + filename, 'wb') as handler:
            handler.write(data)