# encoding=utf-8

import re, urllib2, urllib


class zhilianzhaopin():
    def inter(self, job, base, startpage, endpage):
        url = "http://sou.zhaopin.com/jobs/searchresult.ashx?"
        urlall = url + urllib.urlencode({"jl": base}) + "&" + urllib.urlencode({"kw": job})
        for page in range(startpage, endpage + 1):
            fin_url = urlall + "&" + urllib.urlencode({"p": page})
            context = self.loadPage(fin_url, page)
            self.dealpage(context, page)

    def loadPage(self, url, page):
        print "正在爬取第" + str(page) + "页数据。。。。"
        header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"
        }

        request = urllib2.Request(url, headers=header)

        response = urllib2.urlopen(request)

        html = response.read()

        return html

    def dealpage(self, html, page):
        partten_href = re.compile(
            '<a style="font-weight: bold" par="ssidkey=y&amp;ss=\d+&amp;ff=\d+&amp;sg=\w+&amp;so=\d+" href="(.*?)" target="_blank">.*?</a>',
            re.S)
        href = partten_href.findall(html)
        for h in href:
            self.dealstep(h, page)

    def dealstep(self, html, page):
        html2 = self.loadPage(html, page)
        context = ""
        partten_title = re.compile('<h1>(.*?)</h1>', re.S)
        title = partten_title.findall(html2)
        for t in title:
            context += t + "\t"
        partten_company = re.compile(
            '<a onclick=".*?" href=".*?" target="_blank">(.*?)<img class=".*?" src=".*?.png" border="\d+" vinfo=".*?"></a>',
            re.S)
        company = partten_company.findall(html2)
        for c in company:
            cc = c.replace('<img title="专属页面" src="//img03.zhaopin.cn/2012/img/jobs/icon.png" border="0" />', "")
            context += cc + "\t"
        partten_money = re.compile('<li><span>职位月薪：</span><strong>(.*?)&nbsp;<a.*?>.*?</a></strong></li>', re.S)
        money = partten_money.findall(html2)
        for m in money:
            context += m + "\t"
        partten_request = re.compile('<li><span>工作经验：</span><strong>(.*?)</strong></li>', re.S)
        request = partten_request.findall(html2)
        for r in request:
            context += r + "\t"
        self.writePage(context, page)

    def writePage(self, context, page):
        print "正在将第" + str(page) + "页数据写入文件。。。"
        with open("zhilianzhangpin.txt", "a") as file:
            file.writelines(context + "\n")


if __name__ == '__main__':
    job = raw_input("请输入想找的岗位：")
    base = raw_input("请输入工作地点：")
    startpage = raw_input("请输入爬取的起始页：")
    endpage = raw_input("请输入爬取的终止页：")
    z = zhilianzhaopin()
    z.inter(job, base, int(startpage), int(endpage))
