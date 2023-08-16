from setuptools import setup

with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='geokakao',
    version='0.1.1',
    description='Geospatial Features Using Kakao API',
    long_description = long_description,
    long_description_content_type='text/markdown',
    author='Byeong-Hyeok Yu',
    author_email='bhyu@knps.or.kr',
    url='https://github.com/osgeokr/geokakao',
    packages=['geokakao'],
    install_requires=[
        'requests',
        'pandas',
        'geopandas',
        ],
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
)
