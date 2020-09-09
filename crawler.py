import logging
import re
from urllib.parse import urlparse
from urllib.parse import urljoin
from bs4 import BeautifulSoup


logger = logging.getLogger(__name__)


class Crawler:
    """
    This class is responsible for scraping urls from the next available link in frontier and adding the scraped links to
    the frontier
    """

    def __init__(self, frontier, corpus):
        self.frontier = frontier
        self.corpus = corpus
        self.counter = 0
        self.loop_counter = 0
        self.last_url = None
        self.linklist = []

        #For analytics part, uncomment this part to let the crawler keep track of all analytics information.

        """
        self.subdomain_dict = dict()
        self.valid_outlink = dict()
        self.download_url = []
        self.page_word_count = dict()
        self.frequency = dict()
        """

    def start_crawling(self):
        """
        This method starts the crawling process which is scraping urls from the next available link in frontier and adding
        the scraped links to the frontier
        """
        while self.frontier.has_next_url():
            url = self.frontier.get_next_url()
            logger.info("Fetching URL %s ... Fetched: %s, Queue size: %s", url, self.frontier.fetched, len(self.frontier))
            url_data = self.corpus.fetch_url(url)

            for next_link in self.extract_next_links(url_data):
                if self.is_valid(next_link):

                    if self.corpus.get_file_name(next_link) is not None:
                        self.frontier.add_url(next_link)

        #After the crawler fetched all the URLs from the frontier, write all the analytics result into local files.
        #Uncomment this part to let the crawler keep track of all analytics information.
        """
        self.write_result()
        """


    def write_result(self):
        """
        This method will write all the analytics result into local files.
        """

        file_1 = open("Analytics_Part_1.txt","w")
        file_2 = open("Analytics_Part_2.txt","w")
        file_3 = open("Analytics_Part_3.txt","w")
        file_4 = open("Analytics_Part_4.txt","w")
        file_5 = open("Analytics_Part_5.txt","w")

        for key,val in self.subdomain_dict.items():
        	file_1.write(key+":"+str(val)+"\n")


        most_valid_links = max(self.valid_outlink,key = self.valid_outlink.get)
        file_2.write("Most valid link is : "+most_valid_links)
        print("Most valid link is : ",most_valid_links)
        
        file_3.write("Downloaded URL's number is: "+str(len(self.download_url)))
        print("Downloaded URL's number is: ",len(self.download_url))

        longest_word_page = max(self.page_word_count,key = self.page_word_count.get)
        file_4.write("Longest page is: "+longest_word_page)
        print("Longest page is: ",longest_word_page)

        fq_list = sorted(self.frequency,key = self.frequency.get,reverse=True)[:50]

        for i in fq_list:
            file_5.write(str(i)+"\n")
            print(i,self.frequency[i])  

        file_1.close()
        file_2.close() 
        file_3.close() 
        file_4.close() 
        file_5.close()     

    def extract_next_links(self, url_data):
        """
        The url_data coming from the fetch_url method will be given as a parameter to this method. url_data contains the
        fetched url, the url content in binary format, and the size of the content in bytes. This method should return a
        list of urls in their absolute form (some links in the content are relative and needs to be converted to the
        absolute form). Validation of links is done later via is_valid method. It is not required to remove duplicates
        that have already been fetched. The frontier takes care of that.

        Suggested library: lxml
        """

        outputLinks = []

     	#For analytics part, uncomment this part to let the crawler keep track of all analytics information.

        """
        self.download_url.append(url_data["url"])
        """
      
        if url_data["is_redirected"] == True:

            if url_data["final_url"] != url_data["url"]:

                single_link = url_data["final_url"]
        		
                if single_link not in self.linklist:

	        	
                    if self.is_valid(single_link) == True:

                        self.last_url = single_link

                        parsed = urlparse(single_link)


 						#For analytics part, uncomment this part to let the crawler keep track of all analytics information.

                        """

                        subdomain = parsed.netloc
                        if "www." in subdomain:
                            subdomain = subdomain.replace("www.","")

                        if subdomain in self.subdomain_dict.keys():
                            self.subdomain_dict[subdomain] += 1
                        else:
                            self.subdomain_dict[subdomain] = 1


                        if url_data["url"] in self.valid_outlink.keys():
                            self.valid_outlink[url_data["url"]] += 1
                        else:
                            self.valid_outlink[url_data["url"]] = 1

                        """

                        self.linklist.append(single_link)
                        outputLinks = [url_data["final_url"]]

            else:	

                soup = BeautifulSoup(str(url_data["content"]))

                #For analytics part, uncomment this part to let the crawler keep track of all analytics information.

                """

                text = soup.get_text()

                word_list = tokenize(text,True)

                computeWordFrequencies(word_list,self.frequency)

                self.page_word_count[url_data["url"]] = len(word_list)

                """

                all_links = soup.find_all('a')
             	

                for link in all_links:

                    single_link = str(link.get('href'))

                    if single_link != None and len(single_link) != 0:

                        if self.valid_single_link(single_link) == True:
                    
                            single_link = urljoin(url_data["url"],single_link)

                            if single_link not in self.linklist:

	        	
                                if self.is_valid(single_link) == True:

                                    self.last_url = single_link
                                    self.linklist.append(single_link)
                                    outputLinks.append(single_link)


                                    #For analytics part, uncomment this part to let the crawler keep track of all analytics information.

                                    """

                                    parsed = urlparse(single_link)

                                    subdomain = parsed.netloc
                                    if "www." in subdomain:
                                        subdomain = subdomain.replace("www.","")

                                    if subdomain in self.subdomain_dict.keys():
                                    	self.subdomain_dict[subdomain] += 1
                                    else:
                                        self.subdomain_dict[subdomain] = 1

                                    if url_data["url"] in self.valid_outlink.keys():
                                        self.valid_outlink[url_data["url"]] += 1
                                    else:
                                        self.valid_outlink[url_data["url"]] = 1
                                    """
                                

        else:

            soup = BeautifulSoup(str(url_data["content"]))

            #For analytics part, uncomment this part to let the crawler keep track of all analytics information.

            """
            text = soup.get_text()

            word_list = tokenize(text,True)
            computeWordFrequencies(word_list,self.frequency)
            self.page_word_count[url_data["url"]] = len(word_list)
            """

            all_links = soup.find_all('a')

            for link in all_links:


                single_link = str(link.get('href'))

                if single_link != None and len(single_link) != 0:

                    if self.valid_single_link(single_link) == True:

                        single_link = urljoin(url_data["url"],single_link)



                        if single_link not in self.linklist:



                            if self.is_valid(single_link) == True:
                                self.last_url = single_link
                                self.linklist.append(single_link)
                                outputLinks.append(single_link)

                                #For analytics part, uncomment this part to let the crawler keep track of all analytics information.
                                """
                                parsed = urlparse(single_link)

                                subdomain = parsed.netloc
                                if "www." in subdomain:
                                    subdomain = subdomain.replace("www.","")

                                if subdomain in self.subdomain_dict.keys():
                                    self.subdomain_dict[subdomain] += 1
                                else:
                                    self.subdomain_dict[subdomain] = 1

                                if url_data["url"] in self.valid_outlink.keys():
                                    self.valid_outlink[url_data["url"]] += 1
                                else:
                                    self.valid_outlink[url_data["url"]] = 1
                                """

        return outputLinks

    def is_valid(self, url):
        """
        Function returns True or False based on whether the url has to be fetched or not. This is a great place to
        filter out crawler traps. Duplicated urls will be taken care of by frontier. You don't need to check for duplication
        in this method
        """
        parsed = urlparse(url)
        if parsed.scheme not in set(["http", "https"]):
            return False


        strurl = parsed.geturl()


        if self.dumb_check(url) == False:
        	return False

        if self.last_url != None:


            if strurl[-1] in "01234567890" and self.last_url[-1] in "01234567890":

                if parsed.path == urlparse(self.last_url).path:

                    current = parsed.geturl()
                    last = urlparse(self.last_url).geturl()

                    if self.is_growthing(last,current) == True:

                        self.counter += 1

                    if self.counter > 150:

                        return False
                else:
            	    self.counter = 0


            if self.detect_infinite_loop(strurl) == True:
        	    self.loop_counter += 1

            if self.loop_counter > 100:
        	    return False
        

        try:
            return ".ics.uci.edu" in parsed.hostname \
                   and not re.match(".*\.(css|js|bmp|gif|jpe?g|ico" + "|png|tiff?|mid|mp2|mp3|mp4" \
                                    + "|wav|avi|mov|mpeg|ram|m4v|mkv|ogg|ogv|pdf" \
                                    + "|ps|eps|tex|ppt|pptx|doc|docx|xls|xlsx|names|data|dat|exe|bz2|tar|msi|bin|7z|psd|dmg|iso|epub|dll|cnf|tgz|sha1" \
                                    + "|thmx|mso|arff|rtf|jar|csv" \
                                    + "|rm|smil|wmv|swf|wma|zip|rar|gz|pdf)$", parsed.path.lower())

        except TypeError:
            print("TypeError for ", parsed)
            return False

    def is_growthing(self,last,current):

        last_str = last[len(last)::-1]
        current_str = current[len(current)::-1]

        last_num = ""
        for i in last_str:
            if i in "1234567890":
                last_num += i
            else:
                break

        current_num = ""
        for p in current_str:
            if p in "1234567890":
                current_num += p
            else:
                break

        last_num = last_num[len(last_num)::-1]
        current_num = current_num[len(current_num)::-1]

        if int(current_num) - int(last_num) == 1 or int(last_num) - int(current_num) == 1:
            return True
        return False


    def valid_single_link(self,single_link):
        if single_link[0] == "\\":
            return False
        return True

    def detect_infinite_loop(self,current_url):



        last_url_list = self.last_url.split("/")
        current_url_list = current_url.split("/")

        if len(last_url_list) != len(current_url_list):

            self.loop_counter = 0
            return False
        else:
            length = len(current_url_list)

            if length < 6:
                return False
            else:
                for i in range(length - 1):
                    if last_url_list[i] != current_url_list[i]:
                        return False

        return True



    def dumb_check(self,url):

        parsed = urlparse(url)
        if parsed.scheme not in set(["http", "https"]):
            return False

        try:
            return ".ics.uci.edu" in parsed.hostname \
                   and not re.match(".*\.(css|js|bmp|gif|jpe?g|ico" + "|png|tiff?|mid|mp2|mp3|mp4" \
                                    + "|wav|avi|mov|mpeg|ram|m4v|mkv|ogg|ogv|pdf" \
                                    + "|ps|eps|tex|ppt|pptx|doc|docx|xls|xlsx|names|data|dat|exe|bz2|tar|msi|bin|7z|psd|dmg|iso|epub|dll|cnf|tgz|sha1" \
                                    + "|thmx|mso|arff|rtf|jar|csv" \
                                    + "|rm|smil|wmv|swf|wma|zip|rar|gz|pdf)$", parsed.path.lower())

        except TypeError:
            print("TypeError for ", parsed)
            return False



"""
This function will take O(n) time for execution since we only have one while loop
inside this function which is loop through every character in the text file for only
one time, and we add all the operations for every one step of the loop and we can come
up with the linear time operation relative to the size of the input.
"""
def tokenize(text,include_stopwords):

    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    stopwords = ["a","about","above","after","again","against","all", "am","an","and","any","are","aren't","as","at",
    "be","because","been","before","being","below","between","both","but","by","can't","cannot","could","couldn't",
    "did","didn't","do","does","doesn't","doing","don't","down","during","each","few","for","from","further","had",
    "hadn't","has","hasn't","have","haven't","having","he","he'd","he'll","he's","her","here","here's","hers","herself",
    "him","himself","his","how","how's","i","i'd","i'll","i'm","i've","if","in","into","is","isn't","it","it's","its",
    "itself","let's","me","more","most","mustn't","my","myself","no","nor","not","of","off","on","once","only","or",
    "other","ought","our","ours", "ourselves","out","over","own","same","shan't","she","she'd","she'll","she's","should",
    "shouldn't","so","some","such","than","that","that's","the",
    "their","theirs","them","themselves","then","there","there's","these","they",
    "they'd","they'll","they're","they've","this","those","through","to","too","under",
    "until","up","very","was","wasn't","we","we'd","we'll","we're","we've","were",
    "weren't","what","what's","when","when's","where","where's","which","while","who",
    "who's","whom","why","why's","with","won't","would","wouldn't","you","you'd","you'll",
    "you're","you've","your","yours","yourself","yourselves"
    ]

    Token_list = []

    token = ""
    
    for char in text:
        
        if char in letters:

            token += str(char)

        else:
            if include_stopwords == True:

                if token != "" and len(token) > 2 and token not in stopwords:
                    Token_list.append(token)
                    token = ""
                else:
                    token = ""
            else:

                if token != "" and len(token) > 2:
                    Token_list.append(token)
                    token = ""
                else:
                    token = ""
    return Token_list

"""
This function, which used for compute word frequencies, also uses O(n) time since we only
use one for-loop to go through the Token list for computing the frequencies. For every token
we only use O(1) time so if we have n tokens, we'll use O(1) * n = O(n) time for execution,
which is linear time relative to the size of the input.
"""
def computeWordFrequencies(Token_list,frequency):

    for i in Token_list:
        if i.lower() not in frequency.keys():
            frequency[i.lower()] = 1
        else:
            frequency[i.lower()] += 1

        
    
"""
This print function will sort the frequency dictionary first, then
print the frequency for every single token we have collected, for sorting, it
will take O(nlogn) time and for printing it will only take O(n) time, so the total
running time for this function will be O(nlogn).
"""
def print_frequencies(frequency):
    
    frequency = sorted(frequency.items(),key = lambda kv:(-kv[1],kv[0]))
    for item in frequency:
        print(item[0] + "\t" + str(item[1]))
