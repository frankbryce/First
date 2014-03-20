import os, re, random, string, sys
words = set(open('C:\Python27\include\pyconfig.h').read().split())
words = [word for word in words if re.match("^[a-z]+$", word)]
def field():
  if random.randint(1,20) < 19:
    return words[random.randint(0, len(words) -1)]
  else:
    return '<a href="%s.com">link</a>' % random.choice(string.lowercase)
pages = dict()
print 'Generating webpages a.com through z.com'
for i in string.lowercase:
  pages['%s.com' % i] = ' '.join([field() for j in range(0, 100)])
def solicitWebPage():
  return raw_input('enter a webpage such as a.com, b.com, ..., z.com: ')
def getWebPage(url):
  return pages[url]
wordCounts = dict()
def recordWord(word, url):
  if word not in wordCounts:
    wordCounts[word] = {}
  if url not in wordCounts[word]:
    wordCounts[word][url] = 0
  wordCounts[word][url] += 1

# CHALLENGE #2 - Identify how often each word occurs in the page.
# Instructions:
# * Delete 'raise BaseException...' statement
# * Replace ___1___ with recordPage
# * Replace ___2___ with word
# * Replace ___3___ with someWebpage
# * Replace ___4___ with recordWord
# * Replace ___5___ with recordPage
# * Replace ___6___ with print
# * Replace ___7___ with wordCounts
#
# Advanced:
# * Print just the list of identified words, not their counts
# * Exclude links from being recorded

def recordPage (someUrl, someWebpage):
  for word in someWebpage.split():
    recordWord(word, someUrl)
recordPage(url, result)
print(wordCounts)
