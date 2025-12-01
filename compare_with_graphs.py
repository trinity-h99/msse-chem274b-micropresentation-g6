from gc import get_referents
import random
import sys
from time import time
from types import ModuleType, FunctionType

import matplotlib.pyplot as plt

from tst import TST


A_ascii = 65
C_ascii = 67
G_ascii = 71
T_ascii = 84


"""
Run this file to generate some graphs:
python compare_with_graphs.py
"""



def generate_random_word(min_length=3, max_length=12):
    # words are just random DNA letters (A, C, T, G), and of random lengths between 3 and 12 letters by default
    # Note that doing random letters from A-Z doesnt have much overlap so the TST took up a lot of space
    # having longer lengths didnt have much overlap either
    s = []
    for _ in range(random.randint(min_length, max_length)):
        letter = chr([A_ascii, C_ascii, G_ascii, T_ascii][random.randint(0, 3)])
        s.append(letter)
    return ''.join(s)

def swap_random_letter(word):
    random_index = random.randint(0, len(word) - 1)
    swapped_letter = chr([A_ascii, C_ascii, G_ascii, T_ascii][random.randint(0, 3)])
    word = list(word)
    word[random_index] = swapped_letter
    return ''.join(word)


def create_data_structures():
    """
    creates 100k random words, and uses those words to create 
    3 lists, 3 sets, and 3 TSTs of different sizes. It will also
    return some of the words that are in each data structure.

    The purpose is to test their speed and size.
    """
    tst1k = TST()
    tst10k = TST()
    tst100k = TST()

    list1k = []
    list10k = []
    list100k = []

    set1k = set()
    set10k = set()
    set100k = set()

    words_to_search_for = []
    words_generated = [] # used so we have common sequences (overlap)

    for i in range(1000):
        # 50% of the time we will use a word already in the dict, but slighty modified to ensure there is some overlap
        if i % 2 == 0 and i > 0:
            random_existing_word = random.sample(words_generated, 1)[0]
            word = swap_random_letter(random_existing_word)
        else:
            word = generate_random_word()
        words_generated.append(word)
        tst1k.put(word, i)
        tst10k.put(word, i)
        tst100k.put(word, i)
        list1k.append(word)
        list10k.append(word)
        list100k.append(word)
        set1k.add(word)
        set10k.add(word)
        set100k.add(word)

        # we know that these 50 words will be in all of the data structures
        if i % 20 == 0:
            words_to_search_for.append(word)

    for i in range(1000, 10000):
        word = generate_random_word()
        tst10k.put(word, i)
        tst100k.put(word, i)
        list10k.append(word)
        list100k.append(word)
        set10k.add(word)
        set100k.add(word)
    
    for i in range(10000, 100000):
        word = generate_random_word()
        tst100k.put(word, i)
        list100k.append(word)
        set100k.add(word)
    
    return (
        tst1k,
        tst10k,
        tst100k,
        list1k,
        list10k,
        list100k,
        set1k,
        set10k,
        set100k,
        words_to_search_for
    )

def getsize(obj):
    """
    sum size of object & members.
    
    copied from:
    https://stackoverflow.com/a/30316760/5042916
    """
    # Custom objects know their class.
    # Function objects seem to know way too much, including modules.
    # Exclude modules as well.
    BLACKLIST = type, ModuleType, FunctionType
    if isinstance(obj, BLACKLIST):
        raise TypeError('getsize() does not take argument of type: '+ str(type(obj)))
    seen_ids = set()
    size = 0
    objects = [obj]
    while objects:
        need_referents = []
        for obj in objects:
            if not isinstance(obj, BLACKLIST) and id(obj) not in seen_ids:
                seen_ids.add(id(obj))
                size += sys.getsizeof(obj)
                need_referents.append(obj)
        objects = get_referents(*need_referents)
    return size

def graph_space_used():
    (
        tst1k,
        tst10k,
        tst100k,
        list1k,
        list10k,
        list100k,
        set1k,
        set10k,
        set100k,
        words_to_search_for
    ) = create_data_structures()
    objs = {
        'tst1k': {'obj': tst1k},
        'tst10k': {'obj': tst10k},
        'tst100k': {'obj': tst100k},
        'list1k': {'obj': list1k},
        'list10k': {'obj': list10k},
        'list100k': {'obj': list100k},
        'set1k': {'obj': set1k},
        'set10k': {'obj': set10k},
        'set100k': {'obj': set100k},
    }
    for k, v in objs.items():
        v['size'] = getsize(v['obj'])
    fig, ax = plt.subplots()
    ax.set(
        title='Memory Usage',
        ylabel='Size in MB',
    )
    width = 0.25  # the width of the bars
    for i, (label, item) in enumerate(objs.items()):
        ax.bar(i, item['size'], width, label=label)
    ax.legend(loc='upper left', ncols=3)
    plt.show()


def time_tst_insert(tst, words):
    start_time = time()
    for word in words:
        tst.get(word)
    return time() - start_time

def time_list_insert(list_ds, words):
    start_time = time()
    for word in words:
        word in list_ds
    return time() - start_time


def time_set_insert(set_ds, words):
    start_time = time()
    for word in words:
        word in set_ds
    return time() - start_time


def graph_insert_speeds():
    (
        tst1k,
        tst10k,
        tst100k,
        list1k,
        list10k,
        list100k,
        set1k,
        set10k,
        set100k,
        words_to_search_for
    ) = create_data_structures()

    # generate 1000 words to insert into the data structures
    words_to_insert = [generate_random_word() for _ in range(1000)]

    objs = {
        'tst1k': {'obj': tst1k},
        'tst10k': {'obj': tst10k},
        'tst100k': {'obj': tst100k},
        'list1k': {'obj': list1k},
        'list10k': {'obj': list10k},
        'list100k': {'obj': list100k},
        'set1k': {'obj': set1k},
        'set10k': {'obj': set10k},
        'set100k': {'obj': set100k},
    }    

    for k in ['tst1k', 'tst10k', 'tst100k']:
        objs[k]['time'] = time_tst_insert(objs[k]['obj'], words_to_insert)
    
    for k in ['list1k', 'list10k', 'list100k']:
        objs[k]['time'] = time_list_insert(objs[k]['obj'], words_to_insert)

    for k in ['set1k', 'set10k', 'set100k']:
        objs[k]['time'] = time_set_insert(objs[k]['obj'], words_to_insert)

    fig, ax = plt.subplots()
    ax.set(
        title='Insert Times',
        ylabel='Time in Seconds',
    )
    width = 0.25  # the width of the bars
    for i, (label, item) in enumerate(objs.items()):
        ax.bar(i, item['time'], width, label=label)
    ax.legend(loc='upper left', ncols=3)
    plt.show()


def time_tst_search(tst, search_words):
    start_time = time()
    for word in search_words:
        tst.get(word)
    return time() - start_time

def time_list_search(list_ds, search_words):
    start_time = time()
    for word in search_words:
        word in list_ds
    return time() - start_time


def time_set_search(set_ds, search_words):
    start_time = time()
    for word in search_words:
        word in set_ds
    return time() - start_time


def graph_search_speeds():
    (
        tst1k,
        tst10k,
        tst100k,
        list1k,
        list10k,
        list100k,
        set1k,
        set10k,
        set100k,
        words_to_search_for
    ) = create_data_structures()

    for i in range(50):
        # generate 50 words that probably are misses (wont be in the data structures)
        words_to_search_for.append(generate_random_word())

    objs = {
        'tst1k': {'obj': tst1k},
        'tst10k': {'obj': tst10k},
        'tst100k': {'obj': tst100k},
        'list1k': {'obj': list1k},
        'list10k': {'obj': list10k},
        'list100k': {'obj': list100k},
        'set1k': {'obj': set1k},
        'set10k': {'obj': set10k},
        'set100k': {'obj': set100k},
    }    

    for k in ['tst1k', 'tst10k', 'tst100k']:
        objs[k]['time'] = time_tst_search(objs[k]['obj'], words_to_search_for)
    
    for k in ['list1k', 'list10k', 'list100k']:
        objs[k]['time'] = time_list_search(objs[k]['obj'], words_to_search_for)

    for k in ['set1k', 'set10k', 'set100k']:
        objs[k]['time'] = time_set_search(objs[k]['obj'], words_to_search_for)

    fig, ax = plt.subplots()
    ax.set(
        title='Search Times',
        ylabel='Time in Seconds',
    )
    width = 0.25  # the width of the bars
    for i, (label, item) in enumerate(objs.items()):
        ax.bar(i, item['time'], width, label=label)
    ax.legend(loc='upper left', ncols=3)
    plt.show()


if __name__ == '__main__':
    # graph_insert_speeds()
    # graph_search_speeds()
    graph_space_used()