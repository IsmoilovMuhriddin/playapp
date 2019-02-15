
""" document obj
{ 
    ids: "", 
    permission_sets: [ 
        {
            'lang':'',
            'permissions':[]
        },   
    ]
}

"""
from bson.son import SON


async def insert_app_info(mongo, app_collection, app_ids, language, permissions):
    # result = await mongo.app_collection.insert_one(app_ids, language, permissions)
    result = await mongo.app_collection.update_one(
        {
            'ids': app_ids
        },
        {
            '$push': {
                'permission_sets': {
                    '$each': [{'lang': language, 'permissions': permissions}]
                }
            }
        },
        upsert=True
    )

    return result['permission_sets']


async def get_app_info(mongo, app_collection, app_ids, language):
    rv = await mongo.app_collection.aggregate([
        {'$match': {
            '$and': [
                {'ids': app_ids}

            ]}},
        {'$project': {
            'permissions': {'$filter': {
                '$input': '$permission_sets',
                '$as': 'perm',
                '$cond': {'$eq': ['$$perm.lang', language]}
            }}
        }}
    ])

    return rv if rv else None
