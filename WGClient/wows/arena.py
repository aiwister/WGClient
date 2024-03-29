from .exception import *
from ..util.utils import get_json


class Arena:

    def __init__(self, application_id, conv, lang, name=None):
        self.application_id = application_id
        self.conv = conv
        self.lang = lang
        self.value = self.conv(self._get_arena(name))
        self.origin = self._get_arena(name)

    def _get_arena(self, name):
        data = get_json(self.application_id,
                        "encyclopedia/battlearenas",
                        language=self.lang)
        res = None
        if not name:
            return data
        else:
            for i in data["data"]:
                if data["data"][i]["name"] == name:
                    res = data["data"][i]
                    break
                else:
                    continue
            if res:
                return res
            else:
                raise ArenaNotFound("arena not found")

    def __str__(self):
        return str(self.origin)
