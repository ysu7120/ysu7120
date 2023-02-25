from insta.metadata import SEARCH_HASHTAG, DONG_PATH

import pandas as pd
import numpy as np
import re
from wordcloud import WordCloud
import matplotlib as mpl
import matplotlib.pyplot as plt
from collections import Counter
import seaborn as sns

def max_place(count_hashtag):
    try:
        # 가장 높은 값을 출력
        return max(count_hashtag, key=count_hashtag.get)
    except:
        return 'ERROR!'

# 그래프 이미지로 저장
def save_graph(save_path, count_hashtag, figsize=(15, 5), rotation=45, font='D2Coding'):
    mpl.rcParams['font.family'] = font

    df = pd.DataFrame.from_dict(count_hashtag, orient='index', columns=['counts'])
    df = df[df['counts'] > 1]
    fig, ax = plt.subplots(constrained_layout=True, figsize=figsize)
    g = sns.barplot(data=df,x=df.index, y=sum(list(df.values.tolist()), []), ax=ax)
    max_value = max(sum(list(df.values.tolist()), []))

    for p in g.patches:
        height = p.get_height()
        g.text(p.get_x() + p.get_width() / 2., height + .5, int(height), ha='center', size=12)


    g.set_title('장소로 확인한 해시태그', size=20)
    g.set_xlabel('해시태그', size=15)
    g.set_ylabel('횟수', size=15)
    g.set_ylim(.5, max_value + 3)
    plt.xticks(fontsize=12, rotation=rotation)
    plt.savefig(f'{save_path}{SEARCH_HASHTAG}_Graph.png', bbox_inches='tight')
    print(f'{save_path}{SEARCH_HASHTAG}_Graph.png 저장 완료!')

    return [k for k, v in count_hashtag.items() if v == max_value]

def save_wordcloud(save_path, count_hashtag):
    wc = WordCloud(font_path='~/Library/Fonts/D2Coding-Ver1.3.2-20180524-all.ttc', \
        width=1024, height=720, scale=2.0, max_font_size=250, background_color='white', \
        colormap = 'gist_earth')
    gen = wc.generate_from_frequencies(count_hashtag)
    wc.to_file(f'{save_path}{SEARCH_HASHTAG}_WordCloud.jpg')
    print(f'{save_path}{SEARCH_HASHTAG}_WordCloud.jpg 저장 완료!')

# 그래프와 워드클라우드 출력
def processing(save_path, csv_length):
    df_place = pd.read_csv(DONG_PATH, encoding='utf8', usecols=[1, 3])
    df_place_tolist = list(set(df_place['Unnamed: 4'].tolist() + df_place['Unnamed: 6'].tolist()))
    places = set([])

    # 전처리
    for _ in df_place_tolist:
        if len(_) != 2:
            place = re.sub("[0-9,.]", '', _[:-1])
            if len(place) > 1:
                places.add(place)
            else:
                place = re.sub("[0-9,.]", '', _)
                places.add(place + '동')
        else:
            places.add(_)
    places = sorted(list(places))

    # 태그 전처리
    df_hashtag = pd.read_csv(f'{save_path}/{csv_length} instagram_crawling.csv', encoding='utf8')
    list_hashtag = []
    for _ in df_hashtag['hashtag']:
        if len(_) != 2:
            list_hashtag.append(re.sub("[\[\],'#]", '', _).split())

    list_hashtag = sum(list_hashtag, [])

    final_process = []
    for hashtag in list_hashtag:
        for _ in places:
            if _ in hashtag:
                final_process.append(hashtag)
                break

    counter_hashtag = Counter(final_process)
    save_wordcloud(save_path, counter_hashtag)
    
    return save_graph(save_path, counter_hashtag)
