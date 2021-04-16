import base64
import binascii
from pyDes import des, ECB, PAD_PKCS5

def des_encrypt(user_list):
    '''
     DES 加密
    :DES_SECRET_KEY: 秘钥
    :content: 原始字符串
    :return: secret_content加密后字符串，base64
    '''

    if user_list and user_list[1]:
        content = str(user_list[1])


        DES_SECRET_KEY = 'MoveUnio'
        content = 'move_' + content
        # content = 'move_13761100490'

        des_obj = des(DES_SECRET_KEY, ECB, padmode=PAD_PKCS5)
        secret_content = str(base64.b64encode(des_obj.encrypt(content)), encoding='utf-8')
        secret_content = str(base64.b64encode(secret_content.encode('utf-8')), "utf-8")

        secret_content = secret_content.replace('+', '-', -1).replace('/', '_', -1).replace('=', '', -1)
        print(secret_content)
        return (user_list[0], secret_content)

def des_descrypt():
    """
     DES 解密
    :DES_SECRET_KEY: 秘钥
    :secret_content: 加密后字符串，base64
    :return: content原始字符串
    """

    DES_SECRET_KEY = 'MoveUnio'
    secret_content = 'eVNjZVZQL1hVTnhWTkxoMitlOGREL3hJQlJVSTU1U3o'

    secret_content = secret_content.replace('-', '+', -1).replace('_', '/', -1)
    if len(secret_content) % 3 == 1:
        secret_content += "=="
    elif len(secret_content) % 3 == 2:
        secret_content += "="

    des_obj = des(DES_SECRET_KEY, ECB, padmode=PAD_PKCS5)
    content = bytes.decode(des_obj.decrypt(binascii.a2b_base64(base64.b64decode(str.encode(secret_content))), padmode=PAD_PKCS5))

# if __name__== '__main__':
# #     des_encrypt()
#     des_descrypt()