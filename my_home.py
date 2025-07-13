'''我的首页'''
import streamlit as st
from PIL import Image

page = st.sidebar.radio(
    '我的首页', ['我的兴趣推荐', '我的图片处理工具', '我的智能词典', '我的留言区', '来都来了填个问卷吧'])


def page_1():
    '''我的推荐'''
    tab1, tab2, tab3, tab4 = st.tabs(["爱豆推荐", "他是谁呢？", "音乐推荐", "视频推荐"])
    with tab1:
        st.image('1.png')
    with tab2:
        st.write('''蔡徐坤于 1998 年 8 月 2 日出生于浙江温州。他从小就对艺术表现出浓厚的兴趣和天赋，
                 在父母的支持下，开始接受各种艺术培训。13 岁时，他参加了中央电视台《开门大吉》节目录制，
                 展现出了一定的舞台表演能力。后来他前往美国留学，系统地学习音乐制作、舞蹈等专业知识，为日后的演艺事业打下了坚实基础。''')
    with tab3:
        with open('1.mp3','rb')as f:
            mymp3 = f.read()
        st.audio(mymp3,format='audio/mp3',start_time=0)
    with tab4:
        with open('1.mp4',"rb")as video_file:
            video =video_file.read()
        st.video(video)


def page_2():
    '''我的图片处理工具'''
    st.write(":sunglasses:图片换色小程序:sunglasses:")
    tab1, tab2, tab3, tab4 = st.tabs(["原图", "改色1", "改色2", "改色3"])
    uploaded_file = st.file_uploader("上传图片", type=['png', 'jpeg', 'jpg'])
    if uploaded_file:
        # 获取图片文件的名称、类型和大小
        file_name = uploaded_file.name
        file_type = uploaded_file.type
        file_size = uploaded_file.size
        img = Image.open(uploaded_file)
        with tab1:
            st.image(img)
        with tab2:
            st.image(img_change(img, 0, 2, 1))
        with tab3:
            st.image(img_change(img, 2, 0, 1))
        with tab4:
            st.image(img_change(img, 1, 2, 0))


def page_3():
    '''我的智能词典'''
    st.write('智能词典')
    # 从本地文件中将词典信息读取出来，并存储在列表中
    with open('words_space.txt', 'r', encoding='utf-8') as f:
        words_list = f.read().split('\n')
    # 将列表中的每一项内容再进行分割，分为“编号、单词、解释”
    for i in range(len(words_list)):
        words_list[i] = words_list[i].split('#')
    # 将列表中的内容导入字典，方便查询，格式为“单词：编号、解释”
    words_dict = {}
    for i in words_list:
        words_dict[i[1]] = [int(i[0]), i[2]]
    # 从本地文件中将单词的查询次数读取出来，并存储在列表中
    with open('check_out_times.txt', 'r', encoding='utf-8') as f:
        times_list = f.read().split('\n')
    # 将列表转为字典
    for i in range(len(times_list)):
        times_list[i] = times_list[i].split('#')
    times_dict = {}
    for i in times_list:
        times_dict[int(i[0])] = int(i[1])
    # 创建输入框
    word = st.text_input('请输入要查询的单词')
    # 显示查询内容
    if word in words_dict:
        st.write(words_dict[word])
        n = words_dict[word][0]
        if n in times_dict:
            times_dict[n] += 1
        else:
            times_dict[n] = 1
        with open('check_out_times.txt', 'w', encoding='utf-8') as f:
            message = ''
            for k, v in times_dict.items():
                message += str(k) + '#' + str(v) + '\n'
            message = message[:-1]
            f.write(message)
        st.write('查询次数：', times_dict[n])
        if word == 'python':
            st.code('''
                    # 恭喜你触发彩蛋，这是一行python代码
                    print('hello world')''')


def page_4():
    '''我的留言区'''
    st.write('我的留言区')
    # 从文件中加载内容，并处理成列表
    with open('leave_messages.txt', 'r', encoding='utf-8') as f:
        messages_list = f.read().split('\n')
    for i in range(len(messages_list)):
        messages_list[i] = messages_list[i].split('#')
    for i in messages_list:
        if i[1] == '阿短':
            with st.chat_message('🌞'):
                st.write(i[1], ':', i[2])
        elif i[1] == '编程猫':
            with st.chat_message('🍥'):
                st.write(i[1], ':', i[2])
    name = st.selectbox('我是……', ['阿短', '编程猫', ''])
    new_message = st.text_input('想要说的话……')
    if st.button('留言'):
        messages_list.append(
            [str(int(messages_list[-1][0])+1), name, new_message])
        with open('leave_messages.txt', 'w', encoding='utf-8') as f:
            message = ''
            for i in messages_list:
                message += i[0] + '#' + i[1] + '#' + i[2] + '\n'
            message = message[:-1]
            f.write(message)


def page_5():
    st.write("蔡徐坤曾在哪些综艺里有突出表现？")
    cb1 = st.checkbox("A.《青春有你》系列")
    cb2 = st.checkbox("B.《奔跑吧》某季") 
    cb3 = st.checkbox("C.《声入人心》") 
    cb4 = st.checkbox("D.《向往的生活》") 
    b1 = st.button('第1题答案')
    if b1:
        # 假设正确答案是 A、B 
        if cb1 and cb2 and not cb3 and not cb4:
            st.write('回答正确！')
        else:
            st.write('再想想')
    st.write("蔡徐坤粉丝的官方名称是？")
    cb11 = st.checkbox("A.ikun")
    cb22 = st.checkbox("B.小坤友") 
    cb33 = st.checkbox("C.蔡家人") 
    cb44 = st.checkbox("D.坤之队") 
    b2 = st.button('第2题答案')
    if b2:
        # 正确答案：A 
        if cb11 and not cb22 and not cb33 and not cb44:
            st.write('回答正确！')
        else:
            st.write('再想想，粉丝叫 ikun 呀~')


def img_change(img, rc, gc, bc):
    '''图片处理'''
    width, height = img.size
    img_array = img.load()
    for x in range(width):
        for y in range(height):
            # 获取RGB值
            r = img_array[x, y][rc]
            g = img_array[x, y][gc]
            b = img_array[x, y][bc]
            img_array[x, y] = (r, g, b)
    return img


if page == '我的兴趣推荐':
    page_1()
elif page == '我的图片处理工具':
    page_2()
elif page == '我的智能词典':
    page_3()
elif page == '我的留言区':
    page_4()
elif page == '来都来了填个问卷吧':
    page_5()
