
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




async def get_app_info(mongo, app_collection, app_ids, language):
    rv =  mongo.app_collection.aggregate(
        [{
            '$match':{'ids':app_ids}
        },
            {  
            '$project': {
                "permission_sets": {
                    '$filter': {
                        'input': "$permission_sets",
                        'as': "perm",
                        'cond': {
                            '$eq': ["$$perm.lang", language]
                        }
                    }
                },
                '_id':0
            }
            
        }]

    )

    
    async def f(cursor):
        if cursor is None :
            return None
        async for doc in cursor:
            return doc
    
    result = await f(rv)
    return result if result and len(result['permission_sets'])>0 else None


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

    return await get_app_info(mongo, app_collection, app_ids, language)
