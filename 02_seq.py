kuangcheng = ['kuangcheng', 28]
dongfengyu = ['dongfengyu', 31];
we = [kuangcheng, dongfengyu]
print we


#2 ����
greeting = 'hello'
print greeting[0]

#3 ��Ƭ��ð���������������ʵ��
name = 'kuangcheng'
print name[0:5]
number = [1,2,3,4,5,6,7,8,9]
print number[-3:-1]
print number[-3:]
print number[0:-1];

#����2
print number[::2];
#����Ϊ���������������ȡ
print number[1:-1:2];


#
print "print*************"
sentence = 'kuangheeng' #raw_input("Sentence:")
screen_width = 80
text_width = len(sentence)
box_width = text_width+6
left_margin = (screen_width - box_width)//2

print
print ' ' * left_margin + '+' + '-' * (box_width-2) + '+'
print ' ' * left_margin + '|' + ' ' * text_width + '|'
print ' ' * left_margin + '|' +  sentence + '|'
print ' ' * left_margin + '|' + ' ' * text_width + '|'
print ' ' * left_margin + '+' + '-' * (box_width-2) + '+'

# ��Ա���
users = ['kc', 'kc2', 'kc3']
print 'kc' in users #raw_input('Enpter your name:') in users

database = [
    ['kc', 'kc'],
    ['kc2', 'kc2'],
    ['kc3', 'kc3']
]
u = raw_input('name')
p = raw_input('password')
if [u, p] in database : print 'good'

# ���� ��� ��С
numbers = [100, 34, 678]
print len(numbers)
print max(numbers)
print min(numbers)
print min(9,10,11)



