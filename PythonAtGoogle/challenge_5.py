# CHALLENGE #3: Crawl the web for links.
# Instructions:
# * Delete 'raise BaseException...' statement
# * Replace ___1___ with urlsVisited
# * Replace ___2___ with crawlForLinks
# * Replace ___3___ with someUrl
# * Replace ___4___ with urlsVisited
# * Replace ___5___ with urlsVisited
# * Replace ___6___ with someUrl
# * Replace ___7___ with someWebPage
# * Replace ___8___ with getWebPage
# * Replace ___9___ with links
# * Replace ___10___ with someWebPage
# * Replace ___11___ with link
# * Replace ___12___ with crawlForLinks
# * Replace ___13___ with allLinks
# * Replace ___14___ with crawlForLinks
# * Replace ___15___ with print
# * Replace ___16___ with allLinks
#
# Advanced:
# * g.com has been blacklisted; make sure we never crawl it for links!
# * The server can't handle this many links; once we have collected 50 links
#   we should stop crawling.

urlsVisited = set()
def crawlForLinks(someUrl):
  if someUrl in urlsVisited:
    return set()
  else:
    urlsVisited.add(somUrl)
  someWebPage = getWebPage(someUrl)
  links = re.compile("href\s*=\s*\"\s*([^\"]+)\"").findall(someWebPage)
  for link in links:
    links += crawlForLinks(link)
  return set(links)

allLinks = crawlForLinks(url)
print allLinks
