## `Android`逆向

#### ---- `easy` ----
```
1. 直接对 *.so 库查找字符串
2. 用apktool, jd-gui, dex2jar对apk进行反编译
3. 反编译失败时可以对xml文件进行检查[010 EDITOR]是否有篡改痕迹
4. 反编译后查看是否有可疑字符串
    - ./AndroidManifest.xml
    - ./res/layout/activity_main.xml
    - ./res/value/strings.xml
    - ./[...]
5. 
```

#### ---- `difficult` ----
```
1. 
```


## `python [*.pyc]`
```sh
git clone https://github.com/wibiti/uncompyle2.git
# or
pip install uncompyle
```