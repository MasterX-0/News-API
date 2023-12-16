from setuptools import setup, find_packages

setup(
    name='MNewsAPI',
    version='0.1.0',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GPL-3.0 License',
        'Operating System :: OS Independent',
    ],
    author='MasterX',
    description='This is a free and versatile news service that provides users with real-time updates and a comprehensive range of news content. This API offers JSON results, ensuring easy integration into your applications or websites. Stay updated with the latest news from various sources, including popular news outlets like Hiru News and Adaderana News.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/MasterX-0/News-API',
    project_urls={
        'Source': 'https://github.com/MasterX-0/News-API',
    },
)
