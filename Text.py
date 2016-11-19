import time
import calendar
import re
import datetime
# import inspect
#
# import sys
import json
import codecs

# from codecs import BOM_UTF8
#
# def lstrip_bom(str_, bom=BOM_UTF8):
#     if str_.startswith(bom):
#         return str_[len(bom):]
#     else:
#         return str_
#
# class Text:
#     "GFE text mapping"
#     def __init__(self):
#         pass
#
# print type(Text())
# print type(Text)
# print type("Hello")
# print type(Text).__name__
#
# text = Text()
# string = ("Hello", "a")
#
# print text.__class__.__name__
# print string.__class__.__name__
#
# print inspect.isclass(Text)
# print type(Text()) is Text
#
# def text_method(obj):
#     print obj.__class__.__name__
#
# text_method(text)
# text_method(string)
#
# print text.__class__.__name__ is "Texts"
#
# print sys.platform

# path = r"C:\Program Files (x86)\NVIDIA Corporation\NVIDIA GeForce Experience\www\l10n\preferences\en-US.json"
#
# print open(r"C:\Program Files (x86)\NVIDIA Corporation\NVIDIA GeForce Experience\www\l10n\preferences\en-US.json").read()
#
# json.loads(lstrip_bom(open('sample.json').read()))

time_str = "2016-10-14 11:14:40.525"
pattern = "\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{3}"
mo = re.match(pattern, time_str)
if mo is None:
    print "not matching"
else:
    print mo.group()

print str(int(time.time()))
print str(int(time.time()*1000))
print str(time.gmtime(time.time()))
print str(time.localtime(time.time()))
path = "C:\Users\cheng\AppData\Local\NVIDIA Corporation\NVIDIA GeForce Experience\CefCache\console.log"
console_log = open(path).read()
index = console_log.index("jsEvents batched response")

print [m.start() for m in re.finditer("jsEvents batched response", console_log)]

while index < len(console_log):
    if console_log[index] == '{':
        break
    index += 1

start_index = index

tmp_index = console_log[0:start_index].rfind('\n')
time_stamp = re.search(pattern, console_log[tmp_index : start_index]).group()
print time_stamp

print time_str
utc_time = time.strptime(time_str, "%Y-%m-%d %H:%M:%S.%f")
epoch_time = calendar.timegm(utc_time)
print epoch_time

print "UTC time: " + str(time.time())

struct_in_utc_strftime = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(time.time()))
print "struct time in UTC: " + struct_in_utc_strftime
struct_in_local_strftime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
print "struct time in local time: " + struct_in_local_strftime

print calendar.timegm(time.strptime(struct_in_utc_strftime, "%Y-%m-%d %H:%M:%S"))
print time.mktime(time.strptime(struct_in_local_strftime, "%Y-%m-%d %H:%M:%S"))

print "local time: " + str(calendar.timegm(time.localtime()))
print "epoch_time: " + str(epoch_time)
if epoch_time > calendar.timegm(time.localtime()):
    print "future"
else:
    print "history"

index += 1
count = 1
while count != 0 and index < len(console_log):
    if console_log[index] == '{':
        count += 1
    if console_log[index] == '}':
        count -= 1
    index += 1

end_index = index
if count == 0:
    print "found end_index"
else:
    print "end_index not found"

print console_log[start_index: end_index+1]

str_format = "%Y-%m-%d %H:%M:%S"
time_str = time.strftime(str_format, time.localtime())

time_str = "2016-10-16 13:26:30"

def get_local_time_str_to_epoch(str_format, time_str):
    print "transferring local time: " + time_str + "(" + str_format + ")" + " into epoch"
    local_struct_time = time.strptime(time_str, str_format)
    print "local struct time: " + str(local_struct_time)
    local_epoch_time = time.mktime(local_struct_time)
    print "local epoch time: " + str(local_epoch_time)
    return local_epoch_time

print str(int(get_local_time_str_to_epoch(str_format, time_str)*1000))
print str(int(time.time()*1000))
