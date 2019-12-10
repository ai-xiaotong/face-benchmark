[English](https://github.com/ai-xiaotong/face-benchmark) | [中文简体](https://github.com/ai-xiaotong/face-benchmark/blob/master/README_CN.md)
# 开放接口人脸识别评估

 本仓库用于评估开放接口的人脸比对性能。

## 条件

- 评估阿里云接口时，需要先申请阿里云的AccessKey.
- 评估腾讯云接口时，需要先申请腾讯云的AccessKey.
- 评估爱小童接口时，需要先申请爱小童的AccessKey.
- 仅支持Python3.x.

## 安装

```
pip install requirements.txt
git clone https://github.com/ai-xiaotong/aixiaotong-python-sdk.git
cd aixiaotong-python-sdk && pip install .
```

## 使用

1. 替换`config.py`中的`ak_id`和`ak_secret`.
2. 替换`pairs.csv`. 每一行的格式为`<图像0>:<图像1>,<标签>`.
3. 生成得分
```
python3 run_aliyun_face_benchmark.py
python3 run_tencentclound_face_benchmark.py
python3 run_aixiaotong_face_benchmark.py
```
4. 绘制ROC曲线
```
python3 run_evaluation.py aliyun-score.csv tencentcloud-score.csv aixiaotong-score.csv
```
