# Jupyter Notebook 环境

## 我需要的 Python package

我通常使用 Jupyter Notebook 进行数据分析、简单测试程序或者写一些演示。常用的包有：

数据科学

1. pandas（数据处理）
2. numpy（矩阵运算）
3. scipy（科学计算）
4. scikit-learn（机器学习）

数据可视化

1. matplotlib（最强的可视化工具）
2. seaborn（快速生成图）
3. plotly（动态图，绘制地图）

地理空间数据处理

1. geopandas

MySQL 数据库
1. pymysql

奇技淫巧

1. qgrid（notebook 插件，优雅地查看表格）
2. tqdm（进度条）

读写 Excel

1. openpyxl
2. xlrd

Notebook 相关

1. notebook
2. ipywidgets
3. jupyter_nbextensions_configurator
4. jupyter_contrib_nbextensions

## 安装

复制粘贴，修改环境名，回车，然后等着

```sh
envname="nbenv"
conda create -n $envname python=3.8 --yes
conda activate $envname
conda config --add channels conda-forge 
conda config --set channel_priority strict
conda install --yes numpy pandas scipy scikit-learn matplotlib seaborn plotly geopandas pymysql qgrid tqdm openpyxl xlrd notebook ipywidgets jupyter_nbextensions_configurator jupyter_contrib_nbextensions
python -m ipykernel install --name $envname
jupyter contrib nbextension install --user
jupyter nbextension enable --py --sys-prefix qgrid
```

## 插件

进入 notebook 后去打勾

1. AutoSaveTime，自动保存
2. Autoscroll，自动折叠
3. Codefolding，折叠代码
6. Collapsible Headings，折叠标题
7. datestamper，插入当前时间戳
8. Equation Auto Numbering，$\LaTeX$ 公式自动编号
9. ExecuteTime，记录cell运行时间戳和时间
10. Export Embedded HTML，允许导出嵌入图片的 html
11. Freeze，冻结 cell，禁止编辑
12. Hide Header，隐藏所有按钮
13. Hide input，隐藏一个 cell
14. Hide input all，隐藏所有 cell
15. highlighter，高亮字
16. Hinterland，自动补全
17. Skip-Traceback，把恼人的报错部分隐藏
18. Snippets，快速插入预设代码
19. Snippets Menu，超级无敌小抄
20. Table of Contents (2)，创建目录，生成html带上目录
21. Tree Filter，文件查找
22. Variable Inspector，变量查看器
23. zenmode，禅

## 修改字体

Windows 中 notebook 的默认字体太丑了，换成微软雅黑。Microsoft Edge 下载插件 Super Styles，添加代码

```css
#notebook-container * {
    font-family: Consolas, "微软雅黑"
}
```

## 常用命令

查看 jupyter kernel 都有哪些

```sh
jupyter kernelspec list
```

删除 jupyter kernel

```sh
kernel_name="delenv"
jupyter kernelspec remove $kernel_name
```

克隆环境

```sh
new_env_name="newenv"
old_env_name="oldenv"
conda create -n $env_name --clone $old_env_name
conda activate $env_name 
python -m ipykernel install --name $env_name 
```
