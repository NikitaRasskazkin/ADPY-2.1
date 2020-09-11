import json
import wikipediaapi


class CountriesInWiki:
    def __init__(self):
        with open('files/countries.json') as f:
            self.file = json.load(f)
            self.max_iter = len(self.file)
            self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        if self.index == self.max_iter:
            raise StopIteration
        country_name = self.file[self.index]['name']['common']
        response = wikipediaapi.Wikipedia('en')
        page_py = response.page(country_name)
        if page_py.exists() is True:
            country_url = page_py.fullurl
        else:
            country_url = None
        return country_name, country_url

    def write_data(self, path: str = 'files/country_data.txt', count: int = -1, console_log: bool = False):
        if count < 0:
            count = self.max_iter
        with open(path, 'w', encoding='utf-8') as f:
            for index, country in enumerate(self):
                if index == count:
                    break
                f.write(f'{country[0]}\t{country[1]}\n')
                if console_log:
                    print(f'{country[0]}    {country[1]}')
