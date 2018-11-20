import httplib, urllib
import urlparse

class HttpReq(object):
    @staticmethod
    def __get_http_host(host):
        if not host.startswith("http://"):
            raise RuntimeError("please start use 'http://'")
        parse_res = m_parse.urlparse(host)
        return {"host": parse_res.netloc, "path": parse_res.path, "query": parse_res.query}

    @staticmethod
    def __combine_query(param):
        if not isinstance(param, dict):
            raise RuntimeError("param must a dict type")
        res_tmp = []
        for k, v in param.items():
            res_tmp.append("%s=%s" % (k, v))
        return '&'.join(res_tmp)

    def get_request(self, host, param, headers=None):
        parse_res = self.__get_http_host(host)
        conn = m_http.HTTPConnection(parse_res["host"])
        if parse_res["query"]:
            query_part = self.__combine_query(param) + "&" + parse_res["query"]
        else:
            query_part = self.__combine_query(param)
        req_path = parse_res["path"] + "?" + query_part
        conn.request("GET", req_path, headers=headers if headers else {})
        respon = conn.getresponse()
        if respon.status == 200:
            res = respon.read()
            if isinstance(res, bytes):
                res = res.decode('utf-8')
            return res
        else:
            raise RuntimeError("HTTP错误码【%s】,错误内容" % respon.status)






host = "http://www.baidu.com"
param = {"123":"321"}

a = HttpReq()
b = a.get_request("http://www.baidu.com", param)
print b


