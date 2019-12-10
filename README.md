[English](https://github.com/ai-xiaotong/face-benchmark) | [中文简体](https://github.com/ai-xiaotong/face-benchmark/blob/master/README_CN.md)
# Face Benchmark For famous open APIs

This repository aims at evaluating face-verification's performance
 of famous open APIs.

## Prerequisites

- To evaluate Alibaba API, you must have an Alibaba Cloud account as well as an AccessKey.
- To evaluate Tencent API, you must have an Tencent Cloud account as well as an AccessKey.
- To evaluate Aixiaotong API, you must have an Aixiaotong account as well as an AccessKey.
- Only support Python3.x.

## Installation

```
pip install requirements.txt
git clone https://github.com/ai-xiaotong/aixiaotong-python-sdk.git
cd aixiaotong-python-sdk && pip install .
```

## Usage

1. Replace your `ak_id` and `ak_secret` in `config.py`.
2. Replace `pairs.csv`. Each line follows format as `<ImagePath0>:<ImagePath1>,<Label>`.
3. Generate the score csv.
```
python3 run_aliyun_face_benchmark.py
python3 run_tencentclound_face_benchmark.py
python3 run_aixiaotong_face_benchmark.py
```
4. Plot ROC curve.
```
python3 run_evaluation.py aliyun-score.csv tencentcloud-score.csv aixiaotong-score.csv
```
