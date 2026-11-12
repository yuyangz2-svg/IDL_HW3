# HW3P2 运行说明

## Colab 正式训练

1. 打开 Google Colab，上传 `HW3P2_Student_Starter_Notebook_F26.ipynb`。
2. 在「运行时 → 更改运行时类型」选择 GPU。
3. 从头执行。上传框出现时上传 `HW3P2_Colab_Bundle.zip`，按提示挂载 Google Drive。
4. 输入 W&B API Key，或提前建立 Colab Secret `WANDB_API_KEY` 并授权 notebook 读取。项目名已经设为 `HW3P2-F26`。
5. 等待数据下载、测试和第一个 epoch 完成。GitHub Token 不需要；公开数据下载失败时才会提示 Kaggle API Token。

默认 batch size 2，累积 8 次梯度，有效 batch size 16；1k tokenizer；encoder 4 层，decoder 3 层，d_model 256。
默认先跑 1 个 epoch，学习率计划为 20 个 epoch。要接着跑，在设置单元格修改 `EPOCHS_THIS_RUN`，执行该设置单元格，再执行第 6 节训练单元格。
更换模型超参数时请修改 `config_colab.yaml` 并使用新的 `RUN_NAME`。恢复已有 run 会采用它已保存的配置。

每轮完成后保存到 `MyDrive/HW3P2_runs/asr_1k_256_v1/`，包含 best/last checkpoint、配置、训练历史和归一化统计。
Colab 重启后重新上传文件并从头执行，会恢复到上一个完成的 epoch；中途未完成的 epoch 会重跑。
验证 CER 默认来自前 50 个 batch；最终推理前单独运行完整验证集。需要提高模型效果时，应根据训练曲线继续训练和调参。

「运行全部」在训练之后会显示预期的 `SystemExit`，防止自动执行耗时的最终推理和外部提交。继续训练不需要改这个开关。
完成正式训练后，按 notebook 第 7 节手动生成 `results.csv` 和作业提交包。
课程声明 `ACKNOWLEDGED` 由你阅读后填写。提交凭证在最终提交阶段输入，无需先发到聊天中。

## 本地小数据验证

建议使用 Python 3.12，在本目录执行：

```bash
python3.12 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements-local.txt
python run_local_smoke.py
```

该命令执行相同 notebook 的训练部分，使用附带数据和小模型，无需 GPU 或账号。
第二次执行会继续下一轮。默认 smoke 总计 2 轮；要重新测试，设置新的 `HW3P2_RUN_NAME` 环境变量再执行。
原始 `requirements.txt` 包含 CUDA 专用包，不用于 macOS 的这个验证入口。

本包没有完整训练数据、训练好的最终模型或账号凭证。完整训练必须等待 Colab 中的数据下载和训练完成。
