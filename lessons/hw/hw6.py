
# Эта библиотека нужна для генерации случайных данных (имена, адреса и т.д.)
from faker import Faker

fake = Faker()

print("Name", fake.name())
print("Email:", fake.email())
print("City:", fake.city())


nums = [2, 7, 11, 15]
target = 9

for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] == target:
            print([i, j])