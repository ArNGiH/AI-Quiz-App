from setuptools import find_packages,setup


setup(
    name='mcqgen',
    version='0.0.1',
    author='aryan nayar',
    author_email='aryan',
    install_requires=["openai","langchain","streamlit","python-dotenv","PyPDF2"],
    packages=find_packages()
)