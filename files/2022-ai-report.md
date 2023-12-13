# 人工智能站点聚类实验报告

## 运行环境与操作指令

### 运行环境

- 硬件信息
  - 显卡：RTX 3090
  - 显存：24GB
  - CPU型号：AMD EPYC 7642 48-Core Processor
  - CPU核心数：24核
  - 内存：80GB

- 操作系统：ubuntu20.04
- 运行镜像：Miniconda/conda3.8/cuda11.3
- 编辑器：JupyterLab
- 编程语言：Python 3.8.10
- 依赖包：[requirement.txt](源代码和输出文件/requirement.txt)

## 操作指令

### 依赖包安装

1. 实验所需硬件平台使用的是[AutoDL](https://www.autodl.com/)的硬件设备，其中镜像信息使用的是AutoDL的基础镜像
   ![image-20221217120227216](C:\Users\13287\AppData\Roaming\Typora\typora-user-images\image-20221217120227216.png)

2. 创建完主机实例后进入JupyterLab，安装依赖包
   因为之前已经进行过依赖包的安装，我们将所有依赖包的信息进行了导出

   ```cmd
   pip freeze > requirement.txt
   ```

   ![image-20221217120626369](C:\Users\13287\AppData\Roaming\Typora\typora-user-images\image-20221217120626369.png)
   之后在安装python依赖包时，可以直接使用以下指令直接进行安装

   ```cmd
   pip install -r requirement.txt
   ```
   
### JupyterLab 插件安装

为了能够显示代码的运行时间，需要安装一个JupyterLab插件jupyter-excute-time

1. 首先我们需要安装依赖项，npm和nodejs两个库

   ``` cmd
   pip install npm
   conda install -c conda-forge nodejs
   ```

2. 之后安装jupyter-excute-time插件

   ``` cmd
   pip install jupyterlab_execute_time
   ```

3. 最后在JupyterLab的设置中，打开笔记本一栏，勾选记录执行用时
   ![image-20221217124932341](C:\Users\13287\AppData\Roaming\Typora\typora-user-images\image-20221217124932341.png)

### 程序运行

1. 将[代码文件](源代码和输出文件/ai_lab.ipynb)用JupyterLab打开
   代码文件为压缩包中ai_lab.ipynb文件
   其中，导入lng.csv数据集的相对目录位置为`autodl-nas/lng2.csv`

   ![image-20221217125028069](C:\Users\13287\AppData\Roaming\Typora\typora-user-images\image-20221217125028069.png)

2. 依次执行单元格中的代码，得到的输出文件中
   `ai_lab_output_data`为中间过程分析文件
   
   - in_rate:船只进口比率
   - out_rate:船只出口比率
   - no_rate:船只停靠比率
   
   `final_data`为结果文件

## 代码运行截图

### 主要运行截图

- 数据预处理截图
  ![image-20221217130503935](C:\Users\13287\AppData\Roaming\Typora\typora-user-images\image-20221217130503935.png)

- 聚类算法运行截图
  ![image-20221217122233917](C:\Users\13287\AppData\Roaming\Typora\typora-user-images\image-20221217122233917.png)
  代码运行时长：8分31.34s
- 站点分析截图
  ![image-20221217130401746](C:\Users\13287\AppData\Roaming\Typora\typora-user-images\image-20221217130401746.png)
- 地图标点截图
  ![image-20221217130708879](C:\Users\13287\AppData\Roaming\Typora\typora-user-images\image-20221217130708879.png)

### 代码性能分析

- 最初我们选择使用的是sklearn的机器学习库，用于将数据进行聚类，但通过很多次试验和了解后我们发现，sklearn库对于大量数据的处理效果并不理想。这是由于sklearn无法支持GPU运算，仅支持CPU运算而导致的。而我们已有的硬件设备中，并没有理想的多核CPU集群运算条件，而sklearn又无法运用到比较优势的GPU硬件条件。通过测试，在计算一次聚类结果，通常需要花费20分钟左右。

  尝试解决：英特尔平台对于Scikit-learn 应用程序，有一个加速器库`sklearnex`，可以带来10-100倍的加速，我们在英特尔平台尝试了运用该库进行加速运算，但效果仍然不理想。

- 随后在通过查阅资料和了解后，我们找到Nvidia有一个专门用于机器学习的库，支持使用GPU进行运算
  `cuml`:接口与sklearn库提供的接口使用方法基本一直一致
  [cuml官方文档](https://docs.rapids.ai/api/cuml/stable/) 
  通过测试，在计算一次聚类结果，cuml使用GPU只需要花费5秒左右。

## 预处理和算法分析

整个流程可以主要分为三大部分，`数据预处理`，`站点聚类` , `站点类型分析`。

### 数据预处理

总共有`7896919`条数据

1. 吃水数据处理
   通过查询资料
   ![image-20221217133031569](C:\Users\13287\AppData\Roaming\Typora\typora-user-images\image-20221217133031569.png) 
   我们将吃水在5m~30m的船只进行保留，将其他不符合要求的船只数据进行删除
   ![image-20221217132742432](C:\Users\13287\AppData\Roaming\Typora\typora-user-images\image-20221217132742432.png)
   通过处理后，剩余`5400073`条数据

2. 船只航行状态处理
   通过查询AIS航行状态
   ![image-20221217132950785](C:\Users\13287\AppData\Roaming\Typora\typora-user-images\image-20221217132950785.png)
   我们认为状态1和状态5是停靠的状态，所以将不是状态1和状态5的数据进行清洗删除。
   ![image-20221217133151719](C:\Users\13287\AppData\Roaming\Typora\typora-user-images\image-20221217133151719.png)
   剩余`3578468`条数据

3. 在进行站点聚类的时候，用不到`航行状态`和`速度`这两个数据项，所以我们将这两个数据项进行了删除

   ![image-20221217133340885](C:\Users\13287\AppData\Roaming\Typora\typora-user-images\image-20221217133340885.png)
   **数据预处理完毕**

### 站点聚类

我们使用的聚类算法是`K-Means`算法，K-Means算法需要我们在初始的时候设定聚类的簇数，而聚类的簇数也是聚类是否准确的关键，所以我们需要确定一个合适的聚类簇数，因此我们需要评价聚类的好坏。

评估方法：`Inertia指标`：每个样本与其簇质心的距离的平方和

cuml中没有Inertia属性，但是有score方法，score为Inertia值的负数

![image-20221217160835976](C:\Users\13287\AppData\Roaming\Typora\typora-user-images\image-20221217160835976.png)

可以知道。簇数越多，指标肯定会越来越小。

我们首先设定一个大概的簇数区间，我们设定了150~210的簇数区间，每个簇数都聚类3次，目的是为了消除初始质心带来的偶然性，然后挑选聚类3次中最小的一次指标保存。

![image-20221217170311317](C:\Users\13287\AppData\Roaming\Typora\typora-user-images\image-20221217170311317.png)

下面我们根据Inertia指标画图，寻找最佳的簇数

画出150~210簇数区间中，单位为10的图像

![image-20221217170405634](C:\Users\13287\AppData\Roaming\Typora\typora-user-images\image-20221217170405634.png)
我们可以看到，190这个点为一个拐点。在190之前下降非常快，在190之后下降逐渐平缓，下降平缓则说明增加簇数带来的效果已经不明显。这说明簇数选择在190左右会比较合适，所以我们缩小范围和单位，继续寻找最佳的簇数。

画出175~200簇数区间中，单位为5的图像

![image-20221217170653307](C:\Users\13287\AppData\Roaming\Typora\typora-user-images\image-20221217170653307.png)

可以看到在185后面变化开始平缓，这说明簇数设置在185左右比较合适。我们进一步缩小范围。

画出180~190簇数区间中，单位为3的图像

![image-20221217170856483](C:\Users\13287\AppData\Roaming\Typora\typora-user-images\image-20221217170856483.png)

可以看到183时为一个拐点，后面的下降变得平缓，这说明簇数设置为183会比较合适。所以我们最终确定簇数为**183**。

即确定了聚类出183个站点，我们将簇的质心作为站点的经纬度坐标。

![image-20221217171241483](C:\Users\13287\AppData\Roaming\Typora\typora-user-images\image-20221217171241483.png)

通过将183个站点画到世界地图上，可以看到站点基本沿着海岸线，这说明聚类的效果比较好。

此时，聚类部分的工作已经完成，接下来要通过每个站点的船只数据进行对站点的分析。

### 站点类型分析

通过站点聚类，现在每条数据都有聚类出来的簇标签，即每条船只数据都有自己的站点编号。相反地，183个站点都有属于自己的船只数据。我们要通过这些船只数据，完成对于站点是否是LNG站点以及是否是进口站点的分析。

而这些要依靠船只数据中的吃水数据来分析出结果。

> 思路是：吃水变化有三种，减少、增加或不变，如果吃水减少则说明该船只在这个站点卸货了，吃水增加则说明该船只在这个站点装货，吃水若不变则说明该船只仅仅只是停靠在该站点。通过每个站点中所有船只的吃水变化，看是三种变化中的哪种变化最多，则可以分析出该站点的类型。
>
> 比如若是吃水不变最多，说明该站点不是LNG站点，而是被用作船只停靠。否则则说明其是LNG站点，是LNG站点后进一步比较吃水减少和吃水增多的船只数量，分析出其是进口站点还是出口站点。

![image-20221217172319396](C:\Users\13287\AppData\Roaming\Typora\typora-user-images\image-20221217172319396.png)

我们输出了中间文件，用比率来描述出了每个站点的三种变化船只。

![image-20221217172518878](C:\Users\13287\AppData\Roaming\Typora\typora-user-images\image-20221217172518878.png)

最终确定每个站点的类型。（划分规则在分析结果中）

![image-20221217172638628](C:\Users\13287\AppData\Roaming\Typora\typora-user-images\image-20221217172638628.png)

## 分析结果

[LNG站点分析聚类结果](源代码和输出文件/lng_results_list.json)

查看压缩包中lng_results_list.json文件

![image-20221217180604417](C:\Users\13287\AppData\Roaming\Typora\typora-user-images\image-20221217180604417.png)

### 划分规则

- 泊点：当站点中的停靠船只数量比率达到70%
- 出站：站点中装货船只数量比率大于入站船只比率
- 入站：站点中卸货船只数量比率大于入站船只比率

### 统计信息

![image-20221217181959603](C:\Users\13287\AppData\Roaming\Typora\typora-user-images\image-20221217181959603.png)

经过统计

- lng站点：129个
  - 进口站点：55个
  - 出口站点：74个
- 泊点：54个
