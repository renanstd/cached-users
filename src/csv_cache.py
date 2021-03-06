import os
import csv


class CsvCache:

    def __init__(self):
        self.cache_file = os.path.abspath(os.getcwd()) + '/cache.csv'

    def save_cache(self, user_data):
        '''Armazena um usuário no cache CSV'''
        file_exists = os.path.exists(self.cache_file)

        with open(self.cache_file, mode='a', newline='') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=user_data.keys())

            if not file_exists:
                writer.writeheader()

            writer.writerow(user_data)

    def check_cache(self, user):
        '''Busca no cache CSV o user solicitado'''
        if not os.path.exists(self.cache_file):
            return False

        with open(self.cache_file, mode='r') as csv_file:
            reader = csv.DictReader(csv_file)
            for user_cached in reader:
                if user_cached['username'] == user:
                    return user_cached
