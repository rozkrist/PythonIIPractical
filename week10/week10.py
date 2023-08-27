# 1.Parallel Matrix Multiplication:
#Implement parallel matrix multiplication using the concurrent.futures
#module to speed up the computation of large matrices. (you can declare the matrixes using, ex. lists or tuples)

#import concurrent.futures

#def multiply(a, b):
#     value = a * b
#     print(f"{a} * {b} = {value}") 

#if __name__ == "__main__":
# with concurrent.futures.ThreadPoolExecutor() as executor:
#    for i in range(3):
#        executor.submit(multiply, a=1, b=1)


#2.Distributed Web Scraping:
#Select a website. Distribute web scraping tasks across multiple processes or threads using libraries
#like concurrent.futures or Scrapy to gather data from various websites simultaneously. 


#import concurrent.futures
#import requests

#URLS = ["https://www.bbc.co.uk/",
#        "https://www.cnn.com/",
#        "https://www.foxnews.com/",
#        "https://www.reuters.com/",
#        "https://www.aljazeera.com/"]


#def scraping_website(url):
#    response = requests.get(url)
#    return response.text[:200]


#with concurrent.futures.ThreadPoolExecutor() as executor:
#    results = executor.map(scraping_website, URLS) 

#for url, result in zip(URLS, results):
#    print (f"data from {url}: {result}")

    

#3.Parallel Word Count:
#Distribute the task of counting words in multiple text files across
#multiple processes using the concurrent.futures module.

#import multiprocessing

#def word_count(filename):
#    with open(filename, "r") as file:
#        text = file.read()
#        words = text.split()
#        return len(words)
    

#if __name__ == "__main__":
#    num_workers = multiprocessing.cpu_count()
#       file_names = ["Africa.txt", "Etymology.txt", "History.txt"]

        
#with multiprocessing.Pool(num_workers) as pool:
#   result = pool.map(word_count, file_names) 

#for filename, count in zip(file_names, result):
#    print(f"Word count of {filename}: {count}")