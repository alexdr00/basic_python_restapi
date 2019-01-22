from flask_restful import marshal


def resource_not_found_message(resource_name):
    error_message = {
        'message': {
            'content': f'{resource_name} not found',
            'type': 'error'
        }
    }

    return error_message, 404


def resource_or_not_found(resource_name,
                          resource,
                          resource_fields,
                          delete=False):
    if not resource:
        return resource_not_found_message(resource_name)

    if delete:
        return None, 204

    return marshal(resource, resource_fields)
