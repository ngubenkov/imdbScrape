from bs4 import BeautifulSoup
from mathematicians import simple_get



def get_hits_on_name(name):
    """
    Accepts a `name` of a mathematician and returns the number
    of hits that mathematician's wikipedia page received in the
    last 60 days, as an `int`
    """
    # url_root is a template string that used to buld a URL.
    url_root = 'https://xtools.wmflabs.org/articleinfo/en.wikipedia.org/{}'
    response = simple_get(url_root.format(name))

    if response is not None:
        html = BeautifulSoup(response, 'html.parser')

        hit_link = [a for a in html.select('a')
                    if a['href'].find('latest-60') > -1]

        if len(hit_link) > 0:
            # Strip commas:
            link_text = hit_link[0].text.replace(',', '')
            try:
                # Convert to integer
                print(int(link_text))
                return int(link_text)
            except:
                log_error("couldn't parse {} as an `int`".format(link_text))

    log_error('No pageviews found for {}'.format(name))
    return None

get_hits_on_name('Joseph Liouville')
