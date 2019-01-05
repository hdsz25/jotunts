from PIL import Image,ImageDraw,ImageFont
import random
from django.http import HttpResponse
def verifycode(request):
    # 定义变量用于画面背景色，宽，高
    bgcolor=(random.randrange(20,100),random.randrange(20,100),random.randrange(20,100))
    width=50
    height=25
    # 创建画面对象
    im=Image.new('RGB',(width,height),bgcolor)
    # 创建画笔对象
    draw=ImageDraw.Draw(im)
#     调用画笔的point()函数绘制噪点
    for i in range(0,100):
        xy=(random.randrange(0,width),random.randrange(0,height))
        fill=(random.randrange(0,255),255,random.randrange(0,255))
        draw.point(xy,fill=fill)
#     定义验证码的备选值
#    str='0123456789qazwsxedcrfvtgbyhnujmikolp'
    str='0123456789'
#     随机选取4个作为验证码
    rand_str=''
    for i in range(0,4):
        rand_str+=str[random.randrange(0,len(str))]
    # 构造字体对象
    font=ImageFont.truetype(r'C:\Boot\Fonts\malgunn_boot.ttf',20)
    # 构造字体颜色
    fontcolor=(255,random.randrange(0,255),random.randrange(0,255))
    # 绘制4个字母
    draw.text((5,1),rand_str[0],font=font,fill=fontcolor)
    draw.text((15, 1), rand_str[1], font=font, fill=fontcolor)
    draw.text((25, 1), rand_str[2], font=font, fill=fontcolor)
    draw.text((35, 1), rand_str[3], font=font, fill=fontcolor)
    # 释放画笔
    del draw
#     存入session
    request.session['verifycode']=rand_str
# 内存文件操作
    import io
    buf=io.BytesIO()
#     将图像存入内存中，类型为png
    im.save(buf,'png')
#     将内存中的图片数据返回给客户端MIME类型为png
    return HttpResponse(buf.getvalue(),'image/png')

