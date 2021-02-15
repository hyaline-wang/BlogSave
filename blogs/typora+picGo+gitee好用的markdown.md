# typora+picGo+gitee = 好用的markdown

## 目录

[TOC]

## 软件下载及安装

### typora

[Typora](https://www.typora.io/)是一款优雅的markdown编辑器，所见即所得的编辑方式让我爱不释手，也推荐给大家。

> 链接：https://pan.baidu.com/s/1btVW8sH99DGlP7F6KZnvLQ 
> 提取码：hy8m 

### picgo

[PicGo](https://github.com/Molunerfinn/PicGo/releases)实现自动上传图片并返回markdown格式的图片url，这是自动上传的，也就是在Typora中插入图片就自动帮你上传替换图片的url，对于我们用户是透明的，十分舒服。

> 链接：https://pan.baidu.com/s/1xmB6j6YtycNGbdrwbdqHSA 
> 提取码：3ja5 

### gitee

[Gitee](https://gitee.com/)是国内版的Github，功能跟Github基本一样，主要是在国内访问非常快，作为图床和笔记文件存放仓库非常合适

### Node.js

在gicgo中下载gitee插件时会用到，不安会报错

> 链接：https://pan.baidu.com/s/1WmBXZmJNW5FLIIbZtQNcQg 
> 提取码：rqkb 



### 安装

安装十分简单，要注意的是picgo的路径一会用的到

## 配置步骤

### 在 gitee 上创建一个仓库来当图床

1.注册 gitee 账号并创建一个仓库当图床，这里仓库名起了img（我用的是img-save）

![image-20200413213232234](https://gitee.com/wangdaochuan/img-save/raw/master/img/20210203182941.png)

2.**生成私人令牌**

进入设置，如下图，（生成的令牌注意保存）

![image-20200413214032380](https://gitee.com/windows_xp_xp/picture_bed/raw/master/img/image-20200413214032380.png)

![image-20200413214138068](https://gitee.com/windows_xp_xp/picture_bed/raw/master/img/image-20200413214138068.png)

![image-20210203182158683](https://gitee.com/wangdaochuan/img-save/raw/master//img/20210203182158.png)

**（注：令牌只会显示一次，如果不复制的话，就只能重新修改令牌，步骤：修改 --> 重新生成令牌）**

### Picgo的配置

1. 打开picgo（可能打开后没看到界面，看看右下角有没有picgo图标），之后如下所示安装插件，有两个，安装第一个

![image-20210203174720719](https://gitee.com/wangdaochuan/img-save/raw/master/img/image-20210203174720719.png)

2. 安装完之后 点击**图床设置-> gitee图床**进行对应配置：

![image-20210203175613759](https://gitee.com/wangdaochuan/img-save/raw/master/img/image-20210203175613759.png)

要填的内容含义如下所示

![image-20210203180156508](https://gitee.com/wangdaochuan/img-save/raw/master//img/20210203182813.png)

我这里在在根目录下专门建了一个文件夹（img）用来存图片因此我的设置如下所示![image-20210203183456011](https://gitee.com/wangdaochuan/img-save/raw/master/img/20210203183456.png)

![image-20210203183117657](https://gitee.com/wangdaochuan/img-save/raw/master/img/20210203183117.png)

3. 最后注意设置一下时间戳重命名，不然遇到相同的图片名会很尴尬（上传失败）

![image-20210203181821254](https://gitee.com/wangdaochuan/img-save/raw/master/img/20210203183558.png)

### typora配置

1. 在typora中点击 **文件->偏好设置** ,进行如下图所示设置完成后注意验证能否上传



![image-20210203180834744](https://gitee.com/wangdaochuan/img-save/raw/master//img/image-20210203180834744.png)



![image-20210203181947750](https://gitee.com/wangdaochuan/img-save/raw/master//img/20210203181947.png)

上传过程和上传成功后会有提示

![image-20210203181958743](https://gitee.com/wangdaochuan/img-save/raw/master//img/20210203181958.png)

![image-20210203182010277](https://gitee.com/wangdaochuan/img-save/raw/master//img/20210203182010.png)

此时你的typora就可以自动上传了