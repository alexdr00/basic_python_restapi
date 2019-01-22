def find_by_id(model, _id):
    try:
        doc = model.objects(id=_id)[0]
    except IndexError:
        return None

    return doc


def update_by_id(model, _id, **data):
    return model.objects(id=_id).modify(new=True, **data)


def delete_by_id(model, _id):
    return model.objects(id=_id).delete()


def create_resource(model, **data):
    return model(**data).save()
