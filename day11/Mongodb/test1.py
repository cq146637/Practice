__author__ = 'Cq'

import pymongo
import random



def add_data(collection):
    first_name = ["陈","张","李","王","赵"]
    second_name = ["冰","鑫","程","爱","暖"]
    third_name = ["强","国","明","风","芬"]
    data = [
        {"_id":int("1000"+str(i)),
         "name":random.choice(first_name)+
                random.choice(second_name)+
                random.choice(third_name),
         "age":random.randint(16,60),
         "high":random.randint(170,190),
         "list":list(random.randint(1,200) for i in range(10))
        } for i in range(5)
    ]
    try:
        for record in data:
            collection.save(record)
    except pymongo.errors.DuplicateKeyError:
        print('record exists')
    except Exception as e:
        print(e)


def delete_data(collection):
    remove_before = collection.find()
    print('---------------delete before--------------------')
    for obj in remove_before:
        print(obj)

    collection.delete_many({'age':{'$gt':20,'$lt':30}})   #删除所有满足条件的文档,删除_id大于6，小于100
    collection.delete_one({'age':20})                     #删除一条满足条件的文档,删除_id=6
    #collection_set01.delete_many({})                     #删除整个集合
    remove_after = collection.find()

    print('---------------delete after--------------------')
    for obj in remove_after:
        print(obj)


def update_data(collection):
    collection.replace_one({'_id': 10000}, {'name': '王宝宝'})                         #replace_one用指定的key-value替代原来所有的key-value
    collection.update_one({"_id": {'$lt': 10008}}, {'$set': {"age": "19"}})           #update_one更新已经对应的key-value，其它不变
    collection.update_many({'_id': {'$gt': 10007}}, {'$set': {'age': '50'}})          #同上，能够update所有符合匹配条件的文档



def select_data(collection):

    print('\n------------身高小于180:')
    print(type(collection.find({'high':{'$lt':180}})))
    for row in collection.find({'high':{'$lt':180}}):
        print(row)
    print(type(collection.find_one({'high':{'$lt':180}})))
    print('use find_one:',collection.find_one({'high':{'$lt':180}})['high'])
    print('use find_one:',collection.find_one({'high':{'$lt':180}}))

    print('\n------------查询特定键')
    print('------------查询身高大于170,并只列出_id,high和age字段(使用列表形式_id默认打印出来,可以使用{}忽视_id):')
    for row in collection.find({'high':{'$gt':170}},projection=['high','age']):
        print(row)

    print('\n------------skip参数用法')
    for row in collection.find({'high':{'$gt':170}},['high','age'],skip=1):
        print(row)
    for row in collection.find({'high':{'$gt':170}},['high','age']).skip(1):
        print(row)

    print('\n------------limit参数用法')
    for row in collection.find({'high':{'$gt':170}},['high','age'],limit=1):
        print(row)

    print('\n------------用{}描述特定键')
    for row in collection.find({'high':{'$gt':170}},{'high':1,'age':1,'_id':False}):
        print(row)

    print('\n------------多条件查询')
    print(collection.find_one({'high':{'$gt':10},'age':{'$lt':26,'$gt':10}}))


    # for u in db.users.find({"age":{"$nin":(23, 26, 32)}}):
    # print u
    # select * from users where age not in (23, 26, 32)

    print('\n------------count')
    print(collection.find({"age":{"$gt":20}}).count())

    print('\n------------条件或')
    print('大于等于29或者小于23')
    for row in collection.find({"$or":[{"age":{"$lte":23}}, {"age":{"$gte":29}}]}):
        print(row)

    print('\n------------exists')
    for row in collection.find({'age':{'$exists':True}}):
        print('age exists',row) # select * from 集合名 where exists 键1
    for row in collection.find({'age':{'$exists':False}}):
        print('age not exists',row)

    print('\n------------正则表达式查询')
    print('method 1')
    for row in collection.find({'name':{'$regex':r'.*暖.*'}}):
        print(row)
    print('method 2')
    import re
    Regex = re.compile(r'.*爱.*',re.IGNORECASE)
    for row in collection.find({'name':Regex}):
        print(row)

    print('\n------------使用sort排序(文档中没有排序的字段也会打印出来,表示最小)')
    print('------------age 升序')
    for row in collection.find().sort([["age",pymongo.ASCENDING]]):
        print(row)
    print('------------age 降序')
    for row in collection.find().sort([("age",-1)]):
        print(row)
    print('------------age升序,high升序')
    for row in collection.find().sort((("age",pymongo.ASCENDING),("high",pymongo.ASCENDING))):
        print(row)
    print('------------age升序，high降序')
    for row in collection.find(sort=[("age",pymongo.ASCENDING),("high",pymongo.ASCENDING)]):
        print(row)

    print('\n------------$all')
    for row in collection.find({'list':{'$all':[77,117,165,37,57,49,178,90,3,166]}}):
        print(row)

    print('\n------------$in')
    for row in collection.find({'list':{'$in':[2,3,4]}}):
        print(row)

    print('\n------------size=10')
    for row in collection.find({'list':{'$size':10}}):
        print(row)


    # print('-------------------$unset')
    # print('$unset和$set相反表示移除文档属性')
    # print('---before')
    # for row in collection.find({'name': "张程芬"}):
    #     print(row)
    # collection.update({'name':'张程芬'},{'$unset':{'age':1}})
    # print('---after')
    # for row in collection.find({'name':'张程芬'}):
    #     print(row)



def main():
    client = pymongo.MongoClient('192.168.198.128', 27017, username='guest', password='123456')

    db = client.test

    collection = db.test

    add_data(collection)

    update_data(collection)

    select_data(collection)

    delete_data(collection)


if "__main__" == __name__:
    main()