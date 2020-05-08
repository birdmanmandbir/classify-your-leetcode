# code-classify
用来整理leetcode刷题代码的小脚本

注释中定义代码所属的标签后，本程序会自动提取标签并将文件放入相应文件夹

如：

在`496.下一个更大元素-i.cpp`中定义标签`// @单调栈`， 程序会将此文件复制到`output_dir`中的`单调栈`
## 依赖
python3
## 配置参数：
```python
# 标签格式：// @
annotation = "// @"
programing_language = ".cpp"
# 输出目录，如果不存在会自动创建； 输出目录可以是输入目录的子目录，在输出目录下的文件会在处理过程中被忽略
output_dir = "/home/neil/Codes/classify-python/题型总结"
input_dir = "/home/neil/Codes/classify-python"
```