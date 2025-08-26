from load_data import LoadData

class ManagerData:

    def __init__(self):
        #loading the data
        loader = LoadData()
        self.newsgroups_interesting = loader.load_interesting()
        self.newsgroups_not_interesting = loader.load_not_interesting()

    #return the all the interesting data
    def get_interesting_data(self):
        return self.newsgroups_interesting.data

    # return the all the not interesting data
    def get_not_interesting_data(self):
        return self.newsgroups_not_interesting.data

    #return top 20 newsgroups 10 from interesting and 10 from not_interesting
    def get_20_newsgroups(self):
        try:
            interesting = self.newsgroups_interesting.data[:10]
            not_interesting = self.newsgroups_not_interesting.data[:10]

            return {
                "interesting": interesting,
                "not_interesting": not_interesting
            }
        except Exception as e:
            print("Error sending message:", e)
            return {}


# m = ManagerData()
#
# print(m.get_20_newsgroups())