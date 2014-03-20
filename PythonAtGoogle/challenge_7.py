# CHALLENGE 5: Let the user search for a word
# Instructions:
# * Delete 'raise BaseException...' statement
# * Replace ___1___ with print
# * Replace ___2___ with sorted
# * Replace ___3___ with wordCounts
# * Replace ___4___ with search
# * Replace ___5___ with info
# * Replace ___6___ with highestCount
# * Replace ___7___ with bestUrl
# * Replace ___8___ with highestCount
# * Replace ___9___ with print
# * Replace ___10___ with search
# * Replace ___11___ with highestCount
# * Replace ___12___ with bestUrl
#
# Advanced:
# * Report which site has the fewest occurrences of the search term.

raise BaseException("Stopping program")
___1___ '\n\n\nAvailable search terms:', ___2___(___3___.keys())
___4___ = raw_input('Please select a search term from the list above:')
___5___ = dict((val, key) for key, val in wordCounts[search].iteritems())
___6___ = sorted(info.keys()) [-1]
___7___ = info[___8___]
___9___('%s occurs the most times (%d) on %s' % (___10___, ___11___, ___12___))
