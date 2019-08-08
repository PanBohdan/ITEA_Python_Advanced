from threading import Thread
import urllib.request


class OurContextManager:

    def __init__(self, filename, mode):
        self.object_we_are_working_with = open(filename, mode)

    def __enter__(self):
        return self.object_we_are_working_with

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.object_we_are_working_with.close()


def actual_decorator(func):
    def wrapper(url, filename, thread, daemon):
        t = Thread(target=func, args=(url, filename), name=thread, daemon=daemon)
        print(f"We are starting and working at {thread} with {url}")
        t.start()
        print(f"The end of {thread} which was working with {url}")
    return wrapper


@actual_decorator
def download_from_url(url, filename):
    try:
        opener = urllib.request.urlopen(url)
        with OurContextManager(filename, 'w') as file:
            file.write(str(opener.read()))
    except urllib.error.HTTPError:
        print(f"URL error at {filename}")


index = 1
list_of_urls = ['https://www.ukr.net',
                'https://stackoverflow.com',
                'http://sum.in.ua/s/vylazka', 'https://gmail.com',
                'https://www.youtube.com',
                'https://code-maven.com',
                'https://www.google.com.ua',
                'https://webpen.com.ua/pages/Syntax_and_punctuation/direct_speech.html',
                'https://github.com',
                'https://itea.ua/uk/']

for j in list_of_urls:
    download_from_url(j, f"file{index}", f"thread{index}", False)
    index += 1


with OurContextManager('some_file', 'r') as f:
    print(f.readlines())
