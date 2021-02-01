import logging
from mongoengine.errors import DoesNotExist


logger = logging.getLogger(__name__)


def get_object(model, value, key="id"):
    try:
        target = model.objects.get(**{key: value})
    except DoesNotExist as e:
        logger.error(e, exc_info=True)
        target = None
    return target


def error_messages(target):
    error_messages = {
        'required': '{target}不能为空'.format(target=target),
        'invalid': '{target}错误'.format(target=target),
        'null': '{target}不能为空'.format(target=target),
        'blank': '{target}不能为空'.format(target=target),
        'max_length': '{0}长度不能超过{{max_length}}'.format(target),
        'min_length': '{0}长度不能少于{{min_length}}'.format(target),
        'max_value': '{0}值不能超过{{max_value}}'.format(target),
        'min_value': '{0}值不能小于{{min_value}}'.format(target),
    }
    return error_messages


# def token_required(f):
#    @wraps(f)
#    def decorator(*args, **kwargs):

#       token = None

#       if 'x-access-tokens' in request.headers:
#          token = request.headers['x-access-tokens']

#       if not token:
#          return jsonify({'message': 'a valid token is missing'})

#       try:
#          data = jwt.decode(token, app.config[SECRET_KEY])
#          current_user = Users.query.filter_by(public_id=data['public_id']).first()
#       except:
#          return jsonify({'message': 'token is invalid'})

#         return f(current_user, *args, **kwargs)
#    return decorator