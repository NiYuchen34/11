'''我的主页'''
import streamlit as st
from PIL import Image
# -*- coding: utf-8 -*-
page = st.sidebar.radio('我的首页', ['兴趣推荐', '图片处理工具', '智慧词典', '留言区', '话题辩论'])

def page_1():
    st.write('兴趣推荐。只有你爱看三体，我们就是同志了！')
    st.link_button('三体首页', 'https://www.threebody.com/')
    with open('永恒孤独.mp3','rb') as f:
        mymp3 = f.read()
    st.audio(mymp3, format='audio/mp3', start_time=0)
    st.image('ETO.jpg')
    st.write('欢迎来到三体。《三体》是刘慈欣创作的系列长篇科幻小说，由《三体·地球往事》《三体Ⅱ·黑暗森林》《三体Ⅲ·死神永生》组成。《三体·地球往事》在汪淼和史强的视角下探究物理学家自杀的原因，逐渐揭开文革中一些不为人知的秘密，彻底改变人类的命运甚至历史的走向……文明的序幕就此展开。')
def page_2():
    st.write(":sunglasses:图片换色小程序:sunglasses:")
    tab1,tab2,tab3,tab4=st.tabs(["原图", "换色1", "换色2", "换色3"])
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
            st.image(img_change(img, 1, 0, 2))
        with tab4:
            st.image(img_change(img, 2, 1, 0))
def page_3():
    st.write('智能词典')
    with open('words_space.txt','r',encoding='utf-8') as f:
        words_list = f.read().split('\n')
    for i in range(len(words_list)):
        words_list[i] = words_list[i].split('#')
    words_dict = {}
    for i in words_list:
        words_dict[i[1]] = [int(i[0]), i[2]]
    with open('check_out_times.txt', 'r', encoding='utf-8') as f:
        times_list = f.read().split('\n')
    for i in range(len(times_list)):
        times_list[i] = times_list[i].split('#')
    times_dict = {}
    for i in times_list:
        times_dict[int(i[0])] = int(i[1])
    word = st.text_input('请输入查询单词')
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
            message=message[:-1]
            f.write(message)
        st.write('查询次数：', times_dict[n])
        if word == 'balloon' or word == 'party':
            st.balloons()
        if word == 'snow' or word == 'winter':
            st.snow()
        if word == 'ETO':
            st.write('消灭人类暴政，世界属于三体！')
        if word == 'PDC':
            st.write('面壁计划')
        if word == 'PIA':
            st.write('只送大脑。')
        
def page_4():
    st.write('留言区，欢迎同志们参与讨论')
    # 从文件中加载内容，并处理成列表
    with open('leave_messages.txt', 'r', encoding='utf-8') as f:
        messages_list = f.read().split('\n')
    for i in range(len(messages_list)):
        messages_list[i] = messages_list[i].split('#')
    for i in messages_list:
        if i[1] == '同志(三体)':
            with st.chat_message('🌞'):
                st.write(i[1],':',i[2])
        elif i[1] == '其他人':
            with st.chat_message('🍥'):
                st.write(i[1],':',i[2])
    name = st.selectbox('我是……', ['同志(三体)', '其他人'])
    new_message = st.text_input('想要说的话……')
    if st.button('留言'):
        messages_list.append([str(int(messages_list[-1][0])+1), name, new_message])
        with open('leave_messages.txt', 'w', encoding='utf-8') as f:
            messages = ''
            for i in messages_list:
                messages += i[0] + '#' + i[1] + '#' + i[2] + '\n'
            messages = messages[:-1]
            f.write(messages)

def page_5():
    st.write('三体和哈利波特谁更厉害？')
    # 从文件中加载内容，并处理成列表
    with open('leave_messages1.txt', 'r', encoding='utf-8') as f:
        messages1_list = f.read().split('\n')
    for i in range(len(messages1_list)):
        messages1_list[i] = messages1_list[i].split('#')
    for i in messages1_list:
        if i[1] == '同志':
            with st.chat_message('🌞'):
                st.write(i[1],':',i[2])
        elif i[1] == '其他人':
            with st.chat_message('🍥'):
                st.write(i[1],':',i[2])
    name1 = st.selectbox('我是……', ['同志', '魔法方'])
    new_message1 = st.text_input('想要说的话……')
    if st.button('留言'):
        messages1_list.append([str(int(messages1_list[-1][0])+1), name1, new_message1])
        with open('leave_messages1.txt', 'w', encoding='utf-8') as f:
            messages1 = ''
            for i in messages1_list:
                messages1 += i[0] + '#' + i[1] + '#' + i[2] + '\n'
            messages1 = messages1[:-1]
            f.write(messages1)

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

if page == '兴趣推荐':
    page_1()
elif page == '图片处理工具':
    page_2()
elif page == '智慧词典':
    page_3()
elif page == '留言区':
    page_4()
elif page == '话题辩论':
    page_5()