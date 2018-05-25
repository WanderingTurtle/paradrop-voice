from setuptools import find_packages, setup

setup(name="paradrop-voice",
      version="0.1",
      description="Enable voice interactivity with a Paradrop node.",
      author="Paradrop Labs",
      author_email="info@paradrop.io",
      url="https://paradrop.org",
      packages=find_packages(),
      install_requires=[
          "certifi==2018.4.16",
          "chardet==3.0.4",
          "Flask==1.0.2",
          "idna==2.6",
          "numpy==1.14.3",
          "pocketsphinx==0.1.3",
          "PyAudio==0.2.11",
          "requests==2.18.4",
          "scipy==1.1.0",
          "urllib3==1.22"
      ],
      entry_points={
          "console_scripts": [
              "paradrop-voice = voice.voice:main"
          ]
      }
)