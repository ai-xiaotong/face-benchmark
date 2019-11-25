# Face Benchmark For famous open APIs

This repository aims at evaluating face-verification's performance
 of famous open APIs.

## Prerequisites

- To evaluate Alibaba API, you must have an Alibaba Cloud account as well as an AccessKey.
- To evaluate Tencent API, you must have an Tencent Cloud account as well as an AccessKey.
- Only support Python3.x.

## Installation

```
pip install requirements.txt
```

## Usage

1. Replace your `ak_id` and `ak_secret` in `config.py`.
2. Replace `pairs.csv`. Each line follows format as `<ImagePath0>:<ImagePath1>,<Label>`.
3. Generate the score csv.
```
python3 run_aliyun_face_benchmark.py
python3 run_tencentclound_face_benchmark.py
```
4. Plot ROC curve.
```
python3 run_evaluation.py aliyun-score.csv tencentcloud-score.csv
```
