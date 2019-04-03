from QuestionC import LRUCache
import random

if __name__ == '__main__':

    # Test the cache
    Keys = [i for i in range(7)]     # Total Entries
    sites = ['www.amazon.com ', 'www.google.com ', 'www.Ebay.com ', 'www.facebook.com ', 'www.mozilla.com ',
              'www.Ebay.com ', 'www.natgeo.com ', 'www.github.com ']

    # Cache object
    cache = LRUCache(3, "Canada/Eastern", True)


    # Updating Cache with entries
    for i, key in enumerate(Keys):
        if key in cache.dictionary:
            continue
        else:
            value = ''.join([random.choice(sites)])
            print('\t', value)
            cache.put(key, value, "2019-01-26 11:43:59")

        print("{0}.Iteration, #{1} cached entries" .format(i+1, cache.capacity))

    # Cache List
    print('\n\n\t', ' CACHE LIST ')
    for k, v in cache.dictionary.items():
        print("{0} : {1}".format(k, v))
