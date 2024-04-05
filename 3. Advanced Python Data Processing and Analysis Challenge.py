# Task 1: Travel Blog Sentiment Analysis:

import re

reaction_words = {
    "positive": {"amazing", "enjoy", "beautiful", "breathtaking", "wonderful", "stunning", "fantastic", "excellent"},
    "negative": {"bad", "disappointing", "poor", "lackluster"}
}

def analyze_blog_sentiments(blog_file):
    with open(blog_file, 'r') as file:
        for line in file:
            # print(re.match(r"^\d", line, re.MULTILINE))
            if re.match(r"^\d", line, re.MULTILINE):
                words_pos = 0
                words_neg = 0

                for word in reaction_words["positive"]:
                    if word in line:
                        words_pos += 1
                
                for word in reaction_words["negative"]:
                    if word in line:
                        words_neg += 1

                print("This review:")
                print(line.strip()[3:])
                print(f"Contains {words_pos} positive words, and {words_neg} negative words\n")


analyze_blog_sentiments("travel_blogs.txt")


# Task 2: Historical Weather Data Compiler

def compile_weather_data(file_list):
    yearly_temps = {}

    for file_name in file_list:
        with open(file_name, 'r', encoding='utf-8') as file:
            total_temp = 0
            total_days = 0
            for line in file:
                day_temp_pair = line.strip().split(",")
                total_temp += int(re.match(r"\d+", day_temp_pair[1]).group())
                total_days += 1
            yearly_temps[re.search(r"\d+", file_name).group()] = total_temp / total_days
    
    for year, avg_temp in yearly_temps.items():
        print(f"Average temperature in {year}: {avg_temp}°C")

    max_temp = max(yearly_temps.values())
    hottest_year = list(yearly_temps.keys())[list(yearly_temps.values()).index(max_temp)]
    print(f"Hottest average year was {hottest_year} with an average temperature of {avg_temp}°C")

weather_file_list = ("weather_2020.txt", "weather_2021.txt")

compile_weather_data(weather_file_list)