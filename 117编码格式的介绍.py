#coding=gbk
# editor hc
# date: 2023/2/21 21:10

'''
�����ʽ�Ľ���
�ļ��Ķ�дԭ��
�ļ���д����
�ļ�����ĳ��õķ���
with��䣨�����Ĺ�������
Ŀ¼����
'''
print('hello China')
'''
pythonĬ�ϵı����ʽΪUTF-8
'''
#����޸ı����ʽ��ֻ�����ļ���ʼд '#coding = �����ʽ' ����'#coding:�����ʽ'
s = '���ڴ�֪��'
print(s.encode(encoding='GBK'))
# b'\xba\xa3\xc4\xda\xb4\xe6\xd6\xaa\xbc\xba'
bytes =  b'\xba\xa3\xc4\xda\xb4\xe6\xd6\xaa\xbc\xba'
print(bytes.decode(encoding='GBK'))
# ���ڴ�֪��
