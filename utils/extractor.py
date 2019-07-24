# -*- coding: utf-8 -*-
import json
import jsonpath
#from utils.client import Httpclient
class Extractor(object):
    def __init__(self,body):
        if  isinstance(body,dict):
            self.body=body

    def extract(self,query=None):
        try:
            return  jsonpath.jsonpath(self.body,query)
        except Exception as e:
            raise ValueError("Invalid query: " + query + " : " + str(e))


if __name__ == '__main__':
    book_store = {
"store": {
"book": [
{
"category": "reference",
"author": "Nigel Rees",
"title": "Sayings of the Century",
"price": 8.95
},
{
"category": "fiction",
"author": "Evelyn Waugh",
"title": "Sword of Honour",
"price": 12.99
},
{
"category": "fiction",
"author": "Herman Melville",
"title": "Moby Dick",
"isbn": "0-553-21311-3",
"price": 8.99
},
{
"category": "fiction",
"author": "J. R. R. Tolkien",
"title": "The Lord of the Rings",
"isbn": "0-395-19395-8",
"price": 22.99
}
],
"bicycle": {
"color": "red",
"price": 19.95
}
},
"expensive": 10
}
# 查询store下的所有元素
print(jsonpath.jsonpath(book_store, '$.store.*'))

# 获取json中store下book下的所有author值
print(jsonpath.jsonpath(book_store, '$.store.book[*].author'))

# 获取所有json中所有author的值
print(jsonpath.jsonpath(book_store, '$..author'))

# 获取json中store下所有price的值
print(jsonpath.jsonpath(book_store, '$.store..price'))

# 获取json中book数组的第3个值
print(jsonpath.jsonpath(book_store, '$.store.book[2]'))

# 获取所有书
print(jsonpath.jsonpath(book_store, '$..book[0:1]'))

# 获取json中book数组中包含isbn的所有值
print(jsonpath.jsonpath(book_store, '$..book[?(@.isbn)]'))

# 获取json中book数组中price<10的所有值
print(jsonpath.jsonpath(book_store, '$..book[?(@.price<10)]'))