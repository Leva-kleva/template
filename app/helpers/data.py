def get_or_create(session, model, obj, filters=None, update=False, pk=None, data_to_update=None):
    """
    Input: db session, db model, object, filters (is identification fields in model),
            update bool, pk - array primary key
    Output: refresh object, is_commit (boolean; True if commit, else False)
    """
    data = None
    if filters is not None:
        if isinstance(filters, dict):
            data = session.query(model).filter_by(**filters).one_or_none()
        else:
            data = session.query(model).filter(*filters).one_or_none()
    if data is None:
        session.add(obj)
        session.commit()
        session.refresh(obj)
        return obj, True
    if update:
        tmp = data_to_update if data_to_update else obj.dict()
        if pk:
            for key in pk: tmp.pop(key, None)
        session.query(model).filter_by(**filters).update(tmp)
        session.commit()
        session.refresh(data)

    return data, False
