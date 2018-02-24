INSTALATION FOR WINDOWS:
------------------------------------------------------------------------------------------

1. Python 3.6 Windows x86-64 executable installer (Make sure Pip is ticked as well as PATH)
https://www.python.org/downloads/release/python-364/

2. Visual C++ 2015 Build Tools
http://landinghub.visualstudio.com/visual-cpp-build-tools

3. Installing Scrapy with command pip install scrapy
https://doc.scrapy.org/en/latest/intro/install.html

4. Might also need to install with command pip install pypiwin32

RUNNING THE SCRIPT:
-----------------------------------------------------------------------------------------

1. Navigate to the folder with cd \aliexpress-master\aliexpress\aliexpress and run python create_new_db.py (prior delete aliexpress_db.sqlite with data). This will generate new database file. Need to be done only once.
2. To run the script you need to make sure you are in the \aliexpress-master\aliexpress\aliexpress directory, otherwise the script won't be able to find database file. There are two versions of the scraper aliexpress_spider.py- scrapes whole website and aliexpress_popular.py- scrapes only popular items.
To run the scraper you need simply type scrapy crawl aliexpress_spider or scrapy crawl aliexpress_popular
3. To export report need to run python export_report.py which is going to generate out.csv (SQL statement could be edited and start date and end date could be changed)
