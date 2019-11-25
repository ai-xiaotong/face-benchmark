# -*- coding:utf-8 -*-
import base64
import numpy as np


def b64encode_image(path):
    with open(path, 'rb') as f:
        return base64.b64encode(f.read())


def roc(gts, scores, start=0.10, stop=0.60, step=0.001):
    FARs, TARs, THs = [], [], []
    for TH in np.arange(start, stop, step):
        # FA, FN, TA, TN = 0, 0, 0, 0
        # FA: Number of different ID pair score > TH, FN: Different ID number
        # TA: Number of same ID pair score > TH, TN: Same ID number
        FA = np.count_nonzero((scores > TH) & ~gts.astype(np.bool))
        TA = np.count_nonzero((scores > TH) & gts.astype(np.bool))
        FN = np.count_nonzero(~gts.astype(np.bool))
        TN = np.count_nonzero(gts.astype(np.bool))

        if FN == 0 or TN == 0:
            continue

        FAR = FA/FN
        TAR = TA/TN
        FARs.append(FAR)
        TARs.append(TAR)
        THs.append(TH)

    return FARs, TARs, THs


def find_TAR_and_TH_by_FAR(FARs, TARs, THs, target_FAR=1.e-4):
    FARs = np.array(FARs)
    TARs = np.array(TARs)
    idx = np.argwhere(FARs <= target_FAR).reshape(-1)[0]
    return FARs[idx], TARs[idx], THs[idx]