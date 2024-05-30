# folder = "C:/User/x.xls"
# arpita = "D:/data/Arpita"
# # import shutil
# # import os
# #
# # try:
# #     for i in os.listdir():
# #         if i.lower()  ".xls":
# #             try:
# #                 path = i
# #
# #         shutil.move(i, arpita)
# # except as Exception e:
# #     return str(e)
# import os
#
#
# import requests
# from bs4 import BeautifulSoup
#
# # URL of the webpage you want to scrape
# url = 'https://google.com/bhilwara/hotel'
#
# # Send a GET request to the webpage
# response = requests.get(url)
#
# # Parse the HTML content of the page with BeautifulSoup
# soup = BeautifulSoup(response.content, 'html.parser')
#
# # Find the data you're interested in
# # This is just an example; you'll need to inspect the website's HTML to find the correct tags and classes
# data_items = soup.find_all('div', class_='data-item')
#
# # Extract and print the data
# for item in data_items:
#     title = item.find('h2').text
#     address = item.find('p', class_='address').text
#     price = item.find('span', class_='price').text
#     print(f'Title: {title}, Address: {address}, Price: {price}')

"""Given a string s, find the length of the longest substring without repeating characters.
Example 1:
Input: s = "abcdxyzxb"
Output: 7
Explanation: The answer is "abcdxyz", with the length of 7.
Example 2:
Input: s = "abcdabcbbxyzt"
Output: 5
Explanation: The answer is "bxyzt", with the length of 5.
Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring."""

# def
# def longest(s):
#     temp = {}
#     n = 0
#     ln = 0
#     for i in range(len(s)):
#         if s[i] in temp and n<=temp[s[i]]:
#             n = temp[s[i]]+1
#         else:
#             ln = max(ln,i-n+1)
#         temp[s[i]] = i
#     return ln
#
# print(longest("abcdxyzxb"))
# print(longest("abcdabcbbxyzt"))
# print(longest("pwwkew"))
#
# MOD = 10**9 + 7
# def pureString(stn):
#     n = len(stn)
# 	if n <= 1:
#         tem = 0
#     char_counts = {}
#     for char in stn:
#         char_counts[char] = char_counts.get(char, 0) + 1
# 	if len(char_counts) == 1:
#         tem =  n - 1
# 	remaining_chars = 0
#     for count in char_counts.values():
#         if count == 1:
#             remaining_chars += 1
#             if remaining_chars > 1:
#                 return 0
# 	total_removals = 0
#     for count in char_counts.values():
# 		if count > 1:
#             total_removals += count - 1
# 	return total_removals % MOD
#

def find_first_non_repeating(lst):
    counts = {}
    for num in lst:
        counts[num] = counts.get(num, 0) + 1
    for num in lst:
        if counts[num] == 1:
            return num
    return None

# Example usage:
my_list = [1, 2, 2, 3, 4, 4, 5]
print("First non-repeating element:", find_first_non_repeating(my_list))


def find_all_non_repeating(lst):
    counts = {}
    non_rep = []
    for num in lst:
        counts[num] = counts.get(num, 0) + 1
    for num in lst:
        if counts[num] == 1:
            non_rep.append(num)
    return non_rep
    # return None

# Example usage:
my_list = [1, 2, 2, 3, 4, 4, 5]
print("First non-repeating element:", find_all_non_repeating(my_list))

A=[1, 2, 3, 2, 5, 1,3,5]
unique=[i for i in A if A.count(i)==1]
if unique != []:
    print(unique[0])
else:
    print(unique)

A=[1, 2, 3, 2, 5, 1,5]
rep=[i for i in A if A.count(i)>1]
element_counts = {element: A.count(element) for element in A if A.count(element)>1}
print(element_counts)
new_dict = {k: v for k, v in element_counts.items() if element_counts[k] > 1}
print(new_dict)
if rep != []:
    print(rep)
else:
    print(rep)


def find_missing_number(lst):
    n = len(lst) + 1
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(lst)
    return expected_sum - actual_sum

# Example usage:
my_list = [1, 2, 3, 5, 6, 7, 8, 9, 10]
print("Missing number:", find_missing_number(my_list))


def find_majority_element(lst):
    counts = {}
    for num in lst:
        counts[num] = counts.get(num, 0) + 1
    majority_count = len(lst) // 2 + 1
    for num, count in counts.items():
        if count >= majority_count:
            return num
    return None

# Example usage:
my_list = [1, 2, 2, 2, 3, 4, 2, 2, 2,3]
print("Majority element:", find_majority_element(my_list))

def split_into_chunks(lst, size):
    l = [lst[i:i+size] for i in range(0, len(lst), size)]
    return l

# Example usage:
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
chunk_size = 3
print("List chunks:", split_into_chunks(my_list, chunk_size))


def longest_consecutive_sequence(lst):
    longest_sequence = []
    current_sequence = []
    for num in sorted(lst):
        if not current_sequence or num == current_sequence[-1] + 1:
            current_sequence.append(num)
        else:
            if len(current_sequence) > len(longest_sequence):
                longest_sequence = current_sequence
            current_sequence = [num]
    return longest_sequence if len(longest_sequence) > len(current_sequence) else current_sequence

# Example usage:
my_list = [100, 4, 200, 1, 3, 2]
print("Longest consecutive sequence:", longest_consecutive_sequence(my_list))

def rotate_list(lst, steps):
    steps = steps % len(lst)
    return lst[-steps:] + lst[:-steps]

# Example usage:
my_list = [1, 2, 3, 4, 5]
steps_to_rotate = 2
print("Original list:", my_list)
print("List after rotating by", steps_to_rotate, "steps:", rotate_list(my_list, steps_to_rotate))

def find_last_occurrence(lst, element):
    return len(lst) - 1 - lst[::-1].index(element)

# Example usage:
my_list = [10, 20, 30, 40, 20]
element_to_find = 20
print("Index of the last occurrence of", element_to_find, ":", find_last_occurrence(my_list, element_to_find))

def longest_common_prefix(lst):
    if not lst:
        return ""
    min_str = min(lst, key=len)
    for i, char in enumerate(min_str):
        for string in lst:
            if string[i] != char:
                return min_str[:i]
    return min_str

# Example usage:
my_list = ["flower", "flow", "flight"]
print("Longest common prefix:", longest_common_prefix(my_list))

def longest_increasing_subsequence(lst):
    if not lst:
        return []
    dp = [1] * len(lst)
    for i in range(1, len(lst)):
        for j in range(i):
            if lst[i] > lst[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    max_length = max(dp)
    max_index = dp.index(max_length)
    subsequence = [lst[max_index]]
    current_length = max_length - 1
    for i in range(max_index - 1, -1, -1):
        if dp[i] == current_length and lst[i] < subsequence[-1]:
            subsequence.append(lst[i])
            current_length -= 1
    return subsequence[::-1]

# Example usage:
my_list = [3, 1, 4, 1, 5, 9, 2, 6, 5]
print("Longest increasing subsequence:", longest_increasing_subsequence(my_list))

def find_subsets(lst):
    subsets = [[]]
    for element in lst:
        subsets += [current_subset + [element] for current_subset in subsets]
    return subsets

# Example usage:
my_list = [1, 2, 3]
print("All possible subsets:", find_subsets(my_list))


# Define a generator to generate a list of numbers
def generate_numbers(n):
    for i in range(1, n + 1):
        yield i

# Define a decorator to modify the list with the square of each element
def square_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return [x ** 2 for x in result]
    return wrapper

# Apply the decorator to the generator function
@square_decorator
def generate_squared_numbers(n):
    return generate_numbers(n)

# Generate a list of numbers and modify it with the square of each element
n = 5
result = generate_squared_numbers(n)
print("List with squares of numbers up to", n, ":", result)




class Dummy:
    count = 0 # class variable (access by all the instance)
    def __init__(self,name,age,phone): #constructor
        self.name = name #instance variable (access by only own object)
        self.age = age
        self.phone = phone
        Dummy.count+=1
    def get_detail(self):
        print(self.name,self.age,self.phone)

    def edit_detail(self):
        self.phone = +91

    def delete_details(self):
        del self.phone


D = Dummy("arpita",24,9602781943)
print(D.count)
D = Dummy("arpita",24,9602781943)
print(D.count)

# import pandas as pd
# import numpy as np
# info = pd.DataFrame([[2, 7]] * 4, columns=['P', 'Q'])
# info.apply(np.sqrt)
# info.apply(np.sum, axis=0)
# info.apply(np.sum, axis=1)
# info.apply(lambda x: [1, 2], axis=1)
# info.apply(lambda x: [1, 2], axis=1, result_type='expand')
# info.apply(lambda x: pd.Series([1, 2], index=['foo', 'bar']), axis=1)
# info.apply(lambda x: [1, 2], axis=1, result_type='broadcast')
# print(info)

from collections import defaultdict
import statistics

emp_data = [
    {"Name": "Ravi", "Salary": 30000, "Location": "Mumbai"},
    {"Name": "Santhosh", "Salary": 20000, "Location": "Bangalore"},
    {"Name": "Anu", "Salary": 40000, "Location": "Mumbai"},
    {"Name": "Raju", "Salary": 35000, "Location": "Bangalore"},
    {"Name": "Sita", "Salary": 25000, "Location": "Delhi"}
]

# 1) No of employees in each location
location_count = defaultdict(int)
for emp in emp_data:
    location_count[emp["Location"]] += 1

print("1) Number of employees in each location:")
for location, count in location_count.items():
    print(f"{location}: {count}")

# 2) Min, Max, Avg Salary of each location
salary_stats = defaultdict(list)
for emp in emp_data:
    salary_stats[emp["Location"]].append(emp["Salary"])

print("\n2) Salary statistics of each location:")
for location, salaries in salary_stats.items():
    min_salary = min(salaries)
    max_salary = max(salaries)
    avg_salary = statistics.mean(salaries)
    print(f"{location}: Min Salary - {min_salary}, Max Salary - {max_salary}, Avg Salary - {avg_salary}")


emp_data = [
    {"Name": "Ravi", "Salary": 30000, "Location": "Mumbai"},
    {"Name": "Santhosh", "Salary": 20000, "Location": "Bangalore"},
    {"Name": "Anu", "Salary": 40000, "Location": "Mumbai"},
    {"Name": "Raju", "Salary": 35000, "Location": "Bangalore"},
    {"Name": "Sita", "Salary": 25000, "Location": "Delhi"}
]

# 1) No of employees in each location
location_count = {}
for emp in emp_data:
    if emp["Location"] not in location_count:
        location_count[emp["Location"]] = 0
    location_count[emp["Location"]] += 1

print("1) Number of employees in each location:")
for location, count in location_count.items():
    print(f"{location}: {count}")

# 2) Min, Max, Avg Salary of each location
salary_stats = {}
for emp in emp_data:
    if emp["Location"] not in salary_stats:
        salary_stats[emp["Location"]] = []
    salary_stats[emp["Location"]].append(emp["Salary"])

print("\n2) Salary statistics of each location:")
for location, salaries in salary_stats.items():
    min_salary = min(salaries)
    max_salary = max(salaries)
    avg_salary = sum(salaries) / len(salaries)
    print(f"{location}: Min Salary - {min_salary}, Max Salary - {max_salary}, Avg Salary - {avg_salary}")
