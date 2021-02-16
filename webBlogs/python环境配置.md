# python环境配置
## 目录

[TOC]

## pycharm +conda配置

1. 开始前请确认自己已经安装了 pycharm +anaconda

2. 首先在桌面创建一个文件夹“conda test”，进入这个文件夹，右键点击open floder as py.......![image-20210123171806309](https://github.com/ChasingTheDreamOfLoad/BlogSave/blob/main/images/0.png)

   即可打开pycharm ，若不习惯英文，可先汉化 pycharm （[右键+点此跳转至汉化](#chinese)）

3. 首先在pycharm中打开终端(其实cmd 或者 power shell 也行，只要能输命令行)

   ![image-20210123160945727](https://github.com/ChasingTheDreamOfLoad/BlogSave/blob/main/images/1.png)

4. 在终端中输入 conda create -n py3.6 python=3.6  （大致含义为   conda 创建 环境 名称“py3.6” Python版本=3.6，具体含义可通过conda create -h 查看）回车

   ![image-20210123161144078](https://github.com/ChasingTheDreamOfLoad/BlogSave/blob/main/images/2.png)

5. 等待如图所示界面，输入 y 回车，并等待下载完成

   ![image-20210123161232898](https://github.com/ChasingTheDreamOfLoad/BlogSave/blob/main/images/3.png)

   

6. 结束后出现如下图所示界面，#部分写了，要进入这个环境 conda activate py3.6 ，要退出一个环境用 conda deactivate

   ![image-20210123163036742](https://github.com/ChasingTheDreamOfLoad/BlogSave/blob/main/images/4.png)

7. 使用 conda activate py3.6进入刚刚创建的环境，若看到如图中所示的（py3.6）字样

   ![image-20210123163102059](https://github.com/ChasingTheDreamOfLoad/BlogSave/blob/main/images/5.png)

8. 测试安装numpy 若下载速度过慢，可更换国内源，[右键+点此跳转至pip换源](#pip)   

   ![image-20210123163947340](https://github.com/ChasingTheDreamOfLoad/BlogSave/blob/main/images/6.png)

9. 现在正式开始pycharm的配置，如下图所示进入设置

   ![image-20210123160550347](https://github.com/ChasingTheDreamOfLoad/BlogSave/blob/main/images/7.png)

10. 如下图所示，找到下图所示界面，此时并没有python解释器可以用![image-20210123160643093](https://github.com/ChasingTheDreamOfLoad/BlogSave/blob/main/images/8.png)

11. 点击下图所示界面 ->添加

    ![img](https://github.com/ChasingTheDreamOfLoad/BlogSave/blob/main/images/9.png)

    

12. 选择conda环境->现有环境，现在看到如下图所示界面，寻找刚刚创建的环境需要一些时间

    ![image-20210123170708775](https://github.com/ChasingTheDreamOfLoad/BlogSave/blob/main/images/10.png)

13. 当寻找到环境后可看到如下图所示界面，（路径可能略有不同）点击确定

    ![image-20210123170728760](https://github.com/ChasingTheDreamOfLoad/BlogSave/blob/main/images/11.png)

14. 再次确定，即可回到主界面

    ![image-20210123170757573](https://github.com/ChasingTheDreamOfLoad/BlogSave/blob/main/images/12.png)

## <span id="chinese">pycharm 汉化</span>

1.部分来自网络，在pycharm中点击file->settings，得到如下所示画面，按图中步骤操作（不要第5步）

![最新PyCharm从安装到PyCharm永久激活再到PyCharm官方中文汉化详细教程](https://github.com/ChasingTheDreamOfLoad/BlogSave/blob/main/images/13.png)

安装完成后如下图所示 restart 即可

![最新PyCharm从安装到PyCharm永久激活再到PyCharm官方中文汉化详细教程](https://github.com/ChasingTheDreamOfLoad/BlogSave/blob/main/images/14.png)

效果如下所示

![image-20210123160329193](https://github.com/ChasingTheDreamOfLoad/BlogSave/blob/main/images/15.png)

## <span id="pip">pip换源</span>

由于墙的原因，pip下载速度奇慢，可以换用国内镜像源如下，
当然除此之外你也可以通过翻墙解决，如果你已经翻了墙，但是pip还是很慢请点此


### linux: 

修改 ~/.pip/pip.conf (没有就创建一个)， 内容如下：

```
[global]
index-url = https://pypi.tuna.tsinghua.edu.cn/simple
```

### windows:

直接在user目录中创建一个pip目录，如：C:\Users\xx\pip，在pip 目录下新建文件pip.ini，内容如下

```
[global]
timeout = 6000
index-url = https://pypi.tuna.tsinghua.edu.cn/simple
trusted-host = pypi.tuna.tsinghua.edu.cn
```


## conda 常用语法
安装完anaconda后就可以使用conda的命令了，anaconda在windows下有图形化界面，但是没人用。 
```
#创建环境
conda create -n environment-name python= python-vision
#进入环境
conda activate environment-name
#退出环境
conda deactivate
#查看已有环境
conda info -e 
```

## requirements.txt 的使用
很多 Python 项目中经常会包含一个 requirements.txt 文件，里面内容是项目的依赖包及其对应版本号的信息列表，
即项目依赖关系清单，其作用是用来重新构建项目所需要的运行环境依赖。

他的作用不仅仅是看而已，通过简单的命令即可以 直接完成requirements 所需环境的安装。 当然requirements生成也是一步完成的。

注意requirements生成是列出当前环境所有的依赖，最好


```shell
#requirements.txt 的安装
pip install -r requirements.txt
#requirements.txt 生成
pip freeze > requirements.txt
```
## 翻墙后pip还是很慢
### （文不对题等搬家）~~虚拟机翻墙，常见翻墙方式有VPN和shadowsocks~~

#### 如果你的翻墙方式是shadowsocks
1. 在宿主机windows上运行shadowsocks.exe并勾选“允许局域网连接”（ALLOW LAN ， LAN就是局域网的意思）
2. 使用桥接方式运行虚拟机（这时虚拟机与宿主处于同一个局域网）
进入linux系统，System Settings – Network – Network proxy勾选Manual（手动）,地址全部填宿主机IP（局域网网段），设置好代理端口（可在windows下的shadowsocks查看，一般为默认1080）
4. linux 用浏览器访问www.google.com，成功
### shell 翻墙
方法一：（推荐使用）

> 为什么说这个方法推荐使用呢？因为他只作用于当前终端中，不会影响环境，而且命令比较简单
在终端中直接运行：

```
export http_proxy=http://proxyAddress:port
```

如果你是SSR,并且走的http的代理端口是12333，想执行wget或者curl来下载国外的东西，可以使用如下命令：

```
export http_proxy=http://127.0.0.1:12333
```
如果是https那么就经过如下命令：
```
export https_proxy=http://127.0.0.1:12333
```
除此之外的方法请参考
https://zhuanlan.zhihu.com/p/46973701