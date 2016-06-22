# 学习Scrapy的过程记录，同时练习git的使用
练习项目，学习Scrapy同时练习Git的命令。
##Scrapy安装遇到的问题（centOS阿里云主机环境）
1. **首先提示lxml安装失败，stackoverflow中找到解决方案，利用yum安装了可能确实的组件：**</br>`sudo yum install -y gcc ruby-devel libxml2 libxml2-devel libxslt libxslt-devel`
2. **然后再次安装cryptography失败，提示No package ‘libffi’ found**</br>参照博客园《安装python爬虫scrapy踩过的那些坑和编程外的思考》中解决方案并未成功，配置PKG\_CONFIG\_PATH，仍未成功，利用whereis搜索libffi.so库时候未找到任何信息。此时应该是libffi安装没有成功，查找了一下yum安装的方法，利用yum安装后提示仍然缺失libffi.so.6，因为yum安装版本不同，安装的版本为libffi.so.5版本。所以此时libffi官网参照安装命令安装成功：`http://www.linuxfromscratch.org/blfs/view/svn/general/libffi.html`，成功之后设置LD_LIBRARY_PATH后成功安装cryptography；此时scrapy安装成功；
3. **另外一个问题是scarpy的xpath selector选择chrome或者xpath helper产生的xpath无法获取到节点:**</br>最终发现chrome在table的结构中会添加节点，tbody，这样产生的xpath和直接下载到的html的xpath存在不同，所以存在拿不到节点问题；目前没有好的解决办法，手动编写xpath，尽量使用相对路径；(后面投靠正则表达式阵营)
