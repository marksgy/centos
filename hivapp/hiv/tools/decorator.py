from hiv.tools.exception import Unauthorized
from hiv.tools.verification import Verify_Rd3
from oflMsgForm.views import getFormId


def check_rd3_decorator(func):
    def wapper(*args, **kwargs):
        request = args[0]
        rd3 = request.POST.get('access_token')
        # 先检测jwt是否是有效请求
        effection = Verify_Rd3(rd3)
        if effection:
            getFormId(request)
            return func(*args, **kwargs)
        if not effection:
            raise Unauthorized('reregister')
    return wapper

