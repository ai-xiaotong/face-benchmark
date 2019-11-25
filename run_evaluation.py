import os
from itertools import islice
import numpy as np
import argparse
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt

from helper import roc, find_TAR_and_TH_by_FAR


def get_roc(path, start=1., stop=100., step=0.1):
    batch_size = 1000
    scores, gts = [], []
    with open(path, 'r') as f:
        while True:
            next_n_lines = list(islice(f, batch_size))
            if not next_n_lines:
                break
            for line in next_n_lines:
                tokens = line.strip().split(',')
                score = float(tokens[1])
                pair = tokens[0].split(':')
                gt = pair[0].split('/')[-2] == pair[1].split('/')[-2]
                scores.append(score)
                gts.append(gt)

    scores = np.array(scores)
    gts = np.array(gts)
    FARs, TARs, THs = roc(gts, scores, start=start, stop=stop, step=step)
    return FARs, TARs, THs


def main(csv_list):
    platforms = [os.path.basename(csv.split('.')[0]) for csv in csv_list]
    for platform, csv_path in zip(platforms, csv_list):
        print(platform)
        FARs, TARs, THs = get_roc(csv_path, start=0., stop=100., step=0.1)
        far_2, tar_2, th_2 = find_TAR_and_TH_by_FAR(FARs, TARs, THs, target_FAR=1.e-2)
        print('FAR: {}, TAR: {}, TH: {}'.format(far_2, tar_2, th_2))
        far_3, tar_3, th_3 = find_TAR_and_TH_by_FAR(FARs, TARs, THs, target_FAR=1.e-3)
        print('FAR: {}, TAR: {}, TH: {}'.format(far_3, tar_3, th_3))
        far_4, tar_4, th_4 = find_TAR_and_TH_by_FAR(FARs, TARs, THs, target_FAR=1.e-4)
        print('FAR: {}, TAR: {}, TH: {}'.format(far_4, tar_4, th_4))
        # Plot ROC
        plt.plot(FARs, TARs)

    plt.title('Face verification ROC')
    plt.xscale('log')
    plt.xlabel('FAR')
    plt.ylabel('TAR')
    plt.legend([os.path.basename(csv.split('.')[0]) for csv in csv_list])
    plt.grid(True)
    plt.savefig('roc.png')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('score', nargs='+', help='score csv file path list', type=str)
    args = parser.parse_args()

    main(args.score)
