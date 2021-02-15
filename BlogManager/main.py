import os
import re
import codecs
import requests
import time

img_dir = '..\\images'
blog_dir = '..\\blogs'
if __name__ == '__main__':
    print("图片归类开始")
    init_time = time.strftime("%Y-%m-%d, %H:%M:%S", time.localtime())
    print('当前时间' + init_time)
    isExists = os.path.exists(img_dir)
    if not isExists:
        os.makedirs(img_dir)
        print('create ' + img_dir)
    isExists = os.path.exists(blog_dir)
    if not isExists:
        print('create ' + blog_dir)
        os.makedirs(blog_dir)

    list = os.listdir(blog_dir)  # 列出文件夹下所有的目录与文件
    print('共发现%d个文件\n' % len(list))
    for i in range(0, len(list)):
        path = os.path.join(blog_dir, list[i])
        # if os.path.isfile(path):
        # # 你想对文件的操作
        print('路径为  ：' + path)

        input_file = codecs.open(path, mode="r", encoding="utf-8")
        text = input_file.read()
        # print(text)
        ex = 'blogs\\\\.*?md'
        title = re.findall(ex, path, re.DOTALL)
        print(title)
        title = title[0]
        title = title[6:title.index('.')]
        print(title)
        ex = '\[.*?]\(http.*?[" )]'
        lists = re.findall(ex, text)
        print(lists)
        input_file.close()
        for i, l in enumerate(lists):
            lists[i] = l[l.index('(') + 1:len(l) - 1]
        print(lists)
        isExists = os.path.exists(img_dir + '\\' + title)
        if not isExists:
            print('create ' + img_dir + '\\' + title)
            os.makedirs(img_dir + '\\' + title)
        img_root_dir = img_dir + '\\' + title
        print('正在下载图片')
        for u, url in enumerate(lists):
            print('第%d张' % u)
            time.sleep(0.1)
            img_data = requests.get(url=url).content
            with open(img_root_dir + '\\%d.png' % u, 'wb') as fp:
                fp.write(img_data)
                fp.close()
        print('下载完成')
        # with open(img_dir+'\\'+)
#  print('此文章不存在')
#         init_time = time.strftime("%B %d, %Y", time.localtime())
# with open(dirPath + '/' + summary_txt_file, 'w') as fp:
#     fp.writelines([file_name + '\n', summary_paragraph, init_time])
#     fp.close()
