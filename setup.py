from setuptools import setup

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(name='mailsendinghelper',
      version='0.1',
      # description='The funniest joke in the world',
      # url='http://github.com/storborg/funniest',
      # author='Luka Pavlica',
      # author_email='luka.pavlica93@gmail.com',
      # license='MIT',
      packages=['mailsendinghelper',
                'mailsendinghelper.fastfood',
                'mailsendinghelper.veganfood'
                ],
      install_requires=required,
      # zip_safe=False
)