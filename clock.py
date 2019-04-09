
import subprocess


def my_interval_job1():
    subprocess.call(['scrapy', 'crawl', 'indiatv'])


def my_interval_job2():
    subprocess.call(['scrapy', 'crawl', 'ndtv'])


def my_interval_job3():
    subprocess.call(['scrapy', 'crawl', 'republic'])


def my_interval_job4():
    subprocess.call(['scrapy', 'crawl', 'thehindu'])


def my_interval_job5():
    subprocess.call(['scrapy', 'crawl', 'zee'])


def my_interval_job6():
    subprocess.call(['scrapy', 'crawl', 'indianexpress'])


def my_interval_job7():
    subprocess.call(['scrapy', 'crawl', 'news18'])


def my_interval_job8():
    subprocess.call(['scrapy', 'crawl', 'firstpost'])


def my_interval_job9():
    subprocess.call(['scrapy', 'crawl', 'oneindia'])


def my_interval_job10():
    subprocess.call(['scrapy', 'crawl', 'dna'])


if __name__ == '__main__':
    from apscheduler.schedulers.blocking import BlockingScheduler
    sched = BlockingScheduler()

    sched.add_job(my_interval_job1, 'interval', id='indiatv', hours=6)
    sched.add_job(my_interval_job2, 'interval', id='ndtv',    hours=6)
    sched.add_job(my_interval_job3, 'interval', id='republic', hours=6)
    sched.add_job(my_interval_job4, 'interval', id='thehindu', hours=6)
    sched.add_job(my_interval_job5, 'interval', id='zee',     hours=6)
    sched.add_job(my_interval_job6, 'interval', id='indainexpress', hours=6)
    sched.add_job(my_interval_job7, 'interval', id='news18', hours=6)
    sched.add_job(my_interval_job8, 'interval', id='firstpost', hours=6)
    sched.add_job(my_interval_job9, 'interval', id='oneindia', hours=12)
    sched.add_job(my_interval_job10, 'interval', id='dna', hours=6)
    sched.start()
