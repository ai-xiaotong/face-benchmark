# -*- coding:utf-8 -*-
from multiprocessing.dummy import Pool
from itertools import islice
import traceback

from aliyun_face_api import AliyunFaceApi
from config import ALIYUN_AK_ID, ALIYUN_AK_SECRET

batch_size = 1000
pool = Pool(5)


def verify_pair(pair):
    try:
        return AliyunFaceApi(ALIYUN_AK_ID, ALIYUN_AK_SECRET).verify(pair[0], pair[1])
    except Exception as e:
        traceback.print_exc()
        return None


def main():
    with open('pairs.csv', 'r') as fr, open('aliyun-score.csv', 'w') as fw:
        while True:
            next_n_lines = list(islice(fr, batch_size))
            if not next_n_lines:
                break
            pairs = [line.split(',')[0].split(':') for line in next_n_lines]
            scores = pool.map(verify_pair, pairs)
            for pair, score in zip(pairs, scores):
                fw.write('{}:{},{}\n'.format(pair[0], pair[1], score))


if __name__ == '__main__':
    main()