

async def insert_app_info(mongo, app_collection, doc={}):

    result = await mongo.app_collection.insert_one(doc)
    print('result %s' % repr(result.inserted_id))


async def get_app_info(app_collection, app_ids, language):
    rv = await (app_collection.find_one(
        {'app_ids': app_ids})
    )
    return rv['language'] if rv else None
