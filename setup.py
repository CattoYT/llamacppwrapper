from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as _f:
    _README_MD = _f.read()

_VERSION = '0.1.0'
try:
    import llama_cpp
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "llama-cpp-python", "--extra-index-url", "https://abetlen.github.io/llama-cpp-python/whl/cu122"])

setup(
    name='llama_cpp_wrapper',
    version=_VERSION,
    description='Wrapper for llama cpp cuz I was lazy',
    long_description=_README_MD,
    long_description_content_type='text/markdown',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Typing :: Typed"
    ],
    url='https://github.com/CattoYT/llamacppwrapper',  # Replace with your repository URL.
    download_url='https://github.com/.../.../tarball/{}'.format(_VERSION),  # Replace with your repository URL.
    packages=find_packages(),  # Automatically find packages.
    install_requires=[
        'llama_cpp', 
    ],
    test_suite="tests",
    include_package_data=True,
    python_requires='>=3.6',
)
